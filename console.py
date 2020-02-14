#!/usr/bin/python3

from models.base_model import BaseModel
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
