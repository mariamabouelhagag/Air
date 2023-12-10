#!/usr/bin/python3
"""Module for Console unit tests."""
import unittest
from io import StringIO
from unittest.mock import patch

from console import HBNBCommand

from models.base_model import BaseModel
from models.engine.file_storage import storage


class TestHBNBCommand_prompting(unittest.TestCase):
  """Unittests for testing prompting of the HBNB command interpreter."""

  def test_prompt(self):
      self.assertEqual("(hbnb) ", HBNBCommand.prompt)

  def test_empty_line(self):
      with patch("sys.stdout", new=StringIO()) as output:
          self.assertFalse(HBNBCommand().onecmd(""))
          self.assertEqual("", output.getvalue().strip())

class TestHBNBCommand_exit(unittest.TestCase):
    """Unittests for testing exiting from the HBNB command interpreter."""

    def test_quit_exits(self):
        self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF_exits(self):
        self.assertTrue(HBNBCommand().onecmd("EOF"))


if __name__ == '__main__':
  unittest.main()
