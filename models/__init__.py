from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
storage = FileStorage()

class Classes(dict):
    """ classes """
    def __getitem__(self, key):
        """get item"""
        try:
            return super(Classes, self).__getitem__(key)
        except Exception as e:
            raise KeyError("** class doesn't exist **")

classes = Classes(**{
    BaseModel.__name__: BaseModel
    })

storage.reload()
