from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Product(Base):

    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    height = Column(Integer)
    firmness = Column(String)
    max_weight = Column(Integer)
    size = Column(String)
    category = Column(String)
