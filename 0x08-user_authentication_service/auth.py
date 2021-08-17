#!/usr/bin/env python3
"""Hash password module"""


import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


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


def _hash_password(password: str) -> bytes:
    """Method to hash password"""
    p = password.encode()
    salt = bcrypt.gensalt()
    to_hash = bcrypt.hashpw(p, salt)
    return to_hash
