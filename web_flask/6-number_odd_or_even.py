#!/usr/bin/python3
"""
Module to initiate a flask app
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """
    Index route
    """

    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    hbnb route
    """

    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """
    Dynamic routing
    """
    text = text.replace("_", " ")
    return "C " + text


@app.route('/python/')
@app.route("/python/<text>", strict_slashes=False)
def python(text='is cool'):
    """
    Dynamic routing
    """
    if text:
        return "Python " + text.replace("_", " ")
    return "Python " + text


@app.route('/number/<int:number>')
def number(number):
    """
    Dynamic routing
    """
    return str(number) + " is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Dynamic routing and template rendering
    """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Dynamic routing and template rendering
    """
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == "__main__":
    app.run(debug=True)
