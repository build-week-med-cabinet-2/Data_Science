"""
Build my app factory and do routes and configuration
"""

from decouple import config
from flask import Flask, request
from dotenv import load_dotenv
from .strain_id_method import Strain_Id
from .models import DB, Records
from flask_restful import Api
load_dotenv()


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    DB.init_app(app)

    api = Api(app)

    api.add_resource(Strain_Id, '/')

    return app