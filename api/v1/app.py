#!/usr/bin/python3
""" API Backend for user feedback application """

from flask import Flask, jsonify, request
from api.v1.views import app_views
from models import storage
from models.post import Post
from models.thread import Thread

app = Flask(__name__)
app.register_blueprint(app_views)

if __name__ == '__main__':
    app.run()
