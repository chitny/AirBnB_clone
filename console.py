#!/usr/bin/python3
"""
    HBNBCommand class for the console
"""

import cmd
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
            quit: command to exit the program
        """

        return True

    def do_EOF(self, line):
        """
            function to handle EOF (exit the program)
        """

        print()
        return True

    def emptyline(self):
        """
            function to handle enter when empty line
        """

        pass

    def do_create(self, clsname):
        """
            Creates a new instance of BaseModel, saves it
            (to the JSON file) and prints the id.
            use ex: create "ClassName"
        """

        if len(clsname) == 0:
            print('** class name missing **')
            return

        else:

            try:
                new_instance = classes[clsname]()
                print(new_instance.id)
                new_instance.save()

            except:
                print("** class doesn't exist **")

    def do_show(self, clsnameid):
        """
            Prints the string representation of an instance
            based on the class name and id.
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

            if checkbd not in storage.all():
                print("** no instance found **")
                return

            else:
                print(storage.all()[checkbd])
                return

    def do_destroy(self, clsnameid):
        """
            function to handle enter when empty line
        """

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
        splitted = clsname.split()
        objects = storage.all()

        if len(clsname) == 0:
            for key, value in objects.items():
                newlist.append(value.__str__())
            print(newlist)
        else:
            if not splitted[0] in classes:
                print("** class doesn't exist **")
                return
            else:
                for key, value in objects.items():
                    class_name = value.__class__.__name__
                    if class_name == splitted[0]:
                        newlist.append(value.__str__())
                    return
                print(newlist)

    def do_update(self, clsname):
        """
            function to handle enter when empty line
        """

        argus = clsname.split()

        if not clsname:
            print("** class name missing **")
            return
        elif argus[0] not in classes:
            print("** class doesn't exist **")
            return
        elif len(argus) == 1:
            print("** instance id missing **")
            return
        elif "{}.{}".format(argus[0], argus[1]) not in storage.all().keys():
            print("** no instance found **")
            return
        elif len(argus) == 2:
            print("** attribute name missing **")
            return
        elif len(argus) == 3:
            print("** value missing **")
            return
        else:
            checkbd = "{}.{}".format(argus[0], argus[1])
            objects = storage.all()
            if checkbd in objects:
                if argus[2] not in self.attributes:
                    if argus[3][0] in self.specs and argus[3][-1]
                    in self.specs:
                        setattr(objects[checkbd], argus[2],
                                str(argus[3][1: -1]))
                    else:
                        setattr(objects[checkbd], argus[2], str(argus[3]))
                    storage.save()
            else:
                print("** no instance found **")
                return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
