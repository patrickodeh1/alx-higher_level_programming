#!/usr/bin/python3

"""
module that connects to database
and lists all cities.
"""
import sys
import MySQLdb
from model_state import State, 

def list_states():
    states = session.query(state).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))


if __name__ == "__main__":
    list_states()
