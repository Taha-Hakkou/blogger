#!/usr/bin/python3
""" Index """
from models.user import User
#from models import storage
from api.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of API """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def number_objects():
    """ Retrieves the number of each objects by type """
    num_objs = {'users': 1,
                'posts': 0}
    # storage.count(User)
    return jsonify(num_objs)