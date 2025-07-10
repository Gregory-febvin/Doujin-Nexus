# app/general_endpoints.py
from flask import Blueprint, jsonify, request
from .database import fetch_all

general_bp = Blueprint('general', __name__)

@general_bp.route('/api/sauces', methods=['GET'])
def get_all_sauces():
    page = request.args['page']
    limit = request.args['limit']
    
    offset = (int(page) - 1) * int(limit)
    query = "SELECT title FROM galleries LIMIT ? OFFSET ?"
    sauces = fetch_all(query, (limit, offset))

    return jsonify([dict(sauce) for sauce in sauces])

@general_bp.route('/api/sauces/<int:sauce_id>', methods=['GET'])
def get_specific_sauce(sauce_id):
    
    return jsonify({"message": f"Get info for sauce {sauce_id}"})

@general_bp.route('/api/sauces/<int:sauce_id>/images', methods=['GET'])
def get_sauce_images(sauce_id):
    # Logic to get all images of a sauce
    return jsonify({"message": f"Get images for sauce {sauce_id}"})

