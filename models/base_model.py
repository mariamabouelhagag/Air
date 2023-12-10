#!user/bin/python3

from datetime import datetime
from uuid import uuid4

import models


class BaseModel:
    """
    Base class for all models
    """
    def __init__(self, *args, **kwargs):
      """
      Initializes a new instance of BaseModel
      """
      self.id = str(uuid4())
      self.created_at = datetime.today()
      self.updated_at = datetime.today()
      if kwargs:
        for key, value in kwargs.items():
          setattr(self, key, value)
          if key == "created_at" or key == "updated_at":
            setattr(self, key, datetime.strptime(value, "%Y-%m-%d %H: %M: %S"))
          if key == "id" or key == "__class__":
            setattr(self, key, value)
        models.storage.new(self)

      def save(self):
        """
        Updates the updated_at attribute
        """
        self.updated_at = datetime.today()
        models.storage.save()

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
      dictionary['created_at'] = self.created_at.isoformat()
      dictionary['updated_at'] = self.updated_at.isoformat()
      return dictionary
