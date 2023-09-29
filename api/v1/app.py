#!/usr/bin/python3
"""creating a flask application"""

import os
from flask import Flask
from models import storage
from api.v1.views import app_views


# Create a Flask application instance
app = Flask(__name__)

# Register the blueprint app_views
app.register_blueprint(app_views)


# Declare a method to handle teardown
@app.teardown_appcontext
def teardown(error):
    """closes the current SQLAchemy session"""
    storage.close()


if __name__ == "__main__":
    port = int(os.getenv("HBNB_API_HOST", 5000))
    host = os.getenv("HBNB_API_PORT", "0.0.0.0")
    app.run(host=host, port=port, threaded=True)
