from AIMS.Login import login


class dashboard:
    """
    THis is
    """

    def main(self):
        """
        This is like main page off console will give different options
        :return: True/False
        """
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
                login().check_admin()
            elif ch == '2':
                login().check_team()
            elif ch == '3':
                login().check_emp()
            elif ch == '4':
                return True
            else:
                print("Invalid choice")

if __name__ == '__main__':
    dashboard().main()
