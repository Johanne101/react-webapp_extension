#!/usr/bin/python3
""" Views for handling thread metadata """
from models import storage
from models import thread
from api.v1.views import app_views
from flask import jsonify

@app_views.route('/threads', methods=['GET'], strict_slashes=False)
def status():
    """ Basic Thread get """
    return jsonify({"Thread": "yes"})
