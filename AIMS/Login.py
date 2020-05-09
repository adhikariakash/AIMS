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
        except IOError or FileNotFoundError  as e:
            print(e)

    def check(self):
        username = input("Enter your username: ")
        password = getpass.getpass('Enter your password: ')
        if username and password:
            try:
                retrieve_password = cursor.execute(
                    "select password from login where username = \'{}\' and role_name = \'admin\'".format(
                        username)).fetchall()
                connection.commit()
                cursor.close()
                if retrieve_password:
                    if password.encode() == self.cipher_suite.decrypt(retrieve_password[0][0].encode()):
                        return "Access granted"
                    return "wrong password"
                return "Username not found"
            except IOError or getpass.GetPassWarning or Error as e:
                return e
        return "Password or Username is empty"

    def check_employee(self):
        username = input("Enter your username: ")
        password = getpass.getpass('Enter your password: ')
        if username and password:
            try:
                retrieve_password = cursor.execute(
                    "select password from login where username = \'{}\' and role_name = \'employee\'".format(
                        username)).fetchall()
                connection.commit()
                cursor.close()
                if retrieve_password:
                    if password.encode() == self.cipher_suite.decrypt(retrieve_password[0][0].encode()):
                        return "Access granted"
                    return "wrong password"
                return "Username not found"
            except IOError or getpass.GetPassWarning or Error as e:
                return e
        return "Password or Username is empty"

    def check_team(self):
        team_id = input("Enter your team id: ")
        password = getpass.getpass('Enter your team password: ')
        if team_id and password:
            try:
                retrieve_password = cursor.execute(
                    "select password from supervising_team where team_id = \'{}\'".format(team_id)).fetchall()
                connection.commit()
                cursor.close()
                if retrieve_password:
                    if password.encode() == self.cipher_suite.decrypt(retrieve_password[0][0].encode()):
                        return "Access granted"
                    return "wrong password"
                return "Team id not found"
            except IOError or getpass.GetPassWarning or Error as e:
                return e
        return "Team id or password is empty"


log = login()
print(log.check())
