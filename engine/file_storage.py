#!/usr/bin/python3
"""
File storage:  serializes instances to a JSON file and 
    deserializes JSON file to instances:
"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """
    serializes instances to a JSON file and 
    deserializes JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the class atribute objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = '{}.{}'.format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
        file = FileStorage.__file_path
        with open(file, mode="a", encoding="utf-8") as f:
            f.write(json.dumps(FileStorage.__objects))

    def reload(self):
        """deserializes the JSON file to __objects"""
        file = FileStorage.__file_path
        if os.path.exists(file):
            with open(file, mode="a", encoding="utf-8") as f:
                pass

    def update(self, model, id, attr, value):
        pass