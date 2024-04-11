#!/usr/bin/python3
"""
Module to initiate a flask
"""
from flask import Flask, render_template
from models import storage, State

app = Flask(__name__)


@app.teardown_appcontext
def close_all(error):
    """
    func to remove sqlalchemy session
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    States display
    """
    states = [state.to_dict() for state in storage.all(State).values()]
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(debug=False)
