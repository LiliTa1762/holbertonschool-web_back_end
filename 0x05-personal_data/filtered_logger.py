#!/usr/bin/env python3
"""Filtered_logger"""


import logging
import mysql.connector
import re
from typing import List
import os


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """returns the log message obfuscated"""
    for f in fields:
        message = re.sub(f'{f}=.*?{separator}',
                         f'{f}={redaction}{separator}', message)
    return message


def get_logger() -> logging.Logger:
    """returns a logging.Logger object"""
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = RedactingFormatter(list(PII_FIELDS))
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """connect to secure database"""
    cnx = mysql.connector.connection.MySQLConnection(
          user=os.getenv('PERSONAL_DATA_DB_USERNAME', 'root'),
          password=os.getenv('PERSONAL_DATA_DB_PASSWORD', ''),
          host=os.getenv('PERSONAL_DATA_DB_HOST', 'localhost'),
          database=os.getenv('PERSONAL_DATA_DB_NAME')
          )

    return cnx


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """constructor"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """filter values in incoming log records"""
        message_log = logging.Formatter(self.FORMAT).format(record)
        log_records = filter_datum(self.fields, self.REDACTION,
                                   message_log, self.SEPARATOR)
        return log_records
