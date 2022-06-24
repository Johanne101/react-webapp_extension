#!/usr/bin/python3
""" Contains Post Class """

import models
from models.basemodel import BaseModel
from models.thread import Thread
from os import getenv


class Post(BaseModel):
    """ Post Content meant to be requested in batches """

    post_total = 0

    def __init__(self, *args, **kwargs):
        """ initializes values on creation """
        self.user_id = ""
        self.post_content = ""
        self.thread_id = ""
        super().__init__(*args, **kwargs)
