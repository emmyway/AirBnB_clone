#!/usr/bin/python3
"""
This file will contain Main console
"""
import cmd
from models.base_model import BaseModel
from models import storage
from typing import Union


class HBNBCommand(cmd.Cmd):
    """
    Class that facilitates command line interpreter

    Attributes:
        - prompt (str): Command line message
        - support_models (list(str)): list that contains supported models
    """

    prompt = "(hbnb) "
    support_models = [
        "BaseModel",
    ]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("\nExiting the HBNB console.")
        return True

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

    def do_create(self, args):
        """
        Method that commits create command

        Args:
            - args (str): Input that represent the command input as in string.
        """
        # Check if arguments is empty
        if not args:
            print("** class name missing **")
            return

        # Get arguments
        arguments: list[str] = args.split(" ")
        # Best usecase for this is match case where as if the model exists it operates
        match (arguments[0]):
            case "BaseModel":
                # Initiate a new instance of base model
                new: BaseModel = BaseModel()
                # Don't forget to save
                new.save()
            case _:
                # Default case in case the model entered is does not exist
                print("** class doesn't exist **")

    def do_show(self, args):
        """
        Method that commits show command

        Args:
            - args (str): Input that represent the command input as in string.
        """
        # Check if arguments is empty
        if not args:
            print("** class name missing **")
            return

        # Get arguments
        arguments: list[str] = args.split(" ")

        # Check if the model is supported or not
        if arguments[0] not in self.support_models:
            print("** class doesn't exist **")
            return

        # Check if instance id exists or not
        if len(arguments) < 2:
            print("** instance id missing **")
            return

        # Grab all instances
        instance = storage.find(arguments[0], arguments[1])
        # Check if instance exists
        if not instance:
            print("** no instance found **")
            return

        print(instance)

    def do_destroy(self, args):
        """
        Method that commits destroy command

        Args:
            - args (str): Input that represent the command input as in string.
        """
        # Check if arguments is empty
        if not args:
            print("** class name missing **")
            return

        # Get arguments
        arguments: list[str] = args.split(" ")

        # Check if the model is supported or not
        if arguments[0] not in self.support_models:
            print("** class doesn't exist **")
            return

        # Check if instance id exists or not
        if len(arguments) < 2:
            print("** instance id missing **")
            return

        # Grab all instances
        instance = storage.find(arguments[0], arguments[1])
        # Check if instance exists
        if not instance:
            print("** no instance found **")
            return

        # Destroy the model
        storage.delete(arguments[0], arguments[1])

    def do_all(self, args):
        """
        Method that commits all command

        Args:
            - args (str): Input that represent the command input as in string.
        """
        # Get the models
        models = storage.all()

        # if no argument just print them
        if not args:
            reformed: list = []
            for key, value in list(models.items()):
                copy_value = {k: v for k, v in value.items() if k != "__class__"}
                reconvert: object
                if value["__class__"] == "BaseModel":
                    reconvert: BaseModel = BaseModel(**copy_value)
                reformed.append(repr(reconvert))
            print(reformed)
            return

        # Check if the model mention exists within
        if args not in self.support_models:
            print("** class doesn't exist **")
            return

        filtered_models: list = [
            value for value in models.values() if value["__class__"] == args
        ]
        # Print out the results
        models: list = []

        match (args):
            case "BaseModel":
                models: list = [repr(BaseModel(value)) for value in filtered_models]

        print(models)

    def do_update(self, args):
        """
        Method that commits update command

        Args:
            - args (str): Input that represent the command input as in string.
        """
        # Check if arguments is empty
        if not args:
            print("** class name missing **")
            return

        # Get arguments
        arguments: list[str] = args.split(" ")

        # Check if the model is supported or not
        if arguments[0] not in self.support_models:
            print("** class doesn't exist **")
            return

        # Check if instance id exists or not
        if len(arguments) < 2:
            print("** instance id missing **")
            return

        # Grab all instances
        instance = storage.find(arguments[0], arguments[1])
        # Check if instance exists
        if not instance:
            print("** no instance found **")
            return

        # Check if instance id exists or not
        if len(arguments) < 3:
            print("** attribute name missing **")
            return

        # Check if instance id exists or not
        if len(arguments) < 4:
            print("** value missing **")
            return

        parameter: str = arguments[2]
        value: str = arguments[3]

        instance_copy = {k: v for k, v in instance.items()}
        # instance to model
        model: object
        if instance_copy["__class__"] == "BaseModel":
            model: BaseModel = BaseModel(**instance_copy)

        # update/set attribute
        setattr(model, parameter, value)
        model.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
