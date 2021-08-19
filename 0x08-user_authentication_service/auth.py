#!/usr/bin/env python3
"""Hash password module"""


import bcrypt
from db import DB
from flask import request
import uuid
from user import User
from sqlalchemy.orm.exc import NoResultFound
from typing import Union


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """init method"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """to register a user, checking if email already exists"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            password_hashed = _hash_password(password)
            user = self._db.add_user(email, password_hashed)
            return user
        else:
            raise ValueError('User {email} already exists')

    def valid_login(self, email: str, password: str) -> bool:
        try:
            user = self._db.find_user_by(email=email)
            if user:
                p = password.encode()
                return bcrypt.checkpw(p, user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """Get session ID"""
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> Union[str, None]:
        """"Find user by session ID"""
        try:
            user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None
        return user

    def destroy_session(user_id: int) -> None:
        """Destroy session"""
        try:
            user = self._db.find_user_by(id=user_id)
            self._db.update_user(user.id, session_id=None)
            return None
        except NoResultFound:
            return None


def _hash_password(password: str) -> bytes:
    """Method to hash password"""
    p = password.encode()
    salt = bcrypt.gensalt()
    to_hash = bcrypt.hashpw(p, salt)
    return to_hash


def _generate_uuid() -> str:
    """Generate UUIDs"""
    return str(uuid.uuid4())
