# app/browsing_section.py
from flask import Blueprint, jsonify

browsing_bp = Blueprint('browsing', __name__)

@browsing_bp.route('/api/tags', methods=['GET'])
def get_all_tags():
    # Logic to get all tags with pagination
    return jsonify({"message": "Get all tags with pagination"})

@browsing_bp.route('/api/artists', methods=['GET'])
def get_all_artists():
    # Logic to get all artists with pagination
    return jsonify({"message": "Get all artists with pagination"})

@browsing_bp.route('/api/categories', methods=['GET'])
def get_all_categories():
    # Logic to get all categories with pagination
    return jsonify({"message": "Get all categories with pagination"})

@browsing_bp.route('/api/parodies', methods=['GET'])
def get_all_parodies():
    # Logic to get all parodies with pagination
    return jsonify({"message": "Get all parodies with pagination"})
