from AIMS.Login import login


class dashboard:

    def main(self):
        print('AIMS(Accident & Incident Management System)')
        ch = ''
        while ch != 4:
            print("MAIN MENU")
            print("1. ADMIN LOGIN")
            print("2. SUPERVISING TEAM LOGIN")
            print("3. EMPLOYEE LOGIN")
            print("4. EXIT")
            print("Select Your Option (1-4)")
            ch = input("Enter your choice: ")
            if ch == '1':
                self.login_admin()
            elif ch == '2':
                self.login_team()
            elif ch == '3':
                self.login_emp()
            elif ch == '4':
                break
            else:
                print("Invalid choice")

    def login_admin(self):
        if login().check_admin():
            print("Enter into admin")
        else:
            self.login_admin()

    def login_team(self):
        if login().check_team():
            print("Enter into team")
        else:
            self.login_team()

    def login_emp(self):
        if login().check_emp():
            print("Enter into emp")
        else:
            self.login_emp()


if __name__ == '__main__':
    dashboard().main()
