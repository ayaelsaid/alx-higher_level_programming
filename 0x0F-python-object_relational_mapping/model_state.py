#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

"""a python file that contains the class definition of
a State and an instance Base = declarative_base()"""

Base = declarative_base()


class State(Base):
    """
    represent a state in the database.

    Attributes:
      id (int): The unique id for the state.
      name (str): The name of the state.
      state_id (int): ForeignKey
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1],
                           sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
