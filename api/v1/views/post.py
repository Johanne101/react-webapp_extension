#!/usr/bin/python3
""" Views for handling post metadata """
from models import storage
from models.post import Post
from api.v1.views import app_views
from flask import jsonify, abort, make_response, request

@app_views.route('/posts', methods=['GET'], strict_slashes=False)
def post_stat():
    """ Basic Post status get """
    return jsonify({"post_status": "OK"})

@app_views.route('/posts/<post_id>', methods=['GET'], strict_slashes=False)
def get_post(post_id):
    """ Will obtain post metadata """
    post = storage.get(Post, post_id)
    if not post:
        abort(404)

    return jsonify(post.to_dict())

@app_views.route('/posts', methods=['POST'], strict_slashes=False)
def new_post():
    """ Will create a thread """
    if not request.get_json():
        abort(400, description="Invalid input, Non-JSON")

    if 'thread_id' not in request.get_json():
        abort(400, description="No thread_id provided")
    if 'user_id' not in request.get_json():
        abort(400, description="No user_id provided")
    if 'post_content' not in request.get_json():
        abort(400, description="No post_content provided")
    data = request.get_json()
    data['reload'] = False
    new_post = Post(**data)
    new_post.save()
    return make_response(jsonify(new_post.to_dict()), 201)
