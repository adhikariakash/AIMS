import datetime
import re
import uuid
from cryptography.fernet import Fernet
import getpass

import AIMS.Repository as repo
from sqlite3 import Error

connection = repo.sql_connection()


class admin:

    def select_choice(self):
        ch = ''
        while ch != 8:
            print("ADMIN MENU")
            print(
                "1.ADD MEMBER 2.UPDATE MEMBER 3.DELETE MEMBER 4.CREATE TEAM 5.UPDATE TEAM 6.DELETE TEAM 7.GIVE "
                "JUDGEMENT 8.EXIT")
            ch = input("Select Your Option (1-8): ")
            if ch == '1':
                self.create_member()
            elif ch == '2':
                self.update_member()
            elif ch == '3':
                self.delete_member()
            elif ch == '4':
                self.create_team()
            elif ch == '5':
                self.update_team()
            elif ch == '6':
                self.delete_team()
            elif ch == '7':
                self.final_judgement()
            else:
                print("Invalid choice")
        return True

    def create_member(self):
        print("Creating new member")
        username = self.input_username()
        password = self.input_password()
        while not password:
            password = self.input_password()
        created_at = datetime.datetime.today()
        role_id = str(uuid.uuid4())
        working_zone = input("Insert member's working zone: ")
        name = input("Enter employee name: ")
        phone_number = ''
        while not "".join(name.split(' ')).isalpha():
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
            print("New member created")
            return True
        except Error as e:
            print(e)
            return False

    def update_member(self):
        print("Updating a member")
        try:
            connection = repo.sql_connection()
            cursor = connection.cursor()
            members = cursor.execute("SELECT * from employee where deleted = \'False\'").fetchall()
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
        try:
            print("Deleting a member")
            connection = repo.sql_connection()
            cursor = connection.cursor()
            members = cursor.execute("SELECT * from employee where deleted = \'False\'").fetchall()
            if members:
                for member in members:
                    print(
                        "ROLE ID: {} | WORKING_ZONE: {} | NAME: {} | PHONE NUMBER: {}".format(member[0], member[1],
                                                                                              member[2],
                                                                                              member[3]))
                ch = ''
                while ch != '2':
                    ch = input("Choose any option: 1.Choose role id to be deleted 2.Exit: ")
                    if ch == '1':
                        role_id = input("Select the role id for which you need to delete the record: ")
                        if role_id and re.match(
                                "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
                                role_id):
                            cursor.execute("UPDATE employee SET deleted = 'True' WHERE role_id = \'{}\'".format(
                                role_id))
                            cursor.execute(
                                "UPDATE login SET delete_value= 'True',updated_at = \'{}\' WHERE role_id = \'{}\'".format(
                                    datetime.datetime.today(), role_id))
                            connection.commit()
                            cursor.close()
                        else:
                            print('Wrong role id.....try again')
                    elif ch == '2':
                        return True
                    else:
                        print("Invalid choice")
            print("No member in the record")
            return False
        except Error as e:
            print(e)
            return False

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
        re_check = input('Re-enter your password: ')
        if password and len(password) >= 6 and password == re_check:
            file = open('key.txt', 'rb')
            key = file.read()
            cipher_suite = Fernet(key)
            file.close()
            password = cipher_suite.encrypt(password.encode())
            print("Password created successfully")
            return password
        print("Either your password is empty or less than 6 characters....try again")
        return None

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
                    print("Name should only consist of alphabets")
                    pass
                elif ch == '3':
                    phone_number = input("Enter new phone number: ")
                    if phone_number.isnumeric():
                        cursor.execute(
                            "UPDATE employee SET phone_number = \'{}\' WHERE role_id = \'{}\'".format(phone_number,
                                                                                                      role_id))
                    print("Phone number should be only numeric")
                    pass
                else:
                    return
        print("Role id didn't match....try again")
        self.is_updated(cursor)

    def create_team(self):
        try:
            print("Creating a new team to investigate")
            connection = repo.sql_connection()
            cursor = connection.cursor()
            records = cursor.execute(
                "select complain_id,description,working_zone,status,created_at from complains where delete_value = "
                "'False' and status = 'working'".format()).fetchall()
            if records:
                for row in records:
                    print("complain_id= ", row[0])
                    print("Description= ", row[1])
                    print("working_zone= ", row[2])
                    print("status= ", row[3])
                    print("Date of incident= ", row[4])
                    print("-----------------------")
                complain_id = input("Enter the complain id: ")
                while not self.validate_complaintid(complain_id, cursor):
                    complain_id = input("Enter the complain id: ")
            else:
                print("No  complaints available")
                return False
            members = cursor.execute("SELECT * from employee where deleted = \'False\'").fetchall()
            if members:
                print("Available members:")
                for member in members:
                    print(
                        "ROLE ID: {} | WORKING_ZONE: {} | NAME: {} | PHONE NUMBER: {}".format(member[0], member[1],
                                                                                              member[2],
                                                                                              member[3]))
                n = ''
                member_list = ''
                while n != '2':
                    n = input("Enter 1.To add 2.Exit: ")
                    if n == '1':
                        role_id = input("Select the role id of the person to be added in team: ")
                        if self.validate_roleid(role_id, cursor) and role_id not in member_list:
                            member_list = member_list + role_id + ','
                        else:
                            print("Error with the role id.Role id cannot be added....try again")
                    elif n == '2':
                        print("Okay")
                    else:
                        print("Invalid choice")
                team_id = str(uuid.uuid4())
                password = self.input_password()
                while not password:
                    password = self.input_password()
                cursor.execute(
                    "INSERT INTO supervising_team(team_id,role_ids,complain_id,created_at,delete_value,password) VALUES(\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')".format(
                        team_id, member_list,
                        complain_id,
                        str(datetime.datetime.today()),
                        False,
                        password.decode()))
                cursor.execute("UPDATE complains SET status = 'working' WHERE complain_id = \'{}\'".format(complain_id))
                connection.commit()
                cursor.close()
            else:
                print("There are no members to  be added")
                return False
        except Error as e:
            print(e)
            return False

    def update_team(self):
        try:
            print("Updating the team")
            connection = repo.sql_connection()
            cursor = connection.cursor()
            records = cursor.execute(
                "select team_id,complain_id,created_at from supervising_team where delete_value = 'False' ").fetchall()
            if records:
                for record in records:
                    print("Team id: {} | Complain_id: {} | Created at: {}".format(record[0], record[1], record[2]))
                complain_id = input("Select the complain id for which team needs to be updated: ")
                while not self.validate_complaintid(complain_id, cursor):
                    complain_id = input("Wrong complain id.Enter again: ")
                roles_list = cursor.execute(
                    "SELECT role_ids from supervising_team where complain_id=\'{}\'".format(complain_id)).fetchall()[0][
                    0]
                temp_roles_list = roles_list.split(',')
                ch = ''
                while ch != '3':
                    ch = input("Select  any option: 1.To add member 2.Delete member 3.Exit: ")
                    if ch == '1':
                        members = cursor.execute("SELECT * from employee where deleted = \'False\'").fetchall()
                        if members:
                            for member in members:
                                if member[0] not in temp_roles_list:
                                    print(
                                        "ROLE ID: {} | WORKING_ZONE: {} | NAME: {} | PHONE NUMBER: {}".format(member[0],
                                                                                                              member[1],
                                                                                                              member[2],
                                                                                                              member[
                                                                                                                  3]))
                            role_id = input("Select the role id to be added: ")
                            while not self.validate_roleid(role_id, cursor):
                                role_id = input("Entred role id is wrong...enter again: ")
                            roles_list = roles_list + role_id + ','
                            cursor.execute(
                                "UPDATE supervising_team SET role_ids = \'{}\' WHERE complain_id = \'{}\'".format(
                                    roles_list, complain_id))
                            connection.commit()
                            cursor.close()
                            return True
                        print("No member found")
                        return False
                    elif ch == '2':
                        roles_list = cursor.execute(
                            "SELECT role_ids from supervising_team where complain_id=\'{}\'".format(
                                complain_id)).fetchall()[0][0]
                        temp_roles_list = roles_list.split(',')
                        for i in range(len(temp_roles_list) - 1):
                            members = cursor.execute(
                                "SELECT * from employee where deleted = \'False\' and role_id = \'{}\'".format(
                                    temp_roles_list[i])).fetchall()
                            for member in members:
                                print(
                                    "ROLE ID: {} | WORKING_ZONE: {} | NAME: {} | PHONE NUMBER: {}".format(member[0],
                                                                                                          member[1],
                                                                                                          member[2],
                                                                                                          member[
                                                                                                              3]))
                        role_id = input("Select the role_id to be deleted: ")
                        while not self.validate_roleid(role_id, cursor):
                            role_id = input("Entred role id is wrong...enter again: ")
                        temp_roles_list.remove(role_id)
                        new_roles_list = ''
                        for i in range(len(temp_roles_list) - 1):
                            new_roles_list = new_roles_list + temp_roles_list[i] + ','
                        cursor.execute(
                            "UPDATE supervising_team SET role_ids = \'{}\' WHERE complain_id = \'{}\'".format(
                                new_roles_list, complain_id))
                        connection.commit()
                        cursor.close()
                        return True
                    else:
                        print("Invalid choice")
            print("No team found")
            return False
        except Error as e:
            print(e)
            return False

    def delete_team(self):
        try:
            print("Deleting a team")
            connection = repo.sql_connection()
            cursor = connection.cursor()
            records = cursor.execute(
                "select team_id,complain_id,created_at from supervising_team where delete_value = 'False' ").fetchall()
            if records:
                for record in records:
                    print("Team id: {} | Complain_id: {} | Created at: {}".format(record[0], record[1], record[2]))
                complain_id = input("Select the complain id for which team needs to be deleted: ")
                while not self.validate_complaintid(complain_id, cursor):
                    complain_id = input("Wrong complain id.Enter again: ")
                cursor.execute(
                    "UPDATE supervising_team SET delete_value = 'True' WHERE complain_id = \'{}\'".format(complain_id))
                cursor.execute("UPDATE complains SET status = 'open' WHERE complain_id = \'{}\'".format(complain_id))
                connection.commit()
                cursor.close()
                print("Selected team deleted")
                return True
            print("No team found")
            return False
        except Error as e:
            print(e)
            return False

    def validate_roleid(self, role_id, cursor):
        if not role_id:
            return False
        if not cursor.execute(
                "select * from employee where role_id = \'{}\' and deleted = 'False'".format(role_id)).fetchall():
            return False
        if not re.match("^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
                        role_id):
            return False
        return True

    def validate_complaintid(self, complain_id, cursor):
        if not complain_id:
            return False
        if not cursor.execute(
                "select * from complains where complain_id = \'{}\' and delete_value = 'False'".format(
                    complain_id)).fetchall():
            return False
        if not re.match("^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$", complain_id):
            return False
        return True

    def final_judgement(self):
        try:
            connection = repo.sql_connection()
            cursor = connection.cursor()
            reports = cursor.execute("SELECT * from final_report where feedback IS NOT NULL").fetchall()
            if reports:
                for report in reports:
                    print("Report Id: {}".format(report[0]))
                    print("Complain Id: {}".format(report[1]))
                    print("Date of accident: {}".format(report[2]))
                    print("Injured people: {}".format(report[3]))
                    print("Dead people: {}".format(report[4]))
                    print("Short Description: {}".format(report[5]))
                    print("Root Cause: {}".format(report[6]))
                    print("Feedback: {}".format(report[7]))
                    print("----------------------------")
                complain_id = input("Enter the complain id for which you want to give judgement: ")
                while not self.validate_complaintid(complain_id, cursor):
                    print("Entered complain id is wrong")
                    complain_id = input("Enter the complain id for which you want to give judgement: ")
                verdict = input("Give your final verdict: ")
                while not "".join(verdict.split(' ')).isalnum():
                    print("Give a proper verdict")
                    verdict = input("Give your final verdict: ")
                cursor.execute(
                    "UPDATE complains SET status = 'closed',verdict = \'{}\' WHERE complain_id = \'{}\'".format(
                        verdict, complain_id))
                connection.commit()
                cursor.close()
                return True
            print("No report to show")
            return True
        except Error as e:
            print(e)
            return False

# admin().update_member()
# admin().create_member()
# admin().delete_member()
# admin().create_team()
# admin().delete_team()
# admin().update_team()
# admin().final_judgement()
