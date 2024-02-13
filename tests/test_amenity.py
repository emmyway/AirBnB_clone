#!/usr/bin/python3
"""
Test File for the Amenity class, a class that defines all common \
attributes/methods for other classes
"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from typing import Dict


class TestAmenity(unittest.TestCase):
    """
    Class used to test Amenity model
    """

    def test_inheritance(self):
        """
        Test inheritance
        """
        # Create an instance of Amenity
        amenity_instance = Amenity()

        # Check if it is a subclass of BaseModel
        self.assertTrue(issubclass(Amenity, BaseModel))

        # Check if the instance is an instance of both Amenity and BaseModel
        self.assertTrue(isinstance(amenity_instance, Amenity))
        self.assertTrue(isinstance(amenity_instance, BaseModel))

        # Check the type of the instance
        self.assertTrue(type(amenity_instance) is Amenity)
