"""
These are my database models
"""

from flask_sqlalchemy import SQLAlchemy


DB = SQLAlchemy()

class Records(DB.Model):
    strain_id = DB.Column(DB.BigInteger, primary_key=True)

    def __repr__(self):
        return '<Strain id is {}>'.format(self.strain_id)
