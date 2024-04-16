#!/usr/bin/python3
"""
This script defines a Place class that inherits from the BaseModel class.
"""
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """
    A class representing a place, inheriting from BaseModel.

    Attributes:
    - city_id (str): The ID of the city where the place is located.
    - user_id (str): The ID of the user who owns the place.
    - name (str): The name of the place.
    - description (str): The description of the place.
    - number_rooms (int): The number of rooms in the place.
    - number_bathrooms (int): The number of bathrooms in the place.
    - max_guest (int): The maximum number of guests the place can accommodate.
    - price_by_night (int): The price per night for staying at the place.
    - latitude (float): The latitude coordinate of the place's location.
    - longitude (float): The longitude coordinate of the place's location.
    - amenity_ids (list): A list of IDs representing amenities available at the place.
    """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship('Review', backref='place')

    @property
    def reviews(self):
        """ getter returns list of reviews """
        from models.engine.file_storage import FileStorage
        file_storage = FileStorage()
        file_storage.reload()
        reviews = []
        for obj_id, obj in file_storage.all().items():
            if isinstance(obj, Review) and obj.place_id == self.id:
                reviews.append(obj)
        return reviews
