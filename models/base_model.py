#!/usr/bin/python3
"""BaseModel class"""

from datetime import datetime
from uuid import uuid4


class BaseModel:
    """BaseModel defines all common attributes/methods for other classes"""

    def __init__(self):
        """
             init of BaseModel Class
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
            returns: [<class name>] (<self.id>) <self.__dict__>
        """
        classname = self.__class__.__name__
        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)

    def save(self):
        """
            updates the public instance attribute updated_at
            with the current datetime
        """

        self.updated_at = datetime.now()

    def to_dict(self):
        """
            returns a dictionary containing all keys/values of __dict__
            of the instance plus class name, created ad and update at
            attrs
        """

        newdict = self.__dict__.copy()
        newdict["__class__"] = self.__class__.__name__
        newdict["created_at"] = self.created_at.isoformat()
        newdict["updated_at"] = self.updated_at.isoformat()
        return newdict
