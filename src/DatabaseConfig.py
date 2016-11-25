import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker


# In memory only DB
#engine = create_engine('sqlite:///:memory:', echo=True)

# Real Postgres DB
engine = create_engine('postgresql://mpvoss:password@localhost:5432/test')


Base = declarative_base()

def setupDb():
    # Boilerplate configuration


    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    #Session.configure(bind=engine)
    return Session()