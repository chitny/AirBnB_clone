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


def validator(id):
    ''' 
        takes id and checks for it in __objects
    '''
    newlist = []
    for key in models.storage.all():
        aux = key.split('.')
        newlist.append(aux[1])
    if id in newlist:
        return True
    return False


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
        argus = line.split('.')
        if argus[0] not in classes or len(argus) != 2:
            print("This command doesn't exist: {}". format(argus[0]))
            return

        if argus[1] == 'all()':
            newlist = []
            for key, values in models.storage.all().items():
                cls = key.split('.')
                if cls[0] == argus[0]:
                    newlist.append(values.__str__())
            print(newlist)
            return

        if argus[1] == 'count()':
            count = 0
            for key in models.storage.all():
                cls = key.split('.')
                if cls[0] == argus[0]:
                    count += 1
            print(count)
            return

        if argus[1][0:5] == "show(" and argus[1][-1] == ')':
            subid = argus[1].split('(')
            id = subid[1][:-2]
            id = id[1:]
            if validator(id):
                obj_key = argus[0] + '.' + id
                if obj_key in models.storage.all():
                    print(models.storage.all()[obj_key])
                else:
                    print("** no instance found **")
            else:
                print("** no instance found **")
            return

        if argus[1][0:8] == "destroy(" and argus[1][-1] == ')':
            subid = argus[1].split('(')
            id = subid[1][:-2]
            id = id[1:]
            if validator(id):
                key = argus[0] + '.' + id
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** no instance found **")
            return

        if argus[1][0:7] == 'update(' and argus[1][-1] == ')':
            if argus[1][-2] == '}':
                subargus = argus[1].split('"', 2)
                dic = eval(subargus[2][2:-1])
                for key, values in dic.items():
                    parse = argus[0] + " " + subargus[1] + \
                        " " + key + " " + str(values)
                    self.do_update(parse)
                return
            else:
                subargus = argus[1].split('"')
                clsname = argus[0] + " " + subargus[1] + " " + \
                    str(subargus[3]) + " " + str(subargus[5])
                self.do_update(clsname)
                return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
