"""
These are my database models
"""

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


DB = SQLAlchemy()

class Records(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    strain = DB.Column(DB.String(25))
    strain_type = DB.Column(DB.String(6))
    rating = DB.Column(DB.Float)
    effects = DB.Column(DB.String(100))
    flavor = DB.Column(DB.String(100))
    description = DB.Column(DB.String(2000))

    def __repr__(self):
        return '<Strain {}>'.format(self.strain)
