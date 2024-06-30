#!/usr/bin/python3

"""
This module connects to a MySQL database and prints all City objects
from the database hbtn_0e_14_usa.
It uses SQLAlchemy ORM to interact with the database.
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, db_name), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for cities in (session.query(State.name, City.id, City.name)
                   .filter(State.id == City.state_id)):
        print(cities[0] + ": (" + str(cities[1]) + ") " + cities[2])

    session.close()
