from flask.ext.login import UserMixin


class User(UserMixin):
    def __init__(self, name, email, username, password):
        self.id = username
        self.name = name
        self.email = email
        self.username = username
        self.password = password
