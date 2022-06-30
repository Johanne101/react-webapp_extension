#!/usr/bin/python3
""" Index """
from models.thread import Thread
from models.post import Post
from models import storage
from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Basic Status return route """
    return jsonify({"status": "OK"})
