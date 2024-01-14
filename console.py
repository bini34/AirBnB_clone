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
            to_print = []
            alll = storage.all()
            for obj in alll:
                to_print.append(str(alll[obj]))
            print(to_print)
        elif lines not in self.types:
            print("** class doesn't exist **")
        else:
            for i in storage.all().values():
                if isinstance(i, globals()[lines]):
                    list_rep.append(str(i))
            print(list_rep)


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
