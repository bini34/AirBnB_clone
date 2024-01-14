#!/usr/bin/python3
"""
Console module for the command interpreter.
"""
from models.base_model import BaseModel
import cmd


class HBNBCommand(cmd.Cmd):
    """command line intepretrer for airbnb"""
    prompt = "(hbnb) "
    types = ["BaseModel"]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

    def do_create(self, lines):
        """this creates instance with create command """
        if lines == "":
            print("** class name missing **")
            return
        elif lines in self.types:
            instance = eval(lines)()
            instance.save()
            print(instance.id)
        else:
            print("** class doesn't exit **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
