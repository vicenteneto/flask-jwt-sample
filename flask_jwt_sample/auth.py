from flask_jwt import JWT
from flask_jwt_sample.users import services
from flask_jwt_sample.users.models import User
from werkzeug.security import safe_str_cmp


def authenticate(username, password):
    user = services.get_user_by_username(username)
    if user and safe_str_cmp(user['password'].encode('utf-8'), password.encode('utf-8')):
        return User(user['name'], user['email'], user['username'], user['password'])


def identify(payload):
    user_id = payload['identity']
    return services.get_user_by_username(user_id)


def configure_jwt(flask_app):
    JWT(flask_app, authenticate, identify)
