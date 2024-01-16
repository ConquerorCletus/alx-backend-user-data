#!/usr/bin/env python3
"""
Index module for the API
"""
from flask import Blueprint, jsonify, abort

app_views = Blueprint('app_views', __name__)


@app_views.route('/api/v1/unauthorized', methods=['GET'])
def unauthorized_route():
    """ Endpoint to test unauthorized error handling
    """
    abort(401)
