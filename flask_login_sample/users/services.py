from flask_login_sample.util.db_util import connect, get, get_one, get_by_id, save

db = connect()
user_collection = db.users


def get_user_by_id(user_id):
    return get_by_id(user_collection, user_id)


def get_user_by_username(username):
    data_filter = {
        'username': username
    }
    return get_one(user_collection, data_filter)


def get_all_users():
    return get(user_collection, {})


def save_user(user):
    return save(user_collection, user)
