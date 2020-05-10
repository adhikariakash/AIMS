import datetime
import re
import uuid
from cryptography.fernet import Fernet
import getpass

import AIMS.Repository as repo
from sqlite3 import Error

connection = repo.sql_connection()


class admin:
    def __init__(self):
        # ch = ''
        # while ch != 9:
        #     print("GPM MENU")
        #     print("1.ADD MEMBER\t2.UPDATE MEMBER\t3..DELETE MEMBER\t4.")
        #     print("\tSelect Your Option (1-9)")
        #     ch = input()
        #     if ch == '1':
        #         self.createMember()
        #     elif ch == '2':
        #         self.updateMember()
        #     elif ch == '3':
        #         self.deleteMember()
        #     elif ch == '4':
        #         self.assignProjectToMember()
        #     elif ch == '5':
        #         self.updateProjectOfMember()
        #     elif ch == '6':
        #         self.delete_member_from_project()
        #     elif ch == '7':
        #         self.showComplaints()
        #     elif ch == '8':
        #         self.issueJobCard()
        #     elif ch == '9':
        #         break
        #     else:
        #         print("Invalid choice")
        pass

    def create_member(self):
        print("Creating new member")
        username = self.input_username()
        password = self.input_password()
        created_at = datetime.datetime.today()
        role_id = str(uuid.uuid4())
        working_zone = input("Insert member's working zone: ")
        name = ''
        phone_number = ''
        while not name.isalpha():
            name = input("Enter employee name: ")

        while not phone_number.isnumeric():
            phone_number = input("Enter employee phone number: ")

        try:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO login(username,password,role_name,role_id,created_at,delete_value) VALUES(\'{}\',\'{}\',"
                "\'{}\', \'{}\',\'{}\',\'{}\')".format(username, password.decode(), 'employee', role_id, created_at,
                                                       'False'))
            cursor.execute(
                "INSERT INTO employee(role_id,working_zone,name,phone_number,deleted) VALUES(\'{}\',\'{}\',\'{}\',{},"
                "\'{}\')".format(role_id, working_zone, name, phone_number, 'False'))
            connection.commit()
            cursor.close()
        except Error as e:
            print(e)

    def update_member(self):
        print("Updating a member")
        connection = repo.sql_connection()
        cursor = connection.cursor()
        try:
            members = cursor.execute("SELECT * from employee").fetchall()
            if members:
                for member in members:
                    print(
                        "ROLE ID: {} | WORKING_ZONE: {} | NAME: {} | PHONE NUMBER: {}".format(member[0], member[1],
                                                                                              member[2],
                                                                                              member[3]))
                self.is_updated(cursor)
                connection.commit()
                cursor.close()
                return True
            print("No member in the record")
            return False
        except Error as e:
            print(e)
            return False

    def delete_member(self):
        print("Deleting a member")
        connection = repo.sql_connection()
        cursor = connection.cursor()

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
                file = open('key.txt', 'rb')
                key = file.read()
                cipher_suite = Fernet(key)
                file.close()
                password = cipher_suite.encrypt(password.encode())
                print("Password created successfully")
                return password
            self.input_password()
        print("Either your password is empty or less than 6 characters....try again")
        self.input_password()

    def is_updated(self, cursor):
        role_id = input("Select the role id for which you need to update the record: ")
        if role_id and re.match("^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
                                role_id):
            ch = ''
            while ch != '4':
                ch = input("Choose field to be changed: 1.Working zone 2.Name 3.Phone number 4.Exit: ")
                if ch == '1':
                    new_working_zone = input("Enter new working zone: ")
                    cursor.execute(
                        "UPDATE employee SET working_zone = \'{}\' WHERE role_id = \'{}\'".format(new_working_zone,
                                                                                                  role_id))

                elif ch == '2':
                    name = input("Enter new name: ")
                    if "".join(name.split(' ')).isalpha():
                        cursor.execute("UPDATE employee SET name = \'{}\' WHERE role_id = \'{}\'".format(name, role_id))
                    pass
                elif ch == '3':
                    phone_number = input("Enter new phone number: ")
                    if phone_number.isnumeric():
                        cursor.execute(
                            "UPDATE employee SET phone_number = \'{}\' WHERE role_id = \'{}\'".format(phone_number,
                                                                                                      role_id))
                    pass
                else:
                    return
        print("Role id didn't match....try again")
        self.is_updated()


admin().update_member()
