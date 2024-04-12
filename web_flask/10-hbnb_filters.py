#!/usr/bin/python3
"""
Creating an app
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """
    Simple function
    """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
    dynamic routing
    """
    data = [value for value in storage.all(State).values()]
    amenities = [amenity.to_dict()['name'] for amenity in
                 storage.all(Amenity).values()]
    return render_template('10-hbnb_filters.html',
                           data=data, amenities=amenities)


if __name__ == '__main__':
    app.run(debug=False)
