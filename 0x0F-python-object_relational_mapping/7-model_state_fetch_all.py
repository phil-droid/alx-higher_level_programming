#!/usr/bin/python3
# lists all State objects from the database hbtn_0e_6_usa

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Connect to a MySQL server running on localhost at port 3306
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name), pool_pre_ping=True)

    # Create all tables in the database
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database for all State objects
    states = session.query(State).order_by(State.id)

    # Print the results
    for state in states:
        print("{}: {}".format(state.id, state.name))
