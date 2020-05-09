import datetime
import uuid

import AIMS.Repository as repo
from sqlite3 import Error

connection = repo.sql_connection()


class admin:
    def create_member(self):
        print("Creating new member")
        username = self.input_username()
        password = self.input_password()
        created_at = datetime.datetime.today()
        role_id = str(uuid.uuid4())
        working_zone = input("Insert member's working zone: ")
        try:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO login(username,password,role_name,role_id,created_at,delete_value) VALUES(\'{}\',\'{}\',"
                "\'{}\', ""\'{}\',\'{}\',\'{}\')".format(username, password, 'employee', role_id, created_at, 'False'))
            cursor.execute(
                "INSERT INTO employee(role_id,working_zone) VALUES(\'{}\',\'{}\')".format(role_id, working_zone))
            connection.commit()
            cursor.close()
        except Error as e:
            print(e)

    def input_username(self):
        username = input("Enter username of member: ")
        connection = repo.sql_connection()
        cursor = connection.cursor()
        if username:
            if cursor.execute("select * from login where username = \'{}\'".format(username)).fetchone():
                print("username already exists....try again")
                self.input_username()
            print("Username created")
            connection.commit()
            cursor.close()
            return username
        print("Username cannot be empty")
        self.input_username()

    def input_password(self):
        password = input("Enter your password...should be atleast of length 6: ")
        if password and len(password) >= 6:
            re_check = input('Re-enter your password: ')
            if password == re_check:
                print("Password created successfully")
                return password
            self.input_password()
        print("Either your password is empty or less than 6 characters....try again")
        self.input_password()


admin().create_member()
