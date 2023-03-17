#!/usr/bin/python3
"""
improved version of model_state.py
This module defines the State class
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """This class defines a state"""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")

    def __repr__(self):
        return "<State(name='%s')>" % self.name
