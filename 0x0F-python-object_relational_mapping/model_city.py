#!/usr/bin/python3
"""File contains class definition of City"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base, State


class City(Base):
    """City class inherits from State class
    Links to MySQL table 'cities'
    Attributes:
        id: column of autogenerated unique integer, can't be NULL, primary key
        name: column of string with max 128 characters, can't be NULL
        state_id: column of integer, can't be NULL, foreign key (states.id)
    """
    __tablename__ = 'cities'
    id = Column('id', Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    state = relationship("State", back_populates="cities")

State.cities = relationship("City", order_by=City.id, back_populates="state"
