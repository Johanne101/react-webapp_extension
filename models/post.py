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
        try_thread = models.storage.get(Thread, kwargs["thread_id"])
        if kwargs['reload'] is None:
            if try_thread is None:
                print("ERROR: THREAD NOT FOUND")
            else:
                try_thread.post_count += 1
        super().__init__(*args, **kwargs)
