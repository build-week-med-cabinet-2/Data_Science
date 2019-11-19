"""
Testing out restful to display json from different files
"""


from flask_restful import Resource
from flask import request
import pandas as pd


class HelloWorld(Resource):
    def get(self):
        return {'about': 'Hello API!'}

    def post(self):
        some_json = request.get_json()
        return {'you sent': some_json}, 201
