"""
Build my app factory and do routes and configuration
"""

from flask import Flask, request
from dotenv import load_dotenv
from .hello_test import HelloWorld
from flask_restful import Api
load_dotenv()


def create_app():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(HelloWorld, '/')

    return app