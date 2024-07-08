#!/usr/bin/python3
"""Starts a Flask web app for routes states list"""


from flask import Flask, render_template
from models import storage
from models.state import State


web_app = Flask(__name__)


@web_app.teardown_appcontext
def remove_session(exception):
    storage.close()


@web_app.route('/states_list', strict_slashes=False)
def states_list():
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    web_app.run(host='0.0.0.0', port=5000)
