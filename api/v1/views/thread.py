#!/usr/bin/python3
""" Views for handling thread metadata """
from models import storage
from models.thread import Thread
from api.v1.views import app_views
from flask import jsonify, abort, make_response, request

@app_views.route('/threads', methods=['GET'], strict_slashes=False)
def thread_stat():
    """ Basic Status return route """
    return jsonify({"thread_status": "OK"})

@app_views.route('/threads/<thread_id>', methods=['GET'], strict_slashes=False)
def get_thread(thread_id):
    """ Will obtain thread metadata """
    thread = storage.get(Thread, thread_id)
    if not thread:
        abort(404)

    return jsonify(thread.to_dict())

@app_views.route('/thread_id/<thread_url>', methods=['GET'], strict_slashes=False)
def get_thread_id(thread_url):
    """ Will obtain thread metadata """
    threads = storage.all(Thread).items()
    if not threads:
        abort(404)

    for i in threads:
        if i[1].url_plaintext == thread_url:
            return jsonify(i[1].id)
    abort(404)

@app_views.route('/thread_new/', methods=['POST'], strict_slashes=False)
def post_thread():
    """ Will create a thread """
    if not request.get_json():
        abort(400, description="Invalid input, Non-JSON")

    if 'target_url' not in request.get_json():
        abort(400, description="No url provided")

    data = request.get_json()
    new_thread = Thread(**data)
    new_thread.save()
    return make_response(jsonify(instance.to_dict()), 201)
