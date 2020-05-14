import sqlite3
from sqlite3 import Error

from AIMS import script


def sql_connection():
    """
    connection with sql database
    :return: True/False
    """
    try:
        connection = sqlite3.connect('AIMS')
        cursor = connection.cursor()
        cursor.executescript(script.create_table)
        return connection
    except Error as e:
        print(e)
        return False
