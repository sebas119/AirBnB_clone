#!/usr/bin/python3

"""
    Defines a class FileStorage.
"""

import json


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
                if type(val) != dict:
                    to_json[key] = val.to_dict()
                else:
                    to_json[key] = val
            json.dump(to_json, myfile)

    def reload(self):
        """Function that creates an Object from a JSON file"""

        try:
            with open(self.__file_path, mode='r', encoding="UTF-8") as myfile:
                self.__objects = json.load(myfile)
        except:
            pass
