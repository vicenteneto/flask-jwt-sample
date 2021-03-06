from flask import Flask
from flask_jwt_sample.auth import configure_jwt
from flask_jwt_sample.bootstrap import init_data
from flask_jwt_sample.index import views as index_views


def create_app():
    init_data.init()

    flask_login_sample = Flask('flask_jwt_sample')

    flask_login_sample.config.from_object('flask_jwt_sample.settings.FlaskConfig')
    flask_login_sample.config.from_object('flask_jwt_sample.settings.JWTConfig')

    flask_login_sample.register_blueprint(index_views.blueprint)

    configure_jwt(flask_login_sample)

    return flask_login_sample
