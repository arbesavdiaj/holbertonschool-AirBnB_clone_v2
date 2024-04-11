#!/usr/bin/python3
"""
Module to initiate a flask app
"""


from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Index route
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    HBNB route
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """
    Dynamic routing
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is cool'):
    """
    Dynamic routing
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """
    Dynamic routing
    """
    return str(n) + ' is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Dynamic routing and template rendering
    """
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
