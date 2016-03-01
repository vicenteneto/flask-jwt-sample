from flask_login_sample.users import services


def user_1():
    return {
        'name': 'Usuario 1',
        'username': 'user1',
        'email': 'user1@email.com',
        'password': 'user1'
    }


def user_2():
    return {
        'name': 'Usuario 2',
        'username': 'user2',
        'email': 'user2@email.com',
        'password': 'user2'
    }


def init():
    """
    Populate database mongo with initial data.
    """
    if services.get_all_users().count() == 0:
        services.save_user(user_1())
        services.save_user(user_2())
