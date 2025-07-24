# app/language_change.py
from flask import Blueprint, request, jsonify

language_bp = Blueprint('language', __name__)

@language_bp.route('/api/language', methods=['POST'])
def change_language():
    data = request.get_json()
    new_language = data.get('language')
    # Logic to change the language of the website
    return jsonify({"message": f"Language changed to {new_language}"})
