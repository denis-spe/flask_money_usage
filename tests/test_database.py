"""
Test database.
"""

# Import libraries.
import pytest
from money_usage import create_app
from config import TestConfig
from money_usage.models.model import db, Users


@pytest.fixture()
def app():
    _app = create_app(test_config=TestConfig)
    yield _app


@pytest.fixture()
def app_ctx(app):
    with app.app_context():
        yield


@pytest.mark.usefixtures("app_ctx")
def test_adding_user():
    user = Users()
    user.first_name = "Mutesasira"
    user.last_name = "Denis"
    user.password = "jetaudio"
    user.email = "drnisbrian07@gmai.com"

    db.session.add(user)
    db.session.commit()
