#!/usr/bin/python3
"""This is the user class"""
from models.base_model import BaseModel, Base
from sqlalchemy import String, DateTime, Column, ForeignKey
from sqlalchemy.orm import relationship, backref


class User(BaseModel, Base):
    """This is the class for user
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship('Place',
                          backref=backref('user', cascade='all, delete-orphan'),
                          passive_deletes=True,
                          single_parent=True)
    reviews = relationship('Review',
                           backref=backref('user', cascade='all, delete-orphan'),
                           passive_deletes=True,
                           single_parent=True)
