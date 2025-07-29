# app/browsing_section.py
from flask import Blueprint, jsonify
from .database import fetch_all, fetch_one

browsing_bp = Blueprint('browsing', __name__)

@browsing_bp.route('/api/tags', methods=['GET'])
def get_all_tags():
    try:

        query_tags = """
            SELECT t.name, COUNT(t.id) AS tag_count
            FROM tags t
            JOIN gallery_tags gt ON t.id = gt.tag_id 
            JOIN galleries g ON gt.gallery_id = g.id
            GROUP BY t.name;
        """

        tags = fetch_all(query_tags)
        if tags is None:
            return jsonify({"error": "No tags found."}), 404

        tags_dict = dict(tags)

        return jsonify(tags_dict), 200

    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

@browsing_bp.route('/api/artists', methods=['GET'])
def get_all_artists():
    try:

        query_artists = """
            SELECT a.name, COUNT(a.id) AS artist_count
            FROM artists a
            JOIN gallery_artists ga ON a.id = ga.artist_id 
            JOIN galleries g ON ga.gallery_id  = g.id
            GROUP BY a.name;
        """

        artists = fetch_all(query_artists)
        if artists is None:
            return jsonify({"error": "No artists found."}), 404

        artists_dict = dict(artists)

        return jsonify(artists_dict), 200

    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

@browsing_bp.route('/api/characters', methods=['GET'])
def get_all_characters():
    # Logic to get all characters with pagination
    return jsonify({"message": "Get all characters with pagination"})

@browsing_bp.route('/api/parodies', methods=['GET'])
def get_all_parodies():
    try:

        query_parodies = """
            SELECT p.name, COUNT(p.id ) AS parodie_count
            FROM parodies p 
            JOIN gallery_parodies gp ON p.id = gp.parody_id 
            JOIN galleries g ON gp.gallery_id = g.id
            GROUP BY p.name;
        """

        parodies = fetch_all(query_parodies)
        if parodies is None:
            return jsonify({"error": "No parodies found."}), 404

        parodies_dict = dict(parodies)

        return jsonify(parodies_dict), 200

    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

@browsing_bp.route('/api/groups', methods=['GET'])
def get_all_groups():
    try:

        query_groups = """
            SELECT g.name, COUNT(g.id ) AS group_count
            FROM groups g 
            JOIN gallery_groups gg ON g.id = gg.group_id 
            JOIN galleries ON gg.gallery_id = galleries.id 
            GROUP BY g.name;
        """

        groups = fetch_all(query_groups)
        if groups is None:
            return jsonify({"error": "No groups found."}), 404

        groups_dict = dict(groups)

        return jsonify(groups_dict), 200

    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500