#!/usr/bin/python3
"""a python file that contains the class definition of
a State and an instance Base = declarative_base()"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    represent a state in the database.

    Attributes:
      __tablename__: the name of table
      id (int): The id of the state.
      name (str): The name of the state.
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
