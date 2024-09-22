""" 
Test database.
"""

# Import libraries.
import pytest
from money_usage import create_app
from config import TestConfig
from money_usage.models.model import db, Users
from sqlalchemy import Select


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
    user.email = "denisbrian07@gmail.com"

    db.session.add(user)
    db.session.commit()

    # Get the first user with userId = 1
    user1 = db.get_or_404(Users, 1)
    assert user1.first_name == "Mutesasira"

    # Filter by last name of the users
    filter_user = Select(Users).filter_by(userId=1)
    get_one_user = db.one_or_404(filter_user, description="Unknown user.")
    assert get_one_user.last_name == "Denis"

    # Delete the database.
    db.session.delete(user)

    # commit the changes
    # db.session.commit()
