#!/usr/bin/python3
""" API Backend for user feedback application """

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/status', methods=['GET'])
def status():
    return jsonify({"status": 200})

if __name__ == '__main__':
    app.run()
