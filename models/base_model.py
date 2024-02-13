#!/usr/bin/python3
"""
File that contains BaseModel class that defines all common attributes/methods\
      for other classes
"""
import uuid
import datetime
import models


class BaseModel:
    """
    class that defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize New Class Instance
        """

        # Check if kwargs exists
        if kwargs:
            # Get the dictionary of attributes from kwargs
            if "__class__" in kwargs:
                kwargs.pop("__class__")
            format: str = "%Y-%m-%dT%H:%M:%S.%f"
            # Remmeber that it is a string so we have to.
            # convert it to datetime format= "%Y-%m-%dT%H:%M:%S.%f"
            kwargs["created_at"] = datetime.datetime.strptime(
                kwargs["created_at"], format
            )
            kwargs["updated_at"] = datetime.datetime.strptime(
                kwargs["updated_at"], format
            )
            self.__dict__.update(**kwargs)
        else:
            # Create class uuid (Unique identifier)
            self.id = str(uuid.uuid4())
            # Created at time for the class instance
            self.created_at = datetime.datetime.now()
            # Updated at time for the class instance
            self.updated_at = datetime.datetime.now()
            # Storage
            models.storage.new(self)

    def __str__(self) -> str:
        """
        String Representation of Object

        Returns:
            - String
        """
        attributes: dict = self.__dict__
        attributes["__class__"] = str(self.__class__.__name__)

        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            attributes,
        )

    def __repr__(self) -> str:
        """
        String Representation of Object

        Returns:
            - String
        """
        attributes: dict = self.__dict__

        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            attributes,
        )

    def save(self) -> None:
        """
        Class method used to update updated_at attribute.
        """
        # Update updated add
        self.updated_at = datetime.datetime.now()
        # Update the key
        models.storage.new(self)
        # Call storage.save()
        models.storage.save()

    def to_dict(self) -> object:
        """
        Getter method dictionary containing all keys/values of\
          __dict__ of the instance

        Returns:
            - Python Dictionary!.
        """
        attributes = self.__dict__.copy()
        attributes["created_at"] = attributes["created_at"].isoformat()
        attributes["updated_at"] = attributes["updated_at"].isoformat()
        attributes["__class__"] = self.__class__.__name__
        return attributes
