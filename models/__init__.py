from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
storage = FileStorage()
classes = {
    BaseModel.__name__: BaseModel
}
storage.reload()
