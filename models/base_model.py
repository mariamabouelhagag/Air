#!user/bin/env python3

import uuid
from datetime import datetime

from models.storage_handler import StorageHandler


class BaseModel:
    """
    Base class for all models
    """
    def __init__(self):
      time_format = "%Y-%m-%dT%H:%M:%S.%f"
      self.id = str(uuid.uuid4())
      self.created_at = datetime.today()
      self.updated_at = datetime.today()
      if len(kwargs) != 0:
        for x, y in kwargs.items():
            if x == "created_at" or x == "updated_at":
                self.__dict__[x] = datetime.strptime(y, time_format)
            else:
                self.__dict__[x] = y
      else:
        StorageHandler().add(self)
    
    def save(self):
      """
      Updates the updated_at attribute
      """
      self.updated_at = datetime.today()
      StorageHandler().persist()
    def __str__(self):
      """
      Returns the string that includes the class name,the id and the dic 
      contains all the instance attributes of the object as key-value pairs 
      """
      return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def to_dict(self):
      """
      Returns a dictionary containing all the instance attributes of the object
      """
      dictionary = self.__dict__.copy()
      dictionary['__class__'] = self.__class__.__name__
      dictionary['created_at'] = dictionary['created_at'].isoformat()
      dictionary['updated_at'] = dictionary['updated_at'].isoformat()
      return dictionary
