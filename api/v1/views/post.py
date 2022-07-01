#!/usr/bin/python3
""" Views for handling post metadata """
from models import storage
from models.post import Post
from api.v1.views import app_views
from flask import jsonify

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
