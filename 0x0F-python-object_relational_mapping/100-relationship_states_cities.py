#!/usr/bin/python3
"""Adds a new State object to the database with the City "San Francisco"."""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_state import Base, State
from relationship_city import City

if __name__ == '__main__':
    # Get MySQL credentials
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create engine and session
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(mysql_username, mysql_password, database_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create new state and city
    new_state = State(name='California')
    new_city = City(name='San Francisco', state=new_state)

    # Add city to state and state to session
    new_state.cities.append(new_city)
    session.add(new_state)

    # Commit changes and close session
    session.commit()
    session.close()
