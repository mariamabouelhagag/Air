#!user/bin/env python3
"""
unit tests for base_model.py
"""
import unittest
import uuid
from datetime import datetime

from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
  """
  test instantiation of BaseModel
  """
def test_id(self):
  """
  testt id attribute
  """
  self.assertEqual(BaseModel.id, str(uuid.uuid4()))

def test_created_at(self):
  """
  test created_at attribute
  """
  self.assertEqual(BaseModel.created_at, datetime.today())

def test_updated_at(self):
  """
  test updated_at attribute
  """
  self.assertEqual(BaseModel.updated_at, datetime.today())

def test_to_dict(self):
  """
  test to_dict method
  """
  self.assertEqual(BaseModel.to_dict(), {'__class__': 'BaseModel',
                                          'created' : datetime.today().isoformat(), 
                                          'updated' : datetime.today().isoformat()})
