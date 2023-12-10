#!user/bin/python3
"""
the BaseModle class
"""
from uuid import uuid4
from datetime import datetime

import models

class BaseModel:
    """Represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel."""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance."""
        return{
        '__class__' = self.__class__.__name__,
        'id' : self.id,
        'created_at' : str(self.created_at),
        'updated_at' : str(self.updated_at)
        }

    def __str__(self):
        """Returns string representation of BaseModel class"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
