from flask import Blueprint
from flask_jwt import jwt_required, current_identity

blueprint = Blueprint('index', __name__)


@blueprint.route('/')
def index():
    return 'Hello World!', 200


@blueprint.route('/protected')
@jwt_required()
def protected():
    return 'Hello Protected World!\n%s' % current_identity['name'], 200
