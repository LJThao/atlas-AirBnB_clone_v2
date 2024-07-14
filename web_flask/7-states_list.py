#!/usr/bin/python3
"""Starts a Flask web app for routes states list"""


from flask import Flask, render_template
from models import storage
from models.state import State


web_app = Flask(__name__)


@web_app.teardown_appcontext
def remove_session(exception):
    """Ensure all open connections are closed"""
    storage.close()


@web_app.route('/states_list', strict_slashes=False)
def states_list():
    """Route handler function that requests states_list"""
    # Retrieving all state objects from storage and extracts
    states = storage.all(State).values()
    # Sort all state objects
    states_sorted = sorted(states, key=lambda state: state.name)
    # Render HTML template by passing dynamic data
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    web_app.run(host='0.0.0.0', port=5000)
