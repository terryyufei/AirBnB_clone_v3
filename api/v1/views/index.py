#!/usr/bin/python3
"""Returns a Json response"""

from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def get_status():
    """Checks and returns status"""
    response = {"status": "OK"}
    return jsonify(response)
