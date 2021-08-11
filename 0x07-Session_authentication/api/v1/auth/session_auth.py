#!/usr/bin/env python3
"""
validate if everything inherits correctly
without any overloading
"""

from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """authentication mechanism"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a Session ID for a user_id"""
        if user_id is None or type(user_id) != str:
            return None
        else:
            session_id = str(uuid.uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """returns a User ID based on a Session ID"""
        if session_id is None or type(session_id) != str:
            return None
        else:
            x = self.user_id_by_session_id.get(session_id)
            return x

    def current_user(self, request=None):
        """overload that returns a User instance based on a cookie"""
        s_cookie = self.session_cookie(request)
        user_id_cookie = self.user_id_for_session_id(s_cookie)
        user = User.get(user_id_cookie)
        return user
