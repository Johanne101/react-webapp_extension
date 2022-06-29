#!/usr/bin/python3
""" Contains Post Class """

import models
from models.basemodel import BaseModel
from models.thread import Thread
from os import getenv


class Post(BaseModel):
    """ Post Content meant to be requested in batches """

    def __init__(self, *args, **kwargs):
        """ initializes values on creation """
        err_string = "ERROR: NO [[[{}]]] provided"
        att_str_list = ["post_content", "thread_id", "user_id"]
        for att in att_str_list:
            if att not in kwargs:
                print(err_string.format(att))
        if kwargs['reload'] is False:
            try_thread = models.storage.get(Thread, kwargs["thread_id"])
            if try_thread is None:
                print("ERROR: THREAD NOT FOUND")
            else:
                super().__init__(*args, **kwargs)
                try_thread.post_list.append(self.id)
                try_thread.post_count += 1
                if self.user_id not in try_thread.unique_ip_list:
                    try_thread.unique_ip_list.append(self.user_id)
                    try_thread.unique_ip_count += 1
        else:
            super().__init__(*args, **kwargs)
        delattr(self, 'reload')
