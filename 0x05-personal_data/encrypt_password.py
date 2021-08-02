#!/usr/bin/env python3
"""Encrypting passwords"""


import bcrypt


def hash_password(password: str) -> bytes:
    """return a salted, hashed password"""
    p = password.encode()
    salt = bcrypt.gensalt()
    to_hash = bcrypt.hashpw(p, salt)
    return to_hash


def is_valid(hashed_password: bytes, password: str) -> bool:
    """check valid password"""
    p = password.encode()
    if bcrypt.checkpw(p, hashed_password):
        return True
    else:
        return False
