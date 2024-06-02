import sqlalchemy
from flask_login import UserMixin

from .db_session import SqlAlchemyBase


class City(SqlAlchemyBase, UserMixin):
    __tablename__ = 'cities'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(50), nullable=False)
