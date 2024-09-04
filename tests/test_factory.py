"""
Flask application factory testing.
"""
# Import Libraries.
from money_usage import create_app
from config import TestConfig


def test_factory():
    assert not create_app().testing
    assert create_app(test_config=TestConfig).testing
