#!/usr/bin/python3
"""Defines the Amenity class."""

from models.base_model import BaseModel
import json


class Amenity(BaseModel):
    """Represent an amenity.

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""
