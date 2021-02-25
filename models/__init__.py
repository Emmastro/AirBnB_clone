from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

storage = FileStorage()


class Classes(dict):
    """ classes """
    def __getitem__(self, key):
        """get item"""
        try:
            return super(Classes, self).__getitem__(key)
        except Exception as e:
            raise Exception("** class doesn't exist **")


models = [BaseModel, Place, State, City, Amenity, Review]
classes = Classes(**{x.__name__: x for x in models})

storage.reload()
