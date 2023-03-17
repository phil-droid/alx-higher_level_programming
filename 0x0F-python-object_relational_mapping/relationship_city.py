#!/usr/bin/python3
"""
This module defines the City class
improved version of model_city.py
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State


class City(Base):
    """This class defines a city"""

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)

    def __repr__(self):
        return "<City(name='%s')>" % self.name
