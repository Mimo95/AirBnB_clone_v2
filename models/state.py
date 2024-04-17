#!/usr/bin/python3
"""
This script defines a State class that inherits from the BaseModel class.
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """
    A class representing a state, inheriting from BaseModel and Base.

    Attributes:
    - name (str): The name of the state.
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state')

    @property
    def cities(self):
        from models.engine.file_storage import FileStorage
        from models.city import City
        file_storage = FileStorage()
        file_storage.reload()
        cities = []
        for obj_id, obj in file_storage.all().items():
            if isinstance(obj, City) and obj.state_id == self.id:
                cities.append(obj)
