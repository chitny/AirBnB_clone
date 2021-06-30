#!/usr/bin/python3
"""Storage class"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """
        This class serializes instances to a JSON file
        and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
            returns the dictionary __objects
        """

        return self.__objects

    def new(self, obj):
        """
            sets in __objects the obj with key <obj class name>.id
        """

        key = str(obj.__class__.__name__) + "." + str(obj.id)
        self.__objects.update({key: obj})

    def save(self):
        """
            serializes (save) all __objects to the JSON file
        """

        dicts = {}
        for key in self.__objects:
            dicts[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(dicts, file)

    def reload(self):
        """
            deserializes (load) the JSON file to __objects
        """

        classes = {'BaseModel': BaseModel, 'User': User, 'City': City,
                   'State': State, 'Amenity': Amenity, 'Place': Place,
                   'Review': Review}

        try:
            with open(self.__file_path, "r") as file:
                newdict = json.load(file)

            for keys, values in newdict.items():
                spl = keys.split('.')
                new = classes[spl[0]](**values)
                self.new(new)
        except:
            pass
