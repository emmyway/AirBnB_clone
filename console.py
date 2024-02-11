#!/usr/bin/python3
"""
This file will contain Main console
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Class that facilitates command line interpreter

    Attributes:
        - prompt (str): Command line message
        - support_models (list(str)): list that contains supported models
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")
        return True

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
