import mock
from AIMS.Dashboard import dashboard
import _sqlite3

class Testdashboard:

    @mock.patch('AIMS.Dashboard.login')
    @mock.patch('AIMS.Dashboard.input')
    def test_main_case1(self, input, login):
        input.side_effect = ['1', '4']
        login.check_admin.return_value = True

        assert dashboard().main() == True

    @mock.patch('AIMS.Dashboard.login')
    @mock.patch('AIMS.Dashboard.input')
    def test_main_case2(self, input, login):
        input.side_effect = ['2', '4']
        login.check_team.return_value = True

        assert dashboard().main() == True

    @mock.patch('AIMS.Dashboard.login')
    @mock.patch('AIMS.Dashboard.input')
    def test_main_case3(self, input, login):
        input.side_effect = ['3', '4']
        login.check_emp.return_value = True

        assert dashboard().main() == True

    @mock.patch('AIMS.Dashboard.input')
    def test_main_invalid_choice(self, input):
        input.side_effect = ['10', '4']

        assert dashboard().main() == True

