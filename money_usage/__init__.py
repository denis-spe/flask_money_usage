"""
Flask application factory.
"""

# Import libraries.
import json
from flask import Flask
from .models.model import db
from .blueprints.money_usage.views import mt_bp


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

    # Register the blueprints.
    app.register_blueprint(mt_bp)

    return app
