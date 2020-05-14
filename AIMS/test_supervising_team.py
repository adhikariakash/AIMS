import sqlite3
import mock

from AIMS.SupervisingTeam import supervising_team


class TestSupervisingTeam:

    @mock.patch('AIMS.SupervisingTeam.repo')
    @mock.patch('AIMS.SupervisingTeam.input')
    def test_report_accident_success(self, input, db):
        input.side_effect = ['40', '20', 'fire breakout', 'root cause', 'feedback']
        db.sql_connection.cursor.execute.fetchall.return_value = [()]
        assert supervising_team("UUID").report_accident() == True

    @mock.patch('AIMS.SupervisingTeam.repo')
    @mock.patch('AIMS.SupervisingTeam.input')
    def test_report_accident_success_injured_people(self, input, db):
        input.side_effect = ['40A', '40', '20', 'fire breakout', 'root cause', 'feedback']
        db.sql_connection.cursor.execute.fetchall.return_value = [()]
        assert supervising_team("UUID").report_accident() == True

    @mock.patch('AIMS.SupervisingTeam.repo')
    @mock.patch('AIMS.SupervisingTeam.input')
    def test_report_accident_success_dead_people(self, input, db):
        input.side_effect = ['40', '20A', '20', 'fire breakout', 'root cause', 'feedback']
        db.sql_connection.cursor.execute.fetchall.return_value = [()]
        assert supervising_team("UUID").report_accident() == True

    @mock.patch('AIMS.SupervisingTeam.repo')
    @mock.patch('AIMS.SupervisingTeam.input')
    def test_report_accident_success_short_description(self, input, db):
        input.side_effect = ['40', '20', '', 'fire breakout', 'root cause', 'feedback']
        db.sql_connection.cursor.execute.fetchall.return_value = [()]
        assert supervising_team("UUID").report_accident() == True

    @mock.patch('AIMS.SupervisingTeam.repo')
    @mock.patch('AIMS.SupervisingTeam.input')
    def test_report_accident_success_root_cause(self, input, db):
        input.side_effect = ['40', '20', 'fire breakout', '200', 'root cause', 'feedback']
        db.sql_connection.cursor.execute.fetchall.return_value = [()]
        assert supervising_team("UUID").report_accident() == True

    @mock.patch('AIMS.SupervisingTeam.repo')
    @mock.patch('AIMS.SupervisingTeam.input')
    def test_report_accident_success_feedback(self, input, db):
        input.side_effect = ['40', '20', 'fire breakout', 'root cause', '200', 'feedback']
        db.sql_connection.cursor.execute.fetchall.return_value = [()]
        assert supervising_team("UUID").report_accident() == True

    @mock.patch('AIMS.SupervisingTeam.repo.sql_connection', side_effect=sqlite3.Error)
    def test_report_accident_failure(self, db):
        assert supervising_team("d7807f77-ea14-4519-8f03-ef5e39be7e31").report_accident() == False

    @mock.patch('AIMS.SupervisingTeam.supervising_team.report_accident')
    @mock.patch('AIMS.SupervisingTeam.repo')
    def test_check_complain_exist_success_report_empty(self, db, report_accident):
        report_accident.return_value = True
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value.fetchall.side_effect = [["aka"], []]
        assert supervising_team("UUID").check_complain_exist() == True

    @mock.patch('AIMS.SupervisingTeam.repo')
    def test_check_complain_exist_success(self, db):
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value.fetchall.return_value = [['aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa'],
                                                              ['aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa']]
        assert supervising_team("UUID").check_complain_exist() == False

    @mock.patch('AIMS.SupervisingTeam.repo.sql_connection', side_effect=sqlite3.Error)
    def test_check_complain_exist_failure(self, db):
        assert supervising_team("UUID").check_complain_exist() == False

    @mock.patch('AIMS.SupervisingTeam.supervising_team.check_complain_exist')
    @mock.patch('AIMS.SupervisingTeam.input')
    def test_selection_choice_1(self, input, check):
        check.return_value = True
        input.side_effect = ['1', '2']
        assert supervising_team("UUID").selection() == True

    @mock.patch('AIMS.SupervisingTeam.input')
    def test_selection_choice_2(self, input):
        input.side_effect = ['2']
        assert supervising_team("UUID").selection() == True

    @mock.patch('AIMS.SupervisingTeam.input')
    def test_selection_choice_2(self, input):
        input.side_effect = ['234','2']
        assert supervising_team("UUID").selection() == True