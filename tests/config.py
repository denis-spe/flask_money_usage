"""
Test configuration.
"""


class TestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = ("mysql://root:ILoveGod@localhost/"
                               "test_flask_money_usage")
    SECRET_KEY = "HSJJJFFattw7ut2815627275251gwgs6w"
