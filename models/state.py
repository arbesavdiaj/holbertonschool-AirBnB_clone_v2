#!/usr/bin/python3
"""State class definitiont"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """This is the class for State"""
    __tablename__ = "states"
        
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete", backref="state")
    else:
        name = ""

        if storage_type != 'db':

            @property
            def cities(self):
                """ Returns the list of City"""
                cities = []
                for city in models.storage.all(City).values():
                    if city.state_id == self.id:
                        cities.append(city)
                return cities
