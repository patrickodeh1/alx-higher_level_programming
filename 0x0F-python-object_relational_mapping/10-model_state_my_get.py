#!/usr/bin/python3

"""
This module connects to a MySQL database and lists all State objects.
It uses SQLAlchemy ORM to interact with the database.
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, db_name), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter_by(
        name=state_name).order_by(State.id).first()
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")

    session.close()
