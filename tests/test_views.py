"""
Test blueprints views.
"""

from flask import Flask
import pytest
from money_usage import create_app
from config import TestConfig


@pytest.fixture()
def app():
    """
    Create test application.
    """
    # Initializer the created application.
    _app = create_app(test_config=TestConfig)
    yield _app


@pytest.fixture()
def client(app: Flask):
    """
    Create a test client.
    Args:
        app:(Flask) test flask application.
    """
    return app.test_client()


@pytest.fixture()
def runner(app: Flask):
    """
    Run the test client.
    Args:
        app:(Flask) test flask application.
    """
    return app.test_cli_runner()


def test_landing_page(client):
    """
    Test the landing page.
    """
    response = client.get("/money_usage")
    assert b"<h1>money usage</h1>" in response.data
