import sqlite3
import mock

from AIMS.Login import login


class TestLogin:
    @mock.patch('AIMS.Login.Fernet')
    @mock.patch('AIMS.Login.repo')
    @mock.patch('AIMS.Login.input')
    def test_check_admin_wrong_password(self, input, db, fernet):
        input.side_effect = ['admin', 'pass']
        fernet.cipher_suite.return_value.decrypt.return_value = "pass"
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value.fetchall.return_value = [["pass", "pass"]]
        assert login().check_admin() == False

    @mock.patch('AIMS.Login.Fernet')
    @mock.patch('AIMS.Login.repo')
    @mock.patch('AIMS.Login.input')
    def test_check_admin_username_not(self, input, db, fernet):
        input.side_effect = ['admin', 'pass']
        fernet.cipher_suite.return_value.decrypt.return_value = "pass"
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value.fetchall.return_value = []
        assert login().check_admin() == False

    @mock.patch('AIMS.Login.Fernet')
    @mock.patch('AIMS.Login.repo')
    @mock.patch('AIMS.Login.input')
    def test_check_admin_username_empty(self, input, db, fernet):
        input.side_effect = ['', '']
        fernet.cipher_suite.return_value.decrypt.return_value = "pass"
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value.fetchall.return_value = []
        assert login().check_admin() == False

    @mock.patch('AIMS.Login.Fernet')
    @mock.patch('AIMS.Login.repo.sql_connection', side_effect=sqlite3.Error)
    @mock.patch('AIMS.Login.input')
    def test_check_admin_failure(self, input, db, fernet):
        input.side_effect = ['admin', 'pass']
        assert login().check_admin() == False

    @mock.patch('AIMS.Login.Fernet')
    @mock.patch('AIMS.Login.repo')
    @mock.patch('AIMS.Login.input')
    def test_check_emp_username_empty(self, input, db, fernet):
        input.side_effect = ['', '']
        fernet.cipher_suite.return_value.decrypt.return_value = "pass"
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value.fetchall.return_value = []
        assert login().check_emp() == False

    @mock.patch('AIMS.Login.Fernet')
    @mock.patch('AIMS.Login.repo')
    @mock.patch('AIMS.Login.input')
    def test_check_emp_username_not_found(self, input, db, fernet):
        input.side_effect = ['a', 'a']
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value.fetchall.return_value = []
        assert login().check_emp() == False

    @mock.patch('AIMS.Login.Fernet')
    @mock.patch('AIMS.Login.repo.sql_connection', side_effect=sqlite3.Error)
    @mock.patch('AIMS.Login.input')
    def test_check_emp_failure(self, input, db, fernet):
        input.side_effect = ['admin', 'pass']
        assert login().check_emp() == False

    @mock.patch('AIMS.Login.Fernet')
    @mock.patch('AIMS.Login.repo')
    @mock.patch('AIMS.Login.input')
    def test_check_emp_wrong_password(self, input, db, fernet):
        input.side_effect = ['a', 'a']
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value.fetchall.return_value = [("aa")]
        assert login().check_emp() == False

    @mock.patch('AIMS.Login.Fernet')
    @mock.patch('AIMS.Login.repo')
    @mock.patch('AIMS.Login.input')
    def test_check_team_username_empty(self, input, db, fernet):
        input.side_effect = ['', '']
        fernet.cipher_suite.return_value.decrypt.return_value = "pass"
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value.fetchall.return_value = []
        assert login().check_team() == False

    @mock.patch('AIMS.Login.Fernet')
    @mock.patch('AIMS.Login.repo')
    @mock.patch('AIMS.Login.input')
    def test_check_team_username_not_found(self, input, db, fernet):
        input.side_effect = ['a', 'a']
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value.fetchall.return_value = []
        assert login().check_team() == False

    @mock.patch('AIMS.Login.Fernet')
    @mock.patch('AIMS.Login.repo.sql_connection', side_effect=sqlite3.Error)
    @mock.patch('AIMS.Login.input')
    def test_check_team_failure(self, input, db, fernet):
        input.side_effect = ['admin', 'pass']
        assert login().check_team() == False

    @mock.patch('AIMS.Login.Fernet')
    @mock.patch('AIMS.Login.repo')
    @mock.patch('AIMS.Login.input')
    def test_check_team_wrong_password(self, input, db, fernet):
        input.side_effect = ['a', 'a']
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value.fetchall.return_value = [("aa", "", "", "", "", "", "")]
        assert login().check_team() == False


