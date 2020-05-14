import uuid
import AIMS.Repository as repo
from sqlite3 import Error
import datetime


class employee:
    """
    This is Employee Class
    """
    def __init__(self, role_id):
        """
        Initializer method
        :param role_id:
        """
        self.role_id = role_id

    def selection(self):
        """
        Selection of features for Employee
        :return: True/False
        """
        ch = ''
        while ch != 3:
            ch = input("choose 1.File complain 2.Show complain 3.Exit: ")
            if ch == '1':
                self.complain_file()
            elif ch == '2':
                self.show_complain()
            elif ch == '3':
                return True
            else:
                print("Invalid choice")

    def complain_file(self):
        """
        Complain a file against any incident happened
        :return: True/False
        """
        try:
            print("file your complain here")
            created_at = datetime.datetime.today()
            complain_id = str(uuid.uuid4())
            description = input("Enter all the details about incident please: ")
            working_zone = input("Enter working zone where incident happened: ")
            if description and working_zone:
                accident_list = ["fire breakout", "gas leakage", "infrastructure damages", "other"]
                complain_type = None
                print("Choose complain type \n 1.Fire Breakout 2.Gas Leakage 3.Infrastructure Damages 4.Other")
                ch = (input("Write your complain type: ")).lower()
                while not ch in accident_list:
                    print("Entered complain type doesnt exist")
                    ch = (input("Write your complain type: ")).lower()
                connection = repo.sql_connection()
                cursor = connection.cursor()
                cursor.execute(
                    "INSERT into complains(complain_id,description,working_zone,role_id,status,created_at,"
                    "delete_value,verdict,complain_type) Values(\'{}\',\'{}\', "
                    "\'{}\', \'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')".format(complain_id, description, working_zone,
                                                                                self.role_id,
                                                                                "open", created_at, "False", 'False',
                                                                                complain_type))
                connection.commit()
                cursor.close()
                print("Your complain is filed")
                return True
            print("Description or working zone is empty..Try again")
            return False
        except Error as e:
            print(e)
            return False

    def show_complain(self):
        """
        Show list of complain filed
        :return: True/False
        """
        try:
            connection = repo.sql_connection()
            cursor = connection.cursor()
            records = cursor.execute(
                "select complain_id,description,working_zone,status,created_at from complains where delete_value = "
                "\'False\' and role_id = \'{}\'".format(self.role_id)).fetchall()
            if records:
                print("All complains")
                for row in records:
                    print("Complain_id= ", row[0])
                    print("Description= ", row[1])
                    print("Working_zone= ", row[2])
                    print("Status= ", row[3])
                    print("Date of incident= ", row[4])
                    print("-----------------------")
                return True
            print("No complains found")
            return True
        except Error as e:
            print(e)
            return False
