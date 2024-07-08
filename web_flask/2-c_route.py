#!/usr/bin/python3
"""Starts a Flask web application with routes
/c/<text>/hbnb to display C"""


from flask import Flask
web_app = Flask(__name__)


@web_app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

@web_app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

@web_app.route('/c/<text>', strict_slashes=False)
def c_is_fun():
    return f"C {text.replace('_', ' ')}"


if __name__ == "__main__":
    web_app.run(host="0.0.0.0", port=5000)
