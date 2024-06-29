#!/usr/bin/python3

import SQLAlchemy
from model_state import State, session
"""
This module connects to a MySQL database and lists all State objects.
It uses SQLAlchemy ORM to interact with the database.
"""


def list_states():
    """
         Fetches all State records from the database and prints them.
    """
    states = session.query(state).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))


if __name__ == "__main__":
    list_states()
