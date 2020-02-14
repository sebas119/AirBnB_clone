#!/usr/bin/python3

"""
    Defines a class FileStorage.
"""

import json
import models
from models.base_model import BaseModel


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return all the objects saved in the file"""

        return self.__objects

    def new(self, obj):
        """Add new objects in a dictionary"""
        objId = obj.__class__.__name__ + '.' + obj.id
        self.__objects[objId] = obj

    def save(self):
        """Save object representation of JSON to a file"""

        to_json = {}
        with open(self.__file_path, mode='w', encoding='UTF-8') as myfile:
            for key, val in self.__objects.items():
                to_json[key] = val.to_dict()
            json.dump(to_json, myfile)

    def reload(self):
        """Function that creates an Object from a JSON file"""

        from_json = {}
        try:
            with open(self.__file_path, mode='r', encoding="UTF-8") as myfile:
                from_json = json.load(myfile)
                for key, value in from_json.items():
                    bm = BaseModel(**value)
                    self.__objects[key] = bm
        except:
            pass
