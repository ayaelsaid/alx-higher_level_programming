#!/usr/bin/python3
"""Script to list all State objects from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:/{}'.format(
                           username, password, database))
    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects
    states_first = session.query(State).order_by(State.id).first()
    if states_first is not None:
        print("{}: {}".format(states_first.id, state_first.name))
    else:
        print("Nothing")

    # Close session
    session.close()
