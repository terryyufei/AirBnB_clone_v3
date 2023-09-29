#!/usr/bin/python3

from flask import jsonify
from api.v1.views import app_views


# define a route on the app_views blueprint
@app_views.route('/status', methods=['GET'], strict_slashes=False)
def get_status():
    """checks the status and returns a JSON response"""
    return jsonify({'status': 'OK'})
