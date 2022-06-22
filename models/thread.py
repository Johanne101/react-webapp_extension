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
        super.__init__(args, kwargs)
        self.url_plaintext = ""
        self.unique_ip_count = 0
        self.post_count = 0
        self.ratingPOS = 0
        self.ratingNEG = 0
        self.unique_ip_list = []
        self.post_list = []

#URL HASH
#TOTAL NUMBER OF UNIQUE IP HASHS
#LIST OF IP HASHES
