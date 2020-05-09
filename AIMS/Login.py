from cryptography.fernet import Fernet
import getpass
import AIMS.Repository as repo
from sqlite3 import Error

connection = repo.sql_connection()
cursor = connection.cursor()


class login:

    def __init__(self):
        try:
            file = open('key.txt', 'rb')
            key = file.read()
            self.cipher_suite = Fernet(key)
            file.close()
        except IOError or FileNotFoundError as e:
            print(e)

    def check(self):
        username = input("Enter your username: ")
        password = getpass.getpass('Enter your password: ')
        try:
            retrieve_password = cursor.execute(
                "select password from login where username = \'{}\'".format(username)).fetchall()
            connection.commit()
            cursor.close()
            if username and password and retrieve_password:
                if password.encode() == self.cipher_suite.decrypt(retrieve_password[0][0].encode()):
                    return "Access granted"
                return "wrong password"
            return "Password or Username is not valid"
        except IOError or getpass.GetPassWarning or Error as e:
            return e


log = login()
print(log.check())
