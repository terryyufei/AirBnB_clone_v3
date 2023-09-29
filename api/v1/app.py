#!/usr/bin/python3
"""creating a flask application"""

from os import getenv
from flask import Flask
from models import storage
from api.v1.views import app_views


# Create a Flask application instance
app = Flask(__name__)

# Register the blueprint app_views
app.register_blueprint(app_views)


# Declare a method to handle teardown
@app.teardown_appcontext
def teardown(exception):
    """closes the current SQLAchemy session"""
    storage.close()


if __name__ == "__main__":
    HBNB_API_HOST = getenv('HBNB_API_HOST')
    HBNB_API_PORT = getenv('HBNB_API_PORT')
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT,
            threaded=True) 
