#!/usr/bin/python3

"""
module that connects to database
and lists all cities.
"""

from model_state import State, session


def list_states():
    states = session.query(state).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))


if __name__ == "__main__":
    list_states()
