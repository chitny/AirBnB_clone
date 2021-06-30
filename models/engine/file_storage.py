#!/usr/bin/python3
"""Storage class"""

import json
from models.base_model import BaseModel


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

        return FileStorage.__objects

    def new(self, obj):
        """
            sets in __objects the obj with key <obj class name>.id  
        """

        key = obj.__class__.__name__+"."+obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """
            serializes (save) all __objects to the JSON file
        """

        dicts = {}
        for key in self.__objects:
            dicts = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(dicts, file)

    def reload(self):
        """
            deserializes (load) the JSON file to __objects 
        """
        try:
            with open(self.__file_path, "r") as file:
                dict = json.load(file)
        except:
            pass
