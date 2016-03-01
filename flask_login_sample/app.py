from flask import Flask
from flask_login_sample.bootstrap import init_data
from flask_login_sample.index import views as index_views
from flask_login_sample.users.auth import configure_login_manager


def create_app():
    """Create a Flask app."""

    init_data.init()

    flask_login_sample = Flask('flask_login_sample')
    flask_login_sample.secret_key = flask_login_sample.name
    flask_login_sample.register_blueprint(index_views.blueprint)

    configure_login_manager(flask_login_sample)

    return flask_login_sample
