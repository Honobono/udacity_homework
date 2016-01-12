import os
import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Stock(Base):
    sqlite_autoincrement=True
    __tablename__ = 'stock'
    id = Column(Integer, primary_key = True)
    name = Column(String(20), nullable = False)
    total = Column(Integer, primary_key = True)


class itemProperty(Base):
    __tablename__ = 'itemProperty'
    id = Column(Integer, primary_key = True)
    name = Column(String(20), nullable = False)
    dates = Column(String(10), nullable = False)
    count = Column(Integer, primary_key = True)
    category = Column(String(20), nullable = False)
    note = Column(String(50))
    stock_id = Column(Integer, ForeignKey('stock.id'))
    stock = relationship(Stock)

engine = create_engine('sqlite:///lean_fridge_app.db')

Base.metadata.create_all(engine)