#!/usr/bin/python3
"""Starts a Flask web app to display HBNB filters"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity


web_app = Flask(__name__)


@web_app.teardown_appcontext
def remove_session(exception):
    storage.close()


@web_app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Route handler function that requests hbnb filter list"""
    # sort states, cities, amenities
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    cities = sorted(storage.all(City).values(), key=lambda city: city.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda amenity: amenity.name)
    # render a template with sorted objects
    return render_template('10-hbnb_filters.html', states=states, cities=cities, amenities=amenities)


if __name__ == '__main__':
    web_app.run(host='0.0.0.0', port=5000)
