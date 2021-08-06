#!/usr/bin/env python3
"""
to manage Basic Auth
"""

from api.v1.auth.auth import Auth
import base64
from typing import List, TypeVar
from models.user import User


class BasicAuth(Auth):
    """manage BasicAuth"""
    def extract_base64_authorization_header(
                                            self,
                                            authorization_header:
                                            str) -> str:
        """returns Base64 part of the Auth header"""
        if authorization_header is None or type(authorization_header) != str:
            return None
        if not authorization_header.startswith("Basic "):
            return None
        else:
            return authorization_header[6:]

    def decode_base64_authorization_header(
                                           self,
                                           base64_authorization_header:
                                           str) -> str:
        """returns the decoded value of a Base64 string"""
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) != str:
            return None
        try:
            x = base64.b64decode(base64_authorization_header).decode('utf-8')
            return x
        except base64.binascii.Error():
            return None

    def extract_user_credentials(
                                 self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """returns the user email and password from the Base64 decoded value"""
        if decoded_base64_authorization_header is None:
            return None, None
        if type(decoded_base64_authorization_header) != str:
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None
        else:
            str1 = " "
            decoded_parts = tuple(
                                  decoded_base64_authorization_header.split
                                  (":", 2))
            return decoded_parts

    def user_object_from_credentials(
                                     self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """returns the User instance based on his email and password"""
        if user_email is None or type(user_email) != str:
            return None
        if user_pwd is None or type(user_pwd) != str:
            return None

        finded_objects = User().search({"email": user_email})
        if not finded_objects:
            return None
        if finded_objects[0].is_valid_password(user_pwd):
            return finded_objects[0]
        else:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """oerloads Auth and retrieves the User instance"""
        if not request:
            return None
