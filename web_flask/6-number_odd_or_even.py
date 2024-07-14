#!/usr/bin/python3
"""Starts a Flask web application with routes
/number_odd_or_even/<n> to display a HTML"""


from flask import Flask, render_template
web_app = Flask(__name__)


@web_app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@web_app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@web_app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    return f"C {text.replace('_', ' ')}"


@web_app.route('/python/', strict_slashes=False)
@web_app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text="is cool"):
    return f"Python {text.replace('_', ' ')}"


@web_app.route('/number/<int:n>', strict_slashes=False)
def is_it_a_num(n):
    return f"{n} is a number"


@web_app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', n=n)


@web_app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even(n):
    odd_or_even = "even" if n % 2 == 0 else "odd"
    return render_template('6-number_odd_or_even.html', n=n,
                           odd_or_even=odd_or_even)


if __name__ == "__main__":
    web_app.run(host="0.0.0.0", port=5000)
