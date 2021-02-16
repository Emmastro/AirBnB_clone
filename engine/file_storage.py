#!/usr/bin/python3
"""
File storage:  serializes instances to a JSON file and 
    deserializes JSON file to instances:
"""
import json
import os
from models.base_model import BaseModel
from json import JSONEncoder


class FileStorage:
    """
    serializes instances to a JSON file and 
    deserializes JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        super().__init__()
        self.reload()

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
            f.write(json.dumps(FileStorage.__objects, cls=BaseModelEncoder,  indent=4))

    def reload(self):
        """deserializes the JSON file to __objects"""
        file = FileStorage.__file_path
        if os.path.exists(file):
            with open(file, mode="r", encoding="utf-8") as f:
                file_string = f.read()#.replace('\n', '')
                self.__objects = json.loads(file_string)

    def update(self, obj_name, obj_id, attr, value):
        try:
            model = self.__objects["{}.{}".format(obj_name,obj_id)]
            setattr(model, attr, value)
        except:
            raise Exception("** no instance found **")

    def find(self, obj_name, obj_id):
        try:
            return self.__objects["{}.{}".format(obj_name,obj_id)]
        except:
            raise Exception("** no instance found **")
    
    def delete(self, obj_name, obj_id):
        try:
            del(self.__objects["{}.{}".format(obj_name,obj_id)])
        except:
            raise Exception("** no instance found **")


class BaseModelEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, BaseModel):
            return o.to_dict()
        return super().default(o)
