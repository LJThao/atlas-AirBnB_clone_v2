#!/usr/bin/python3
"""Starts a Flask web app to display HBNB filters"""


from flask import Flask, render_template
from models import storage
from models import *


web_app = Flask(__name__)


@web_app.teardown_appcontext
def remove_session(exception):
    storage.close()


@web_app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Route handler function that requests hbnb filter list"""
    # sort states, cities, amenities
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    # render a template with sorted objects
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


if __name__ == '__main__':
    web_app.run(host='0.0.0.0', port=5000)
