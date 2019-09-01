#!/usr/bin/python3
"""Creates a database engine
   to creates, manipulates, query relational tables
"""
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from datetime import datetime
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage():
    """database class"""
    __engine = None
    __session = None

    def __init__(self):
        """constructor of the database instance"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        self.all_type = {
            "State": State,
            "City": City,
            "User": User,
            "Place": Place,
            "Amenity": Amenity,
            "Review": Review
            }

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def reload(self):
        """reloads the database"""

        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(bind=self.__engine,
                                      expire_on_commit=False)
        Session = scoped_session(self.__session)
        self.__session = Session()

    def all(self, cls=None):
        """query database by cls type
            return a dictionary
        """
        my_dic = {}
        if cls is None:
            for cls in self.all_type.values():
                if self.__session.query(cls).all():
                    for item in self.__session.query(cls).all():
                        my_dic[item.id] = item
        else:
            for item in self.__session.query(self.all_type[cls]).all():
                my_dic[item.id] = item
        return my_dic

    def new(self, obj):
        """add a new obj to table
        database session self.__session
        """
        if not obj:
            return
        self.__session.add(obj)

    def save(self):
        """commit all change to table"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes the obj from table"""
        if obj:
            self.__session.delete(obj)
            self.save()

    def close(self):
        """to close the session"""
        self.__session.close()
