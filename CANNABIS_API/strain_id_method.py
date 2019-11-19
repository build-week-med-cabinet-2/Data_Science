"""
creating path to show the data
"""


from flask_restful import Resource
from flask import request


class Strain_Id(Resource):
    def get(self):
        return {'id': 'strain'}