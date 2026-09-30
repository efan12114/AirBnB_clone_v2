#!/usr/bin/python3
def do_create(self, arg):
        """Creates a new instance of a class"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return False

        new_instance = self.classes[args[0]]()
        for param in args[1:]:
            if "=" in param:
                key, value = param.split('=', 1)
                
                # Handle strings
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1].replace('_', ' ')
                    value = value.replace('\\"', '"')
                # Handle floats
                elif '.' in value:
                    try:
                        value = float(value)
                    except ValueError:
                        continue
                # Handle integers
                else:
                    try:
                        value = int(value)
                    except ValueError:
                        continue
                        
                setattr(new_instance, key, value)
                
        new_instance.save()
        print(new_instance.id)#!/usr/bin/python3
"""Defines the HBNBCommand console entry point."""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB clone project."""

    prompt = "(hbnb) "
    __classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print("")
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_create(self, arg):
        """Creates a new instance of a class with given parameters"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]

        # Resolve class across different console template implementations
        cls = None
        if 'classes' in globals() and isinstance(globals()['classes'], dict) and class_name in globals()['classes']:
            cls = globals()['classes'][class_name]
        elif '_HBNBCommand__classes' in globals() and class_name in globals()['_HBNBCommand__classes']:
            cls = globals()['_HBNBCommand__classes'][class_name]
        elif hasattr(self, 'classes') and isinstance(self.classes, dict) and class_name in self.classes:
            cls = self.classes[class_name]
        else:
            try:
                cls = eval(class_name)
            except (NameError, TypeError):
                print("** class doesn't exist **")
                return

        kwargs = {}
        for param in args[1:]:
            if "=" in param:
                key, val = param.split("=", 1)
                if val.startswith('"') and val.endswith('"'):
                    val = val[1:-1].replace('_', ' ').replace('\"', '"')
                elif '.' in val:
                    try:
                        val = float(val)
                    except ValueError:
                        continue
                else:
                    try:
                        val = int(val)
                    except ValueError:
                        continue
                kwargs[key] = val

        new_instance = cls(**kwargs)
        new_instance.save()
        print(new_instance.id)
    def do_show(self, arg):
        """Prints string representation of instance based on class and id."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        print(objects[key])

    def do_destroy(self, arg):
        """Deletes an instance based on class name and id."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        del objects[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances."""
        args = shlex.split(arg)
        objects = storage.all()
        obj_list = []
        if len(args) == 0:
            for obj in objects.values():
                obj_list.append(str(obj))
            print(obj_list)
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            for key, obj in objects.items():
                if key.startswith(args[0]):
                    obj_list.append(str(obj))
            print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on class name and id."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        obj = objects[key]
        attr_name = args[2]
        attr_val = args[3]

        if hasattr(obj, attr_name):
            attr_type = type(getattr(obj, attr_name))
            try:
                attr_val = attr_type(attr_val)
            except ValueError:
                pass

        setattr(obj, attr_name, attr_val)
        obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
