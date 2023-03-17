#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create connection to database
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(username, password, db_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query database for states with "a" in their name
    states_with_a = session.query(State).filter(State.name.like('%a%')).all()

    # Delete states from database
    for state in states_with_a:
        session.delete(state)

    # Commit changes to database
    session.commit()

    # Close session
    session.close()
