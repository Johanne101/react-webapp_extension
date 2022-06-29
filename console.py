#!/usr/bin/python3
"""
Contains the entry point of the command interpreter for HBnB
"""

import cmd
import shlex
from models.basemodel import BaseModel
from models.thread import Thread
from models.post import Post
import models
import re

classes = {"BaseModel": BaseModel, "Thread": Thread, "Post": Post}


class HBNBCommand(cmd.Cmd):
    """
    Define HBnB console
    """

    prompt = "(Spiel) "

    def do_quit(self, args):
        """Quit command to exit console"""
        return True

    def do_EOF(self, args):
        """EOF signal to exit console"""
        return True

    def emptyline(self):
        """overwriting the emptyline method"""
        return False

    def do_create(self, *args):
        """Creates a new instance of class"""
        regex_value = ['^-?//d+.//d+$', '^".+"$']
        if len(args) == 0:
            print("** class name missing **")
            return False
        argu = args[0].split()
        if argu[0] not in classes:
            print("** class doesn't exist **")
            return False
        kDict = {}

        for i in range(1, len(argu)):
            if (re.search('^.+=.+$', argu[i])):
                key = re.search('^.+=', argu[i]).group()[0:-1]
                val = re.search('=.+$', argu[i]).group()[1:]
                value = ''
                if re.search(regex_value[0], val):
                    # float
                    value = float(val)
                elif re.search(regex_value[1], val):
                    # string
                    value = val.replace('_', ' ')[1:-1].replace('//"', '"')
                else:
                    #integer
                    value = eval(val)
                kDict[key] = value
        kDict['reload'] = False
        new_instance = classes[argu[0]](**kDict)
        print(new_instance.id)
        models.storage.new(new_instance)
        models.storage.save()

    def do_show(self, arg):
        """Prints an instance as a string based on the class and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, args):
        """ Shows all objects, or all objects of a class"""
        f = "[{}] ({}):\n{}\n"

        models.storage.all().items()
        if args:
            args = args.split(' ')[0]  # remove possible trailing args
            if args not in classes:
                print("** class doesn't exist **")
                return
            for k, v in models.storage.all().items():
                if k.split('.')[0] == args:
                    print(str(f.format(k.split('.')[0], k.split('.')[1], v.to_dict())))
        else:
            for k, v in models.storage.all().items():
                print(str(f.format(k.split('.')[0], k.split('.')[1], v.to_dict())))

    def do_destroy(self, args):
            """Deletes an instance based on the class and id"""
            args = shlex.split(args)
            if len(args) == 0:
                print("** class name missing **")
            elif args[0] in classes:
                if len(args) > 1:
                    key = args[0] + "." + args[1]
                    if key in models.storage.all():
                        models.storage.all().pop(key)
                        models.storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")

    def do_update(self, args):
        """Update an instance based on the class name, id, attribute & value"""
        args = shlex.split(args)
        strings = ["thread_id", "post_content", "url_plaintext"]
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            if args[0] == "Place":
                                if args[2] in integers:
                                    try:
                                        args[3] = str(args[3])
                                    except:
                                        args[3] = "ERROR NO STRING FILESTORAGE"
                            setattr(models.storage.all()[key], args[2], args[3])
                            models.storage.all()[key].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
