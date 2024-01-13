#!/usr/bin/python3
"""file management"""


import os
import json
from models.base_model import BaseModel

class FileStorage:
    """file system for airbnb"""

    __file_path = 'file.json'
    __objects = {}
    __cls = {"BaseModel": BaseModel}

    def all(self):
        """returns all objects"""
        return FileStorage.__objects

    def new(self, obj):
        """new object"""
        k = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[k] = obj

    def save(self):
        """saves the objects"""
        new = {prop: val.to_dict() for prop, val in self.__objects.items()}
        with open(FileStorage.__file_path, "w") as opened_file:
            json.dump(new, opened_file)

    def reload(self):
        """file reload"""
        try:
            with open(FileStorage.__file_path, "r") as opened_file:
                    loaded = json.load(opened_file)
                    for key, value in loaded.items():
                        class_name, obj_id = key.split('.')
                        instance = self.__cls[class_name](**value)
                        self.__objects[key] = instance

        except FileNotFoundError:
            pass
