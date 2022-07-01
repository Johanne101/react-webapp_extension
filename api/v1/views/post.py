#!/usr/bin/python3
""" Views for handling post metadata """
from models import storage
from models import post
from api.v1.views import app_views
from flask import jsonify

@app_views.route('/posts', methods=['GET'], strict_slashes=False)
def post_get():
    """ Basic Post get """
    return jsonify({"Post": "yes"})
