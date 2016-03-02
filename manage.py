#!/usr/bin/env python
from flask.ext.script import Manager

from flask_jwt_sample.app import create_app

manager = Manager(create_app)

if __name__ == '__main__':
    manager.run()
