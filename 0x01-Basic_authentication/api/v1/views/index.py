#!/usr/bin/env python3
"""
Index module for the API
"""
from flask import Blueprint, jsonify, abort
from api.v1.views import app_views


@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def unauthorized_route() -> str:
    """ Endpoint to test unauthorized error handling
    """
    abort(401, description='Unauthorized')


@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def forbidden_route() -> str:
    """Handle forbidden access"""
    abort(403, description='forbidden')


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ GET status of the API
    """
    return jsonify({"status": "OK"})
