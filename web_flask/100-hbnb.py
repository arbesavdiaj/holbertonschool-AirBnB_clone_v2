#!/usr/bin/python3
"""
Creating an app
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.user import User


app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """
    Simple function
    """
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    dynamic routing
    """
    states = [value for value in storage.all(State).values()]
    amenities = [amenity.to_dict()['name'] for amenity in
                 storage.all(Amenity).values()]
    places = [place.to_dict() for place in storage.all(Place).values()]
    users = [user.to_dict() for user in storage.all(User).values()]
    for place in places:
        for user in users:
            if user['id'] == place['user_id']:
                place['owner'] = f"{user['first_name']} {user['last_name']}"
    
    return render_template('100-hbnb.html',
                           states=states, amenities=amenities, places=places)


if __name__ == '__main__':
    app.run(debug=False)
