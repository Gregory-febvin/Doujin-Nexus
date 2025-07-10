# app/general_endpoints.py
from flask import Blueprint, jsonify, request, url_for
from werkzeug.exceptions import BadRequest, InternalServerError

from .database import fetch_all
from .image_handle import get_image_path

general_bp = Blueprint('general', __name__)

@general_bp.route('/api/sauces', methods=['GET'])
def get_all_sauces():
    try:
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 10))
        if page <= 0 or limit <= 0:
            raise BadRequest("Page and limit must be positive integers.")
        offset = (page - 1) * limit

        query = "SELECT id, title FROM galleries LIMIT ? OFFSET ?"
        sauces = fetch_all(query, (limit, offset))

        result = []
        for sauce in sauces:
            sauce_dict = dict(sauce)
            sauce_id = sauce_dict.get("id")
            sauce_dict["cover"] = url_for('image.serve_image', sauce_id=sauce_id, _external=True)
            result.append(sauce_dict)

        return jsonify(result), 200

    except ValueError:
        raise BadRequest("Page and limit must be integers.")

    except KeyError as e:
        raise BadRequest(f"Missing required query parameter: {str(e)}")

    except Exception as e:
        raise InternalServerError(f"An unexpected error occurred: {str(e)}")


@general_bp.route('/api/sauces/<int:sauce_id>', methods=['GET'])
def get_specific_sauce(sauce_id):
    
    return jsonify({"message": f"Get info for sauce {sauce_id}"})

@general_bp.route('/api/sauces/<int:sauce_id>/images', methods=['GET'])
def get_sauce_images(sauce_id):
    # Logic to get all images of a sauce
    return jsonify({"message": f"Get images for sauce {sauce_id}"})

