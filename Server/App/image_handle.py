# app/general_endpoints.py
import os
from flask import Blueprint, jsonify, request, send_file, Response, url_for
from werkzeug.exceptions import BadRequest, InternalServerError

IMAGE_PATH = os.path.join(os.path.dirname(__file__), '../Image')
DEFAULT_IMAGE_PATH = os.path.join(IMAGE_PATH, 'default.jpg')

image_bp = Blueprint('image', __name__)

def get_image_path(sauce_id, page_number):
    """Construct the image path and check if it exists."""
    image_path = os.path.join(IMAGE_PATH, str(sauce_id), f'{page_number}.jpg')
    return image_path if os.path.exists(image_path) else DEFAULT_IMAGE_PATH

def build_image_urls(sauce_id, max_pages=30):
    """ Return path of all the image for a sauce"""
    image_links = []
    for page in range(1, max_pages + 1):
        image_path = get_image_path(sauce_id, page)
        if os.path.exists(image_path):
            image_url = url_for('image.serve_image', sauce_id=sauce_id, pageNumber=page, _external=True)
            image_links.append(image_url)
    return image_links

def handle_image_response(image_path):
    """Send the image file or the default image if not found."""
    if os.path.exists(image_path):
        return send_file(image_path, mimetype='image/jpeg')
    else:
        return Response("Image not found", status=404, mimetype='text/plain')

@image_bp.route('/image/cover/<int:sauce_id>', methods=['GET'])
def get_cover_path(sauce_id):
    """Get the cover image for a specific sauce."""
    try:
        image_path = os.path.join(IMAGE_PATH, str(sauce_id), '1.jpg')

        if os.path.exists(image_path):
            return handle_image_response(image_path)
        else: 
            return handle_image_response(DEFAULT_IMAGE_PATH)
            
    except Exception as e:
        return InternalServerError(f"An unexpected error occurred: {str(e)}")

@image_bp.route('/image/<int:sauce_id>', methods=['GET'])
def get_all_image(sauce_id):
    """Get all image URLs for a specific sauce."""
    pages = int(request.args.get('pages', 1))

    if sauce_id <= 0 or pages <= 0:
        return BadRequest("Invalid parameters.")

    try:
        image_links = build_image_urls(sauce_id, pages)
        if image_links:
            return jsonify(image_links), 200
        else:
            return Response("No images found", status=404, mimetype='text/plain')
    except Exception as e:
        raise InternalServerError(f"An unexpected error occurred: {str(e)}")

@image_bp.route('/image/<int:sauce_id>/<int:pageNumber>', methods=['GET'])
def serve_image(sauce_id, pageNumber):
    """Serve a specific image for a given sauce and page number."""
    try:
        image_path = get_image_path(sauce_id, pageNumber)
        return handle_image_response(image_path)
    except Exception as e:
        return InternalServerError(f"An unexpected error occurred: {str(e)}")
