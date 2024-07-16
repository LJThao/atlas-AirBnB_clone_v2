#!/usr/bin/python3
"""Starts a Flask web app for routes states
by states list"""


from flask import Flask, render_template
from models import storage
from models import * 


web_app = Flask(__name__)


@web_app.teardown_appcontext
def remove_session(exception):
    storage.close()


@web_app.route('/states', strict_slashes=False)
@web_app.route('/states/<id>', strict_slashes=False)
def states_list(state_id=None):
    """Route handler function that requests states list"""
    states = storage.all("State")
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)


if __name__ == '__main__':
    web_app.run(host='0.0.0.0', port=5000)
