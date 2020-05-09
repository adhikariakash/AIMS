import sqlite3
from sqlite3 import Error


def sql_connection():
    try:
        connection = sqlite3.connect('AIMS')
        return connection
    except Error as e:
        print(e)
        return False
