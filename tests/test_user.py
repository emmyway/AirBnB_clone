#!/usr/bin/python3
"""
Test File for the User class, a class that defines all common \
attributes/methods for other classes
"""

import unittest
from models.base_model import BaseModel
from models.user import User
from typing import Dict


class TestUser(unittest.TestCase):
    """
    Class used to test User model
    """

    def test_inheritance(self):
        """
        Test inheritance
        """
        # Create an instance of User
        User_instance = User()

        # Check if it is a subclass of BaseModel
        self.assertTrue(issubclass(User, BaseModel))

        # Check if the instance is an instance of both User and BaseModel
        self.assertTrue(isinstance(User_instance, User))
        self.assertTrue(isinstance(User_instance, BaseModel))

        # Check the type of the instance
        self.assertTrue(type(User_instance) is User)