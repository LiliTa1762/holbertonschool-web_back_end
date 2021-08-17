#!/usr/bin/env python3
"""Hash password module"""


import bcrypt


def _hash_password(password: str) -> bytes:
    """Method to hash password"""
    p = password.encode()
    salt = bcrypt.gensalt()
    to_hash = bcrypt.hashpw(p, salt)
    return to_hash
