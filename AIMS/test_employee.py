import sqlite3

import mock

from AIMS.Employee import employee


class TestEmployee:

    @mock.patch('AIMS.Employee.repo.sql_connection')
    @mock.patch('AIMS.Employee.input')
    def test_complain_file_success(self, input, db):
        mocksql = mock.Mock()
        db.cursor.return_value = mocksql
        mocksql.execute.return_value = mocksql
        input.side_effect = ['description', 'A', 'fire breakout']
        assert employee("d7807f77-ea14-4519-8f03-ef5e39be7e31").complain_file() == True

    @mock.patch('AIMS.Employee.repo.sql_connection')
    @mock.patch('AIMS.Employee.input')
    def test_complain_file_description_empty(self, input, db):
        mocksql = mock.Mock()
        db.cursor.return_value = mocksql
        mocksql.execute.return_value = mocksql
        input.side_effect = ['', 'A', 'fire breakout']
        assert employee("d7807f77-ea14-4519-8f03-ef5e39be7e31").complain_file() == False

    @mock.patch('AIMS.Employee.repo.sql_connection')
    @mock.patch('AIMS.Employee.input')
    def test_complain_file_wrong_accident_type(self, input, db):
        mocksql = mock.Mock()
        db.cursor.return_value = mocksql
        mocksql.execute.return_value = mocksql
        input.side_effect = ['description', 'A', 'fire', 'gas leakage']
        assert employee("d7807f77-ea14-4519-8f03-ef5e39be7e31").complain_file() == True

    @mock.patch('AIMS.Employee.repo.sql_connection', side_effect=sqlite3.Error)
    @mock.patch('AIMS.Employee.input')
    def test_complain_file_failure(self, input, db):
        input.side_effect = ['description', 'A', 'fire breakout']
        assert employee("d7807f77-ea14-4519-8f03-ef5e39be7e31").complain_file() == False

    @mock.patch('AIMS.Employee.repo')
    def test_show_complain_success(self, db):
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value.fetchall.return_value = [('id', 'description', 'zone', 'status', 'date')]
        assert employee("d7807f77-ea14-4519-8f03-ef5e39be7e31").show_complain() == True

    def test_show_complain_success_no_records(self):
        assert employee("d7807f77-ea14-4519-8f03-ef5e39be7e31").show_complain() == True

    @mock.patch('AIMS.Employee.repo.sql_connection', side_effect=sqlite3.Error)
    def test_show_complain_failure(self, db):
        assert employee("d7807f77-ea14-4519-8f03-ef5e39be7e31").show_complain() == False

    @mock.patch('AIMS.Employee.employee.complain_file')
    @mock.patch('AIMS.Employee.input')
    def test_selection_choice_1(self, input, complain):
        input.side_effect = ['1', '3']
        complain.return_value = None
        assert employee("d7807f77-ea14-4519-8f03-ef5e39be7e31").selection() == True

    @mock.patch('AIMS.Employee.employee.show_complain')
    @mock.patch('AIMS.Employee.input')
    def test_selection_choice_2(self, input, complain):
        input.side_effect = ['2', '3']
        complain.return_value = None
        assert employee("d7807f77-ea14-4519-8f03-ef5e39be7e31").selection() == True

    @mock.patch('AIMS.Employee.employee.show_complain')
    @mock.patch('AIMS.Employee.input')
    def test_selection_choice_else(self, input, complain):
        input.side_effect = ['aka', '3']
        complain.return_value = None
        assert employee("d7807f77-ea14-4519-8f03-ef5e39be7e31").selection() == True
