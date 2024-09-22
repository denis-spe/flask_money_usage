"""
Money usage blueprints views.
"""

# Import libraries
from flask import render_template, Blueprint

# Instantiate the money usage blueprint.
mt_bp = Blueprint("money_usage", __name__, template_folder="templates/money_usage")

# Create views


@mt_bp.route("/money_usage")
def index():
    return "<h1>money usage</h1>"
