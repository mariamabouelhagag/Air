#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """HBNBCommand class that includes methods for our command interpreter."""

    prompt = '(hbnb) '
    __classes = [
        'BaseModel',
        'User',
        'State',
        'City',
        'Amenity',
        'Place',
        'Review',
    ]
    def do_EOF(self, line):
        """Exits the interpreter."""
        return True
      
    def do_quit(self, line):
        """Exits the interpreter."""
        return True
      
    def emptyline(self):
      """Overrides the default behavior of the emptyline method."""
      pass
      
    def do_all(self, line):
      """
      prints all the instances of the BaseModel class
      """
      for cls in HBNBCommand.__classes:
        print(cls)
        for obj in models.storage.all().values():
          if obj.__class__.__name__ == cls:
            print(obj)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
