#!/usr/bin/python3
""" Contains Thread class """

import models
from models.base_model import BaseModel, Base, hash_func
from os import getenv

class Thread(BaseModel, Base):
    """ Representation of individual thread """
    url_hash = ""
    post_count = ""

    def __init__(self, *args, **kwargs)
        """ Initializes Thread """
        super().__init__(*args, **kwargs)
        if kwargs.get("url", None) and type(self.url) is str:
            self.url_hash = str(hash_func(self.url))
