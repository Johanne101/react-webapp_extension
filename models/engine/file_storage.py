#!/usr/bin/pytho3
"""
Defining FileStorage Class
"""

import json
import os
from models.basemodel import BaseModel
from models.thread import Thread
from models.post import Post

classes = {"BaseModel": BaseModel, "Thread": Thread, "Post": Post}


class FileStorage:
    """
    Class for Serializes and Deserializes
    Class Attributes:
    __file_path - string with JSON file path ('file.json')
    """
    __file_path = "file.json"
    """path to the JSON file"""
    __objects = {}
    """is a dictionary"""

    def all(self, cls=None):
        """returns the dict __objects"""
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def new(self, obj):
        """sets in __objects the key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        """class name of an obj + id"""
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)
            newdic_objs: store the keys and value that will save
                2. It passes trought for each key/val
                3. handels the files/ file handeling
                4. Then open the file path as a json file
                4.a. dumps the encoded data
                5. converts dic object into JSON strin data format
                5.a and writes 'w' to file 'json_f.write(dump(newdic obj))
        """
        newdict_objs = {}
        with open(self.__file_path, 'w') as json_f:
            for key, val in self.__objects.items():
                newdict_objs[key] = val.to_dict()
            json_f.write(json.dumps(newdict_objs))

    def reload(self):
        """deserializes the JSON file to __objects"""
        emptdic_objs = {}
        try:
            with open(self.__file_path, 'r') as json_f:
                emptdict_objs = json.loads(json_f.read())
                post_dict = {}
                for key, val in emptdict_objs.items():
                    if key.split('.')[0] == "Thread":
                        print("LOADED THREAD ({})".format(key.split('.')[1]))
                        new_class = classes[key.split(".")[0]](**val)
                    else:
                        post_dict[key] = val
                for key, val in post_dict.items():
                    if key.split('.')[0] == "Post":
                        print("LOADED POST ({})".format(key.split('.')[1]))
                        new_class = classes[key.split(".")[0]](**val)
        except:
            pass

    def get(self, cls, id):
        try:
            key = cls.__name__ + '.' + id
        except Exception as e:
            return None

        if key in self.__objects:
            return self.__objects[key]
        return None

    def count(self, cls=None):
        return len(self.all(cls))
