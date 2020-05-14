from cryptography.fernet import Fernet
import getpass
import AIMS.Repository as repo
from sqlite3 import Error

from AIMS.Admin import admin
from AIMS.Employee import employee as emp
from AIMS.SupervisingTeam import supervising_team


class login:
    """
    This is login class where login function for all the members
    """
    def __init__(self):
        """
        Initialization method
        """
        try:
            file = open('key.txt', 'rb')
            key = file.read()
            self.cipher_suite = Fernet(key)
            file.close()
        except IOError or FileNotFoundError as e:
            print(e)

    def check_admin(self):
        """
        Login for Admin
        :return: True/False
        """
        username = input("Enter your username: ")
        # password = getpass.getpass('Enter your password: ')
        password = input("Enter your password: ")
        if username and password:
            try:
                connection = repo.sql_connection()
                cursor = connection.cursor()
                retrieve_password = cursor.execute(
                    "select * from login where username = \'{}\' and role_name = \'admin\'".format(username)).fetchall()
                connection.commit()
                cursor.close()
                if retrieve_password:
                    if password.encode() == self.cipher_suite.decrypt(retrieve_password[0][1].encode()):
                        admin().select_choice()
                        print("Access granted")
                        return True
                    print("wrong password")
                    return False
                print("Username not found")
                return False
            except Error as e:
                print(e)
                return False
        print("Password or Username is empty")
        return False

    def check_emp(self):
        """
        Login for Employee
        :return: True/False
        """
        username = input("Enter your username: ")
        # password = getpass.getpass('Enter your password: ')
        password = input("Enter your password: ")
        if username and password:
            try:
                connection = repo.sql_connection()
                cursor = connection.cursor()
                retrieve_password = cursor.execute(
                    "select * from login where username = \'{}\' and role_name = \'employee\'".format(
                        username)).fetchall()
                connection.commit()
                cursor.close()
                if retrieve_password:
                    if password.encode() == self.cipher_suite.decrypt(retrieve_password[0][1].encode()):
                        emp(retrieve_password[0][3]).selection()
                        print("Access granted")
                        return True
                    print("wrong password")
                    return False
                print("Username not found")
                return False
            except Error as e:
                print(e)
                return False
        print("Password or Username is empty")
        return False

    def check_team(self):
        """
        Login for Team
        :return: True/False
        """
        team_name = input("Enter your Team name: ")
        # password = getpass.getpass('Enter your team password: ')
        password = input("Enter your password: ")
        if team_name and password:
            try:
                connection = repo.sql_connection()
                cursor = connection.cursor()
                retrieve_password = cursor.execute(
                    "select * from supervising_team where team_name = \'{}\'".format(team_name)).fetchall()
                connection.commit()
                cursor.close()
                if retrieve_password:
                    if password.encode() == self.cipher_suite.decrypt(retrieve_password[0][6].encode()):
                        supervising_team(retrieve_password[0][0]).selection()
                        print("Access granted")
                        return True
                    print("wrong password")
                    return False
                print("Team id not found")
                return False
            except Error as e:
                print(e)
                return False
        print("Password or team name is empty")
        return False
