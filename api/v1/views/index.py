#!/usr/bin/python3
""" Index """
from models import storage
from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def thread_get():
    """ Basic Status return route """
    return jsonify({"status": "OK"})
