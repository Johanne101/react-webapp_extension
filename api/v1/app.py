#!/usr/bin/python3
""" API Backend for user feedback application """

import sys
print(sys.path)
from flask import Flask, jsonify, request
from models import storage

app = Flask(__name__)

@app.route('/api/status', methods=['GET'])
def status():
    return jsonify({"status": 200})

if __name__ == '__main__':
    app.run()
