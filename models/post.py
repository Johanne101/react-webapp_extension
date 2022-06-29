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
        err_string = "ERROR: NO [[[{}]]] provided"
        att_str_list = ["post_content", "thread_id", "user_id"]
        for att in att_str_list:
            if att not in kwargs:
                print(err_string.format(att))

        super().__init__(*args, **kwargs)
