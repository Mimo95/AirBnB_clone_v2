#!/usr/bin/python3
"""
This script defines a Review class that inherits from the BaseModel class.
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """
    A class representing a review, inheriting from BaseModel.

    Attributes:
    - place_id (str): The ID of the place associated with the review.
    - user_id (str): The ID of the user who wrote the review.
    - text (str): The text content of the review.
    """
    __tablename__ = 'reviews'
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)
