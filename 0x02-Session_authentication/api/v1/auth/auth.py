#!/usr/bin/env python3
"""module contains the auth Class"""
from flask import request
from typing import List, TypeVar


class Auth():
    """Authentication class."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Require auth public method."""
        if path is None:
            return True

        if excluded_paths is None or excluded_paths == []:
            return True

        path = path.rstrip('/') + '/'

        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """Authorization header public method"""
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """Current user method"""
        return None
