#!/usr/bin/python3
"""
add number route
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    return Hello HBNB!
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    return HBNB
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
    return C + text
    """
    text = text.replace('_', ' ')
    return 'C ' + text


@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """
    return python + text
    """
    text = text.replace('_', ' ')
    return 'Python ' + text


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    return number + int
    """
    if isinstance(n, int):
        return f'{n} is a number'
    else:
        return 'Not Found', 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
