#!/usr/bin/python3
"""
Test File for the State class, a class that defines all common \
attributes/methods for other classes
"""

import unittest
from models.base_model import BaseModel
from models.state import State
from typing import Dict


class TestState(unittest.TestCase):
    """
    Class used to test State model
    """

    def test_inheritance(self):
        """
        Test inheritance
        """
        # Create an instance of State
        State_instance = State()

        # Check if it is a subclass of BaseModel
        self.assertTrue(issubclass(State, BaseModel))

        # Check if the instance is an instance of both State and BaseModel
        self.assertTrue(isinstance(State_instance, State))
        self.assertTrue(isinstance(State_instance, BaseModel))

        # Check the type of the instance
        self.assertTrue(type(State_instance) is State)
