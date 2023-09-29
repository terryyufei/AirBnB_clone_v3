#!/usr/bin/python3
"""creating a flask application"""

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
    from os import getenv
    
    # define host and port for flask server
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(getenv("HBNB_API_PORT", 5000))

    # Run flask server
    app.run(host=host, port=port, threaded=True)
