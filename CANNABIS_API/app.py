"""
Build my app factory and do routes and configuration
"""

from decouple import config
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from .predict import predict_strain
from .models import DB, Records
load_dotenv()


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    DB.init_app(app)

    @app.route('/<int:strain_id>', methods=['POST'])
    def predict_strain(strain_id=strain_id):
        strain = request.values['strain_id']
        predictions = predict_strain(strain)
        return jsonify



    return app