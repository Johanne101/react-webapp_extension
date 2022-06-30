#!/usr/bin/python3
""" API Backend for user feedback application """

from flask import Flask, jsonify, request
from api.v1.views import app_views
from models import storage

app = Flask(__name__)
app.register_blueprint(app_views)

if __name__ == '__main__':
    print(app_views)
    app.run()
