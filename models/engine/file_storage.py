#!/usr/bin/python3
"""
File storage:  serializes instances to a JSON file and
    deserializes JSON file to instances:
"""

import json
import models
import os


class Objects(dict):
    """class object"""

    def __getitem__(self, key):
        """get item"""
        try:
            return super(Objects, self).__getitem__(key)
        except Exception as e:
            raise Exception("** no instance found **")

    def pop(self, key):
        """pop item"""
        try:
            return super(Objects, self).pop(key)
        except Exception as e:
            raise Exception("** no instance found **")


class FileStorage:
    """
    serializes instances to a JSON file and
    deserializes JSON file to instances.
    """

    __file_path = "file.json"
    __objects = Objects()

    def __init__(self):
        """init method"""
        super().__init__()

    def all(self):
        """return the class atribute objects"""
        return FileStorage.__objects

    def reset(self):
        """clear data on __object (cache)"""
        self.__objects.clear()

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = '{}.{}'.format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
        file = FileStorage.__file_path

        with open(file, mode="w", encoding="utf-8") as f:
            f.write(
                json.dumps(
                    FileStorage.__objects,
                    cls=models.base_model.BaseModelEncoder
                    )
                )

    def reload(self):
        """deserializes the JSON file to __objects"""

        file = FileStorage.__file_path
        if not os.path.exists(file):
            return
        try:
            with open(file, mode="r+", encoding="utf-8") as f:
                file_string = f.read()
                data = json.loads(file_string)
                for object_key, model_data in data.items():
                    model_name, model_id = object_key.split('.')
                    model = models.classes[model_name](**model_data)
                    self.new(model)

        except Exception as e:
            print(e)

    def update(self, obj_name, obj_id, attr, value):
        """update object with id `obj_id`"""
        model = self.__objects["{}.{}".format(obj_name, obj_id)]
        setattr(model, attr, value)

    def find(self, obj_name, obj_id):
        """find object with id `obj_id`"""
        return self.__objects["{}.{}".format(obj_name, obj_id)]

    def delete(self, obj_name, obj_id):
        """
        delete object with id `obj_id`
        """
        return self.__objects.pop("{}.{}".format(obj_name, obj_id))
