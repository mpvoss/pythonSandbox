from sqlalchemy import Column, Integer, String
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import random
import DatabaseConfig
import InterestUtil

firstNames = ['Stephen', 'Jim', 'Josh', 'Adam', 'Ryan', 'Judy', 'Stephanie', 'Rhonda', 'Bailey', 'Kendra']
surnames = ['Adams', 'Hall', 'Parker', 'Hernandez', 'Edwards', 'Fowler', 'Sandy', 'Robinson', 'Calvin']


class User(DatabaseConfig.Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)
    interests= relationship("Interest", back_populates="parent")

    def __repr__(self):
        result = "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)
        for interest in self.interests:
            result += interest.prettyPrint()
        return result

    def prettyPrint(self):
        result = "Name: %s\n" % (self.name)
        for interest in self.interests:
            result += "\t"+interest.prettyPrint()+ "\n"
        return result

def createUser():
    name = random.choice(firstNames) + " " + random.choice(surnames)
    user = User(name = name, password = createPassword())
    InterestUtil.configureInterests(user)
    return user


def createPassword():
    return "password"