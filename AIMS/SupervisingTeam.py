import uuid
import AIMS.Repository as repo
from sqlite3 import Error
from AIMS.Employee import employee
import datetime

connection = repo.sql_connection()


class supervising_team:

    def __init__(self, team_id):
        self.team_id = team_id

    def selection(self):
        ch = ''
        while ch != '2':
            ch = input("1.Make your Report 2.Exit: ")
            if ch == '1':
                self.report_accident()
            else:
                print("Invalid choice")

    def report_accident(self):
        try:
            cursor = connection.cursor()
            complain_id = cursor.execute(
                "select complain_id from supervising_team where team_id = \'{}\'".format(self.team_id)).fetchall()[0][0]
            date_of_accident = cursor.execute(
                "select created_at from complains where complain_id = \'{}\'".format(complain_id)).fetchall()[0][0]
        except Error as e:
            print(e)
            return False
        report_id = str(uuid.uuid4())
        created_at = datetime.datetime.today()
        injured_people = ''
        dead_people = ''
        while not injured_people.isnumeric():
            injured_people = (input("Enter how many people got injured : "))
        while not dead_people.isnumeric():
            dead_people = (input("How many lives we have lost : "))
        short_description = input("Please give short description of the incident happened: ")
        while not short_description:
            short_description = input("Please give the right short description of the incident happened: ")
        root_cause = input("Enter the root cause of the incident: ")
        while not "".join(root_cause.split(" ")).isprintable():
            root_cause = input("Enter the root cause of the incident: ")
        feedback = input("Enter your feedback: ")
        while not "".join(feedback.split(" ")).isprintable():
            feedback = input("Enter your feedback: ")
        try:
            cursor.execute(
                "Insert into final_report(report_id,complain_id,feedback,date_of_accident,injured_people,dead_people,"
                "short_description,root_cause,created_at) VALUES(\'{}\',\'{}\',\'{}\',\'{}\',{},{},\'{}\',\'{}\',\'{}\')".format(
                    report_id, complain_id, feedback, date_of_accident, injured_people, dead_people,
                    short_description,
                    root_cause, created_at))
            connection.commit()
            cursor.close()
            return True
        except Error or IOError as e:
            print(e)
            return False
