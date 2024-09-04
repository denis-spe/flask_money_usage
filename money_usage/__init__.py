"""
Flask application factory.
"""
# Import libraries.
import json
from flask import Flask
from money_usage.models.model import db


def create_app(test_config=None) -> Flask:
    """
    Create the flask application factory.
    Args:
        test_config: Test configuration.
    Return: Flask object.
    """
    # Instantiate the Flask instance.
    app = Flask(__name__)

    # Application configuration settings.
    if test_config:
        app.config.from_object(test_config)
    else:
        app.config.from_file("../config.json", load=json.load)

    # Initializer the databases.
    db.init_app(app)

    # Create tables.
    with app.app_context():
        db.create_all()

    return app
