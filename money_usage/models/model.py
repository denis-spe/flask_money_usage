"""
Application models.
"""

# Import libraries.
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, MappedColumn, DeclarativeBase
from sqlalchemy.types import String


class Base(DeclarativeBase):
    pass


# Initializer the SQLAlchemy
db = SQLAlchemy(model_class=Base)


class Users(db.Model):
    userId: Mapped[int] = MappedColumn(primary_key=True)
    first_name: Mapped[str] = MappedColumn(String(255))
    last_name: Mapped[str] = MappedColumn(String(255))
    password: Mapped[str] = MappedColumn(String(8))
    email: Mapped[str] = MappedColumn(String(255))
