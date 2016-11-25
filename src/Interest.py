from sqlalchemy import String
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
import DatabaseConfig


class Interest(DatabaseConfig.Base):
    __tablename__ = 'interests'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    value = Column(String)
    priority = Column(Integer)
    parent_id = Column(Integer, ForeignKey('users.id'))
    parent = relationship("User", back_populates="interests")

    def __repr__(self):
        return "%s:%s" % (self.name, self.value)

    def prettyPrint(self):
        return self.name + ": " + self.value