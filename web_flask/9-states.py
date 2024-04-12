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


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_list(id=None):
    """
    dynamic routing
    """
    valid_id = False
    data = [value for value in storage.all(State).values()]
    if id in [state.to_dict()['id'] for state in data]:
        valid_id = True
    return render_template('9-states.html', data=data,
                           id=id, valid_id=valid_id)


if __name__ == '__main__':
    app.run(debug=False)
