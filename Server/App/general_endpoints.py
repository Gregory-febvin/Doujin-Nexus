# app/general_endpoints.py
from flask import Blueprint, jsonify, request, url_for, current_app
from werkzeug.exceptions import BadRequest, InternalServerError

from .database import fetch_all, fetch_one
from .image_handle import build_image_urls

general_bp = Blueprint('general', __name__)

@general_bp.route('/api/sauces', methods=['GET'])
def get_all_sauces():
    try:
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 25))
        if page <= 0 or limit <= 0:
            raise BadRequest("Page and limit must be positive integers.")
        offset = (page - 1) * limit

        query = "SELECT id, title FROM galleries LIMIT ? OFFSET ?"
        sauces = fetch_all(query, (limit, offset))

        result = []
        for sauce in sauces:
            sauce_dict = dict(sauce)
            sauce_id = sauce_dict.get("id")
            sauce_dict["cover"] = url_for('image.get_cover_path', sauce_id=sauce_id, _external=True)
            result.append(sauce_dict)

        return jsonify(result), 200

    except ValueError:
        raise BadRequest("Page and limit must be integers.")

    except KeyError as e:
        raise BadRequest(f"Missing required query parameter: {str(e)}")

    except Exception as e:
        raise InternalServerError(f"An unexpected error occurred: {str(e)}")

@general_bp.route('/api/sauce/<int:sauce_id>', methods=['GET'])
def get_specific_sauce(sauce_id):
    try:
        sauceID = int(sauce_id)

        query_galleries_details = "SELECT * FROM galleries_details WHERE id = ?;"

        query_galleries = """
            SELECT 
            g.title,
            g.pages,
            GROUP_CONCAT(DISTINCT a.name) AS artists,
            GROUP_CONCAT(DISTINCT grp.name) AS groups,
            GROUP_CONCAT(DISTINCT l.name) AS languages,
            GROUP_CONCAT(DISTINCT p.name) AS parodies,
            GROUP_CONCAT(DISTINCT c.name) AS categories,
            GROUP_CONCAT(DISTINCT t.name) AS tags
        FROM 
            galleries g
        LEFT JOIN 
            gallery_artists ga ON g.id = ga.gallery_id
        LEFT JOIN 
            artists a ON ga.artist_id = a.id
        LEFT JOIN 
            gallery_groups ggr ON g.id = ggr.gallery_id
        LEFT JOIN 
            groups grp ON ggr.group_id = grp.id
        LEFT JOIN 
            gallery_languages gl ON g.id = gl.gallery_id
        LEFT JOIN 
            languages l ON gl.language_id = l.id
        LEFT JOIN 
            gallery_parodies gpar ON g.id = gpar.gallery_id
        LEFT JOIN 
            parodies p ON gpar.parody_id = p.id
        LEFT JOIN 
            gallery_categories gc ON g.id = gc.gallery_id
        LEFT JOIN 
            categories c ON gc.category_id = c.id
        LEFT JOIN 
            gallery_tags gt ON g.id = gt.gallery_id
        LEFT JOIN 
            tags t ON gt.tag_id = t.id
        WHERE 
            g.id = ?
        GROUP BY 
            g.id;
        """

        sauce = fetch_one(query_galleries_details, (sauceID,))
        if sauce is None:
            sauce = fetch_one(query_galleries, (sauceID,))
            if sauce is None:
                return jsonify({"error": "No sauce found with the given ID."}), 404

        if sauce is None:
            return jsonify({"error": "No sauce found with the given ID."}), 404

        sauce_dict = dict(sauce)
        sauce_dict["cover"] = url_for('image.get_cover_path', sauce_id=sauceID, _external=True)

        return jsonify(sauce_dict), 200

    except ValueError:
        return jsonify({"error": "The sauce id must be an integer."}), 400

    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


@general_bp.route('/api/sauce/<int:sauce_id>/images', methods=['GET'])
def get_sauce_images(sauce_id):
    # Logic to get all images of a sauce
    return jsonify({"message": f"Get images for sauce {sauce_id}"})

