#!/usr/bin/python3
""" Contains Thread Class """

from models.basemodel import BaseModel
import models
from os import getenv
import uuid

class Thread(BaseModel):
    """ Thread metadata to be requested before Thread content """
    
    poster_total = 0
    thread_total = 0

    def __init__(self, *args, **kwargs):
        """ initializes values """
        err_string = "ERROR: NO [[[{}]]] provided"
        att_str_list = ["url"]
        for att in att_str_list:
            if att not in kwargs:
                print(err_string.format(att))
        if "url" in kwargs:
            kwargs['url_plaintext'] = kwargs['url']
        self.url_plaintext = ""
        self.url_hash = ""
        self.unique_ip_count = 0
        self.post_count = 0
        self.ratingPOS = 0
        self.ratingNEG = 0
        self.unique_ip_list = []
        self.post_list = []
        super().__init__(**kwargs)
