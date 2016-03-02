from datetime import timedelta


class FlaskConfig(object):
    SECRET_KEY = 'flask_jwt_sample'


class JWTConfig(object):
    JWT_AUTH_URL_RULE = '/login'
    JWT_EXPIRATION_DELTA = timedelta(seconds=300)
