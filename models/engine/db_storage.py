#!/usr/bin/python3
"""DBStorage class for AirBnB"""
from os import getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, scoped_session, relationship


class DBStorage:
    """DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initial method"""
        mysql_user = getenv('HBNB_MYSQL_USER')
        mysql_pwd = getenv('HBNB_MYSQL_PWD')
        mysql_host = getenv('HBNB_MYSQL_HOST')
        mysql_db = getenv('HBNB_MYSQL_DB')
        mysql_env = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            mysql_user, mysql_pwd, mysql_host, mysql_db), pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        if mysql_env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """show all data."""
        elem_dict = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls).all()
            for data in query:
                key = "{}.{}".format(type(data).__name__, data.id)
                elem_dict[key] = data
        else:
            list_cls = [State, City, User, Place, Review, Amenity]
            for clas in list_cls:
                query = self.__session.query(clas)
                for data in query:
                    key = "{}.{}".format(type(data).__name__, data.id)
                    elem_dict[key] = data
        return elem_dict

    def new(self, obj):
        """Add the object in the databse"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commit all changes of the current
        database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database"""
        if obj:
            self.__session.delete(obj)

    def close(self):
        """Closes Session"""
        self.__session.close()

    def reload(self):
        """Create database in Alchemy"""
        Base.metadata.create_all(self.__engine)
        db_fac = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(db_fac)
        self.__session = Session()

    def close(self):
        """Clise session"""
        self.__session.close()
