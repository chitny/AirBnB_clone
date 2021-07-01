#!/usr/bin/python3
"""
    HBNBCommand class for the console
"""

import cmd
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage

classes = {'Amenity': Amenity, 'BaseModel': BaseModel, 'City': City,
           'Place': Place, 'Review': Review, 'State': State,
           'User': User}


class HBNBCommand(cmd.Cmd):
    """
        console.py that contains the entry point
        of the command interpreter
    """

    prompt = '(hbnb) '

    def do_quit(self, line):
        """
            Quit: command to exit the program
        """

        return True

    def do_EOF(self, line):
        """
            Function to handle EOF (exit the program)
        """

        print()
        return True

    def emptyline(self):
        """
            Function to handle enter when empty line
        """

        pass

    def do_create(self, clsname):
        """
            Creates a new instance of BaseModel, saves it
            (to the JSON file) and prints the id.
            use ex: create "ClassName"
        """

        if not clsname:
            print('** class name missing **')
        elif clsname not in classes:
            print("** class doesn't exist **")
        else:
            new_instance = classes[clsname]()
            print(new_instance.id)
            new_instance.save()

    def do_show(self, clsnameid):
        """
            Prints the string representation of an instance
            based on the class name and id.
        """

        argus = clsnameid.split()

        if not clsnameid:
            print('** class name missing **')
            return
        elif argus[0] not in classes:
            print("** class doesn't exist **")
            return
        elif len(argus) == 1:
            print("** instance id missing **")
            return
        if len(argus) == 2:

            checkbd = "{}.{}".format(argus[0], argus[1])

            if checkbd not in storage.all():
                print("** no instance found **")

            else:
                print(storage.all()[checkbd])

    def do_destroy(self, clsnameid):
        """
            Function to handle enter when empty line
        """

        argus = clsnameid.split()

        if not argus:
            print('** class name missing **')
            return

        elif argus[0] not in classes:
            print("** class doesn't exist **")
            return

        elif len(argus) < 2:
            print("** instance id missing **")
            return

        if len(argus) == 2:

            checkbd = "{}.{}".format(argus[0], argus[1])

            try:
                storage.all().pop(checkbd)
                storage.save()

            except:
                print("** no instance found **")

    def do_all(self, clsname):
        """
            Prints all string representation of all instances
            based or not on the class name.
        """

        newlist = []
        allitem = storage.all()
        xclsname = clsname.split()

        if clsname and clsname not in classes:
            print("** class doesn't exist **")

        elif clsname in classes:
            for key, value in allitem.items():
                class_name = value.__class__.__name__
                if class_name == xclsname[0]:
                    newlist.append(value.__str__())
        else:
            for key, value in allitem.items():
                newlist.append(str(key) + " " + str(value))
        if newlist != []:
            print(newlist)

    def do_update(self, clsname):
        """
            Function to handle enter when empty line
        """

        argus = clsname.split()

        if not clsname:
            print("** class name missing **")

        elif argus[0] not in classes:
            print("** class doesn't exist **")

        elif len(argus) == 1:
            print("** instance id missing **")

        elif "{}.{}".format(argus[0], argus[1]) not in storage.all().keys():
            print("** no instance found **")

        elif len(argus) == 2:
            print("** attribute name missing **")

        elif len(argus) == 3:
            print("** value missing **")

        else:
            setattr(storage.all()[argus[0]+"."+argus[1]],
                    argus[2], argus[3])

    def do_count(self, clsname):
        """
        Counts the number of the objects in File Storage
        """
        argus = clsname.split()
        allitem = storage.all()
        counter = 0
        for key in allitem.keys():
            if argus[0] in key:
                counter += 1
        print(counter)

    def do_triforce(self, line):
        """
            A Link to the Past was the best!
        """
        print(" ▲ ")
        print("▲ ▲")

    def default(self, line):
        """
            Displays when the console doesn't find your command
        """
        print("This command: \"{}\" is invalid, try again".format(line))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
