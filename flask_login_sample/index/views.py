from flask import Blueprint
from flask.ext.login import current_user, login_required, logout_user

blueprint = Blueprint('index', __name__)


@blueprint.route('/')
def index():
    return 'Hello World!', 200


@blueprint.route('/protected')
@login_required
def protected():
    return 'Hello Protected World!\n%s' % current_user.name, 200


@blueprint.route("/logout")
@login_required
def logout():
    logout_user()
    return 'User logged off successfully!', 200
