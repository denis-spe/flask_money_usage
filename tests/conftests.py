"""
Test application configuration.
"""

# Import libraries.
import pytest
from money_usage import create_app
from tests.config import TestConfig
from flask import Flask


@pytest.fixture()
def app():
    """
    Create a test application.
    """
    _app = create_app(
        test_config=TestConfig
    )

    yield _app


@pytest.fixture()
def client(_app: Flask):
    """
    Create a client.
    """
    return _app.test_client()


@pytest.fixture()
def runner(_app: Flask):
    """
    Runner the client test.
    """
    return _app.test_cli_runner()


@pytest.fixture()
def app_ctx(_app: Flask):
    """
    Create the application context for database.
    """
    with _app.app_context():
        yield
