# -*- coding: utf-8 -*-
from app import create_app
from flask_script import Manager

app = create_app('default')
manager = Manager(app)


@manager.command
def test():
    """Run the unit tests."""
    pass


if __name__ == '__main__':
    manager.run()




# from flask import Flask
# app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return 'hello world'

# if __name__ == '__main__':
#     app.run(host='0.0.0.0',port=5000,debug=True)
