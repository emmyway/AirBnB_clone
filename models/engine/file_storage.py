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
    
    def find(self, model: str, id: str) -> Dict:
        """
        method used to find an instance of a model by it's class name and ID

        Args:
            - model (str): Represents the class name of a model
            - id (str): Represents the id of the model

        Returns:
            - Dict or None in case the instance does not exist
        """
        # Key
        key = f"{model}.{id}"
        # Check if key exists in objects
        if key in self.__objects:
            return self.__objects[key]
        # Return none incase if instance does not exist
        return None
        
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
    
    def delete(self, model, id) -> None:
        """
        Method used to delete an instance using class name and id

        Args:
            - model (str): Represents the class name of a model
            - id (str): Represents the id of the model

        Returns:
            - None
        """
        # Get the key using model name and id
        key = f"{model}.{id}"
        
        if key in self.__objects:
            # Delete instance
            del self.__objects[key]
            # Save
            self.save()

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
        


