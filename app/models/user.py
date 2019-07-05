from app.models.base import Base, db
from sqlalchemy import Column, Integer

class User(Base):
    id = Column(Integer, primary_key = True)
