#!/usr/bin/python3
"""
File that contains a class called FileStorage
"""

import json
import os
from typing import Dict

class FileStorage:
    """
    That serializes instances to a JSON file and deserializes JSON file to instances

    Attributes:
        - __file_path (str): Path to the JSON file (ex: file.json)
        - __objects (dict): empty but will store all objects by "<class name>.id
    """
    __file_path: str = "file.json"
    __objects: Dict = {}

    def all(self) -> Dict:
        """
        Getter method for all object instances

        Returns:
            - Python Dictionary.
        """
        return self.__objects

    def new(self, obj: object) -> None:
        """
        Method sets in objects the object with key <obj class name>.id

        Args:
            - obj (object): Class of anytype that has .id attribute

        Returns:
            - Nothing
        """
        key: str = f"{type(obj).__name__}.{getattr(obj, 'id')}"
        self.__objects[key] = obj.to_dict()

    def save(self):
        pass

    def reload(self):
        pass

