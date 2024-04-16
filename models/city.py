#!/usr/bin/python3
"""
This script defines a City class that inherits from the BaseModel class.
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """
    A class representing a city, inheriting from BaseModel.

    Attributes:
    - state_id (str): The ID of the state where the city is located.
    - name (str): The name of the city.
    """
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship('Place', backref='cities')
