import sqlite3 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative  import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///:users.db:', echo=True)
Base = declarative_base(engine)

class Profiles(Base):
    
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)
    email = Column(String)

    def __init__(self, name, password=None, email=None):
        self.name = name
        self.email = email
        self.password = password

    
    def __repr__(self):
       return "<User(name='%s', password='%s', email;='%s')>" % (
                            self.name, self.fullname, self.password)
Base.metadata.create_all()

Session = sessionmaker(bind=engine)
s = Session()

