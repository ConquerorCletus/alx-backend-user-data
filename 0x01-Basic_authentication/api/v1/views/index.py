#!/usr/bin/env python3
"""
Index module for the API
"""
from flask import Blueprint, jsonify, abort

app_views = Blueprint('app_views', __name__)


@app_views.route('/api/v1/unauthorized', methods=['GET'], strict_slashes=False)
def unauthorized_route() -> str:
    """ Endpoint to test unauthorized error handling
    """
    abort(401, description='Unauthorized')


@app_views.route('/api/v1/forbidden', methods=['GET'], strict_slashes=False)
def forbidden_route() -> str:
    """Handle forbidden access"""
    abort(403, description='forbidden')
