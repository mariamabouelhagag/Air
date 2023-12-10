#!/usr/bin/python3
"""Module for FileStorage class"""

import json


class FileStorage:
    """FileStorage Class"""
    __file_path = "file.json"
    __objects = {}

    
    def all(self):
        """Returns all objects stored in __objects"""
        return FileStorage.__objects

    @classmethod
    def new(cls, obj):
        """Adds a new object to __objects"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        cls.__objects[key] = obj

    @classmethod
    def save(cls):
        """Serializes __objects to the JSON file"""
        my_dict = {key: val.to_dict() for key, val in cls.__objects.items()}
        with open(cls.__file_path, 'w') as f:
            json.dump(my_dict, f)

    @classmethod
    def reload(cls):
        """Deserializes __objects from the JSON file"""
        try:
            with open(cls.__file_path) as f:
                objects = json.load(f)
                for key, value in objects.items():
                    cls_name = value["__class__"]
                    del value["__class__"]
                    cls.new(eval(f"{cls_name}(**value)"))
        except FileNotFoundError:
            pass
