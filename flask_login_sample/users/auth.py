from flask.ext.login import LoginManager, login_user
from flask_login_sample.users import services
from flask_login_sample.users.models import User


def configure_login_manager(app):
    login_manager = LoginManager()
    login_manager.session_protection = 'strong'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(username):
        user_entry = services.get_user_by_username(username)
        if user_entry:
            name = user_entry['name']
            email = user_entry['email']
            password = user_entry['password']

            return User(name, email, username, password)
        return None

    @login_manager.request_loader
    def load_user_from_request(request):
        token = request.headers.get('Authorization')
        if token is None:
            token = request.args.get('token')

        if token:
            username, password = token.split(':')
            user_entry = services.get_user_by_username(username)
            if user_entry:
                user = User(user_entry['name'], user_entry['email'], user_entry['username'], user_entry['password'])
                if user.password == password:
                    login_user(user)
                    return user

        return None
