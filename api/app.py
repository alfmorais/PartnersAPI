import os

from api.database import database
from api.errors.messages import (
    JWT_EXPIRED_TOKEN_CALLBACK,
    JWT_INVALID_TOKEN_CALLBACK,
    JWT_MISSING_TOKEN_CALLBACK,
    JWT_REVOKED_TOKEN_CALLBACK,
    JWT_TOKEN_NOT_FRESH_CALLBACK
)
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_smorest import Api


PROPAGATE_EXCEPTIONS = os.environ["PROPAGATE_EXCEPTIONS"]
API_TITLE = os.environ["API_TITLE"]
API_VERSION = os.environ["API_VERSION"]
OPENAPI_VERSION = os.environ["OPENAPI_VERSION"]
OPENAPI_URL_PREFIX = os.environ["OPENAPI_URL_PREFIX"]
OPENAPI_SWAGGER_UI_PATH = os.environ["OPENAPI_SWAGGER_UI_PATH"]
OPENAPI_SWAGGER_UI_URL = os.environ["OPENAPI_SWAGGER_UI_URL"]
SQLALCHEMY_DATABASE_URI = os.environ["SQLALCHEMY_DATABASE_URI"]
SQLALCHEMY_TRACK_MODIFICATIONS = os.environ["SQLALCHEMY_TRACK_MODIFICATIONS"]
JWT_SECRETY_KEY = os.environ["JWT_SECRETY_KEY"]


def create_app(db_url=None):
    app = Flask(__name__)
    app.config["PROPAGATE_EXCEPTIONS"] = PROPAGATE_EXCEPTIONS
    app.config["API_TITLE"] = API_TITLE
    app.config["API_VERSION"] = API_VERSION
    app.config["OPENAPI_VERSION"] = OPENAPI_VERSION
    app.config["OPENAPI_URL_PREFIX"] = OPENAPI_URL_PREFIX
    app.config["OPENAPI_SWAGGER_UI_PATH"] = OPENAPI_SWAGGER_UI_PATH
    app.config["OPENAPI_SWAGGER_UI_URL"] = OPENAPI_SWAGGER_UI_URL
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS
    app.config["JWT_SECRETY_KEY"] = JWT_SECRETY_KEY

    database.init_app(app=app)
    migrate = Migrate(app=app, db=database)

    api = Api(app=app)
    jwt = JWTManager(app=app)

    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return (jsonify(JWT_REVOKED_TOKEN_CALLBACK), 401)

    @jwt.needs_fresh_token_loader
    def token_not_fresh_callback(jwt_header, jwt_payload):
        return (jsonify(JWT_TOKEN_NOT_FRESH_CALLBACK), 401)

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (jsonify(JWT_EXPIRED_TOKEN_CALLBACK), 401)

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (jsonify(JWT_INVALID_TOKEN_CALLBACK), 401)

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (jsonify(JWT_MISSING_TOKEN_CALLBACK), 401)

    return app