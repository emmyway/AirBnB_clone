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

    def save(self) -> None:
        """
        Method that serializes objects to the JSON file
        """
        # Jsonify the objects
        json_data = json.dumps(self.all())

        # Write objects to json file
        with open(self.__file_path,mode= 'w', encoding='utf-8') as file:
            file.write(json_data)

    def reload(self) -> None:
        """
        Method that is used to load objects from JSON file if exists
        """
        contents: str = ""
        # Check if file exists
        if os.path.exists(self.__file_path):
            # Read contents from file
            with open(self.__file_path, mode='r', encoding='utf-8') as file:
                contents: str = file.read()
            # Deserialize contents and save to instance __objects
            self.__objects: Dict = json.loads(contents)
        


