#!/usr/bin/env python3

from sqlalchemy import (Column, String, Integer)
# from sqlalchemy.ext.declarative import declarative_base-this is Deprecated and has been moved with sqlalchemy 2.0
from sqlalchemy.orm import declarative_base #upgrade for use sqlalchemy 2.0

Base = declarative_base()

class Dog(Base):
    __tablename__ = 'dogs'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    breed = Column(String())
