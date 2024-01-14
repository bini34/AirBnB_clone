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

    def do_show(self, lines):
        """the string represen tation of an instance"""
        if lines == "":
            print("** class name missing **")
        else:
            line = lines.split(" ")
            if line[0] in self.types:
                if len(line) < 2:
                    print("** instance id missing **")
                    return
                else:
                    from models import storage
                    key = f"{line[0]}.{line[1]}"
                    instance = storage.all()
                    if key in instance:
                        print(instance[key])
            else:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
