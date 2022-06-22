#!/usr/bin/python3
""" Contains Post Class """

import models
from models.basemodel import Basemodel
from models.thread import Thread
from os import getenv


class Post(Basemodel):
    """ Post Content meant to be requested in batches """

    post_total = 0

    def __init__(self, *args, **kwargs):
        """ initializes values on creation """
        super.__init__(*args, **kwargs)
        self.user_id = ""
        self.post_content = ""
        self.thread_id = ""
