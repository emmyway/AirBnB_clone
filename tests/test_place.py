#!/usr/bin/python3
"""
Test File for the Place class, a class that defines all common \
attributes/methods for other classes
"""

import unittest
from models.base_model import BaseModel
from models.place import Place
from typing import Dict


class TestPlace(unittest.TestCase):
    """
    Class used to test Place model
    """

    def test_inheritance(self):
        """
        Test inheritance
        """
        # Create an instance of Place
        Place_instance = Place()

        # Check if it is a subclass of BaseModel
        self.assertTrue(issubclass(Place, BaseModel))

        # Check if the instance is an instance of both Place and BaseModel
        self.assertTrue(isinstance(Place_instance, Place))
        self.assertTrue(isinstance(Place_instance, BaseModel))

        # Check the type of the instance
        self.assertTrue(type(Place_instance) is Place)
