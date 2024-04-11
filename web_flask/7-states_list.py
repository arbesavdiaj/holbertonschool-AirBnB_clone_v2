#!/usr/bin/python3
"""
Creating an app
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """
    Simple function
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    dynamic routing
    """
    all_states = storage.all(State)
    return render_template('7-states_list.html', all_states=all_states)


if __name__ == '__main__':
    app.run(debug=False)
