#!/usr/bin/python3
"""Starts a Flask web app for routes states
by states list"""


from flask import Flask, render_template
from models import storage
from models.state import State


web_app = Flask(__name__)


@web_app.teardown_appcontext
def remove_session(exception):
    storage.close()


web_app.route('/states', strict_slashes=False)
def states_list():
    """Route handler function that requests states list"""
    # Retrieve states in database and extract value
    states = storage.all(State).values()
    # sort all states by name
    states_sorted = sorted(states, key=lambda state: state.name)
    # render the template with sorted states
    return render_template('9-states.html', states=states_sorted)


@web_app.route('/states/<id>', strict_slashes=False)
def states_cities(id):
    """Route handler function that requests states, cities, id list"""
    # Retrieve state from database by id
    state = storage.get("State", id)
    # if the state object exists(True), then
    if state:
        # sort all cities name with the state
        cities = sorted(state.cities, key=lambda city: city.name)
        # render the template with the state and cities sorted
        return render_template('9-states.html', state=state, cities=cities)
    # if false then
    else:
        # render the template saying state is not found
        return render_template('9-states.html', state_not_found=True)


if __name__ == '__main__':
    web_app.run(host='0.0.0.0', port=5000)
