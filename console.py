#!/usr/bin/python3

from models.base_model import BaseModel
from models import storage
import cmd


class HBNBCommand(cmd.Cmd):
    """Hbnb command processor."""

    prompt = '(hbnb) '
    file = None

    def emptyline(self):
        """Empty line method"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""

        quit()
        return True

    def help_quit(self):
        print("Quit command to exit the program\n")

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def help_EOF(self):
        print("EOF command to exit the program\n")

    def do_create(self, arg):
        """Create a BaseModel and save the json in a file"""

        if len(arg) > 0:
            if BaseModel.__name__ == arg:
                bm = BaseModel()
                bm.save()
                print(bm.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def help_create(self):
        print("Create a BaseModel and save the json in a file\n")

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id"""

        if len(arg) > 0:
            list_arg = arg.split()
            objects = storage.all()
            if len(list_arg) == 2:
                clsId = '.'.join(list_arg)
                if clsId in objects:
                    print(objects[clsId])
                else:
                    print("** no instance found **")
            else:
                if len(list_arg) == 1:
                    objs_cls = [e.split('.')[0] for e in list(objects.keys())]
                    if arg not in objs_cls:
                        print("** class doesn't exist **")
                    else:
                        print("** instance id missing **")
        else:
            print("** class name missing **")

    def help_show(self):

        msg = "Prints the string representation of an instance "
        msg += "based on the class name and id\n"
        print(msg)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""

        if len(arg) > 0:
            list_arg = arg.split()
            objects = storage.all()
            if len(list_arg) == 2:
                clsId = '.'.join(list_arg)
                if clsId in objects:
                    del objects[clsId]
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                if len(list_arg) == 1:
                    objs_cls = [e.split('.')[0] for e in list(objects.keys())]
                    if arg not in objs_cls:
                        print("** class doesn't exist **")
                    else:
                        print("** instance id missing **")
        else:
            print("** class name missing **")

    def help_destroy(self):
        print("Deletes an instance based on the class name and id\n")

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name"""

        objects = storage.all()
        if len(arg) > 0:
            clsObjs = [str(v) for k, v in objects.items()
                       if arg == k.split('.')[0]]
            if len(clsObjs) > 0:
                print(clsObjs)
            else:
                print("** class doesn't exist **")
        else:
            allObjs = [str(v) for k, v in objects.items()]
            print(allObjs)

    def help_all(self):

        msg = "Prints all string representation of all instances "
        msg += "based or not on the class name"
        print(msg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
