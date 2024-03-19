#!/usr/bin/python3
"""Script to list all State objects from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create engine
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects
    state_first = session.query(State).order_by(State.id).first()
    if state_first is not None:
        print("{}: {}".format(state_first.id, state_first.name))
    else:
        print("Nothing")

    # Close session
    session.close()
