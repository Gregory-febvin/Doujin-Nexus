# app/general_endpoints.py
import os
from flask import Blueprint, jsonify, request, send_file, Response
from werkzeug.exceptions import BadRequest, InternalServerError

IMAGE_PATH = os.path.join(os.path.dirname(__file__), '../Image')
DEFAULT_IMAGE_PATH = os.path.join(IMAGE_PATH, 'default.jpg')

image_bp = Blueprint('image', __name__)

def get_image_path(sauce_id):
    path = os.path.join(IMAGE_PATH, str(sauce_id), '1.jpg')
    return path if os.path.exists(path) else DEFAULT_IMAGE_PATH

@image_bp.route('/images/<int:sauce_id>', methods=['GET'])
def serve_image(sauce_id):
    try:
        image_path = get_image_path(sauce_id)
        return send_file(image_path, mimetype='image/jpeg')
    except Exception:
        return Response("Image not found", status=404, mimetype='text/plain')
