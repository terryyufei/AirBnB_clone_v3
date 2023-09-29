#!/usr/bin/python3
"""creating a blueprint"""

from flask import Blueprint


# create a blueprint instance with a URL
app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")


from api.v1.views.index import *
