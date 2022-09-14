#!/usr/bin/env python3
"""
Main file
"""


import re
import logging
from os import environ
import mysql.connector
from typing import List


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ inits self """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ filters the record """
        f = super().format(record)
        return filter_datum(self.fields, self.REDACTION, f, self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ returns the log message obfuscated """
    for field in fields:
        newLog = re.sub(f"(?<={field}=).*?(?={separator})", redaction, message)
    return newLog


def get_logger() -> logging.Logger:
    """ returns a logging.Logger object """
    user_data = logging.getLogger("user_data")
    user_data.setLevel(logging.INFO)
    user_data.propagate = False
    stream = logging.StreamHandler()
    stream.setFormatter(RedactingFormatter(PII_FIELDS))
    user_data.addHandler(stream)
    return user_data


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ connects to mysql database """
    db = mysql.connector.connect(
        host=environ.get("PERSONAL_DATA_DB_HOST"),
        user=environ.get("PERSONAL_DATA_DB_USERNAME"),
        password=environ.get("PERSONAL_DATA_DB_PASSWORD"),
        database=environ.get("PERSONAL_DATA_DB_NAME"))
    return db


def main():
    """ displays info from database """
    logger = get_logger()
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")

    for i in cursor:
        myList = i.items()
        str = "; ".join(f"{tuple[0]}={tuple[1]}" for tuple in myList)
        logger.info(str)

    db.close()


if __name__ == "__main__":
    main()
