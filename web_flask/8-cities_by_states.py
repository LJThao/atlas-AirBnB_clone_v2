#!/usr/bin/python3
"""Starts a Flask web app for routes cities
by states list"""


from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


web_app = Flask(__name__)


@web_app.teardown_appcontext
def remove_session(exception):
    storage.close()


@web_app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Route handler function that requests cities_by_states list"""
    # Fetching all states objects
    states = storage.all(State).values()
    states_sorted = sorted(states, key=lambda state: state.name)
    # Rendering HTML template 
    return render_template('8-cities_by_states.html', states=states_sorted)


if __name__ == '__main__':
    web_app.run(host='0.0.0.0', port=5000)
