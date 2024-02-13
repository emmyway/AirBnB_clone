#!/usr/bin/python3
"""
Test File for the City class, a class that defines all common \
attributes/methods for other classes
"""

import unittest
from models.base_model import BaseModel
from models.city import City
from typing import Dict


class TestCity(unittest.TestCase):
    """
    Class used to test City model
    """

    def test_inheritance(self):
        """
        Test inheritance
        """
        # Create an instance of City
        City_instance = City()

        # Check if it is a subclass of BaseModel
        self.assertTrue(issubclass(City, BaseModel))

        # Check if the instance is an instance of both City and BaseModel
        self.assertTrue(isinstance(City_instance, City))
        self.assertTrue(isinstance(City_instance, BaseModel))

        # Check the type of the instance
        self.assertTrue(type(City_instance) is City)