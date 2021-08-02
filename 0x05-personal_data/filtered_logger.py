#!/usr/bin/env python3
"""Filtered_logger"""


import logging
import re
from typing import List


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str
                 ) -> str:
    """returns the log message obfuscated"""
    for i in fields:
        log_message = re.sub(f'{i}=.*?{separator}',
                             f'{i}={redaction}{separator}', message)
    return log_message
