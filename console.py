#!/usr/bin/python3
"""
Console module for the command interpreter.
"""
import re
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import cmd


class HBNBCommand(cmd.Cmd):
    """command line intepretrer for airbnb"""
    prompt = "(hbnb) "
    types = [
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    ]

    def precmd(self, line):
        """runs befor command is ex"""
        sho = re.compile(r'''
                \.show\(["\']([\w-]+)["\']\)$
                ''', re.VERBOSE)
        des = re.compile(r'''
                \.destroy\(["\']([\w-]+)["\']\)$
                ''', re.VERBOSE)
        if line.endswith(".all()"):
            classn = line.split('.')[0]
            return f'all {classn}'
        if line.endswith(".count()"):
            classn = line.split('.')[0]
            return f'count {classn}'
        if sho.search(line):
            classn = line.split('.')[0]
            uuids = sho.search(line).group(1)
            return f'show {classn} {uuids}'
        if des.search(line):
            classn = line.split('.')[0]
            uuids = des.search(line).group(1)
            return f'destroy {classn} {uuids}'
        else:
            return line

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
        """the string representation of an instance"""
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
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, lines):
        """this method deletes instance"""
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
                    i = storage.all()
                    if key in i:
                        del i[key]
                        storage.save()
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_all(self, lines):
        """this method lists all the str represenation"""
        from models import storage
        list_rep = []
        if lines == "" or not lines:
            print([str(v) for k, v in storage.all().items()])
        else:
            if lines in self.types:
                (list_rep.extend(str(i) for i in storage.all().values()
                 if isinstance(i, globals()[lines])))
                print(list_rep)
            else:
                print("** class doesn't exist **")

    def do_update(self, lines):
        """this method updates instance"""
        from models import storage
        line = lines.split()
        if lines == "" or not lines:
            print("** class name missing **")
            return
        if line[0] in self.types:
            if len(line) < 2:
                print("** no instance id **")
                return
            else:
                k = f"{line[0]}.{line[1]}"
                if k in storage.all():
                    if len(line) < 3:
                        print("** attribute name missing **")
                    else:
                        if len(line) < 4:
                            print("** value missing **")
                        else:
                            i = storage.all()[k]
                            setattr(i, line[2], eval(line[3]))
                            storage.save()
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_count(self, lines):
        """the number of instance"""
        from models import storage
        if lines != "" and not None:
            if lines in self.types:
                c = 0
                for i in storage.all().values():
                    if type(i) == globals()[lines]:
                        c = c + 1
                print(c)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
