#!/usr/bin/python3
"""Module for BaseModel class"""
from uuid import uuid4
from datetime import datetime

import models


class BaseModel:
    """BaseModel Class"""

    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel class."""
        time_format = "%Y-%m-%d %H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        models.storage.new(self)

        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ['created_at', 'updated_at']:
                    setattr(self, key,
                            datetime.strptime(value, time_format))
                else:
                    setattr(self, key, value)

    def __str__(self):
        """Return a string representation of the BaseModel."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Save the current state of the BaseModel."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel."""
        return {
            'id': self.id,
            '__class__': self.__class__.__name__,
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at)
        }
