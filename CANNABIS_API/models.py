"""
These are my database models
"""

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


DB = SQLAlchemy()

class Records(DB.Model):
    id = DB.Column(DB.BigInteger, primary_key=True)

    def __repr__(self):
        return '<id is {}>'.format(self.id)
