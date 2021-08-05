#!/usr/bin/env python3
"""
to manage the API authentication
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """manage the API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """excludes paths"""
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        if path in excluded_paths:
            return False
        for paths in excluded_paths:
            if path == paths[:-1]:
                return False
            else:
                return True

    def authorization_header(self, request=None) -> str:
        """authorization_header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user"""
        return None