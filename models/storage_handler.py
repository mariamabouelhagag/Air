import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class StorageHandler:
    """Represent an abstracted storage engine."""

    storage_file = "storage.json"
    data_objects = {}

    def get_all(self):
        """Return the dictionary __objects."""
        return StorageHandler.data_objects

    def add(self, instance):
        """Set in __objects instance with key <instance_class_name>.id"""
        class_name = instance.__class__.__name__
        StorageHandler.data_objects["{}.{}".format(class_name, instance.id)] = instance

    def persist(self):
        """Serialize __objects to the JSON file storage_file."""
        object_dict = StorageHandler.data_objects
        serialized_dict = {obj: object_dict[obj].to_dict() for obj in object_dict}
        with open(StorageHandler.storage_file, "w") as f:
            json.dump(serialized_dict, f)

    def load(self):
        """Deserialize the JSON file storage_file to __objects, if it exists."""
        try:
            with open(StorageHandler.storage_file) as f:
                serialized_dict = json.load(f)
                for o in serialized_dict.values():
                    class_name = o["__class__"]
                    del o["__class__"]
                    self.add(eval(class_name)(**o))
        except FileNotFoundError:
            return
