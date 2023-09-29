#!/usr/bin/python3
"""Returns a Json response"""

from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status', methods=['GET'])
def get_status():
    """Checks and returns status"""
    response = {"status": "OK"}
    return jsonify(response)

@app_views.route('/stats', methods=['GET'])
def object_stats():
    """Retrieves the no of each object by type"""
    objects = {
            "amenities": storage.count('Amenity'),
            "cities": storage.count('City'),
            "places": storage.count('Place'),
            "reviews": storage.count('Review'),
            "states": storage.count('State'),
            "users": storage.count('User'),
            }
    return jsonify(objects)
