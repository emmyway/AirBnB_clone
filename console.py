#!/usr/bin/python3

"""
This file will contain Main console
"""

import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    Class that facilitates command line interpreter
    """
    prompt = "(hbnb) "

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
        """
        pass

    def do_destroy(self, args):
        """
        Method that commits destroy command
        """
        pass
    
    def do_all(self, args):
        """
        Method that commits all command
        """
        pass
    
    def do_update(self, args):
        """
        Method that commits update command
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()