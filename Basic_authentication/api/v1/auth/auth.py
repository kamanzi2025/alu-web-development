#!/usr/bin/env python3
"""Auth module that defines the template class for API authentication."""
from typing import List, TypeVar
from flask import request


class Auth():
    """Template class for every authentication system of the API."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Return True if the path requires authentication, else False."""
        if path is None or not excluded_paths:
            return True
        if not path.endswith('/'):
            path += '/'
        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """Return the value of the Authorization header of the request."""
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """Return the current user of the request; None in this template."""
        return None
