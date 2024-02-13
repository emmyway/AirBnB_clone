#!/usr/bin/python3
"""
Test File for the Review class, a class that defines all common \
attributes/methods for other classes
"""

import unittest
from models.base_model import BaseModel
from models.review import Review
from typing import Dict


class TestReview(unittest.TestCase):
    """
    Class used to test Review model
    """

    def test_inheritance(self):
        """
        Test inheritance
        """
        # Create an instance of Review
        Review_instance = Review()

        # Check if it is a subclass of BaseModel
        self.assertTrue(issubclass(Review, BaseModel))

        # Check if the instance is an instance of both Review and BaseModel
        self.assertTrue(isinstance(Review_instance, Review))
        self.assertTrue(isinstance(Review_instance, BaseModel))

        # Check the type of the instance
        self.assertTrue(type(Review_instance) is Review)
