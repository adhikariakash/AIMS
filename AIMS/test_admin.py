import mock
from AIMS.Admin import admin
import _sqlite3


class Testadmin:

    @mock.patch('AIMS.Admin.admin.create_member')
    @mock.patch('AIMS.Admin.input')
    def test_select_choice1(self, input, cm):
        input.side_effect = ['1', '10']
        cm.return_value = True

        assert admin().select_choice() == True

    @mock.patch('AIMS.Admin.admin.update_member')
    @mock.patch('AIMS.Admin.input')
    def test_select_choice2(self, input, cm):
        input.side_effect = ['2', '10']
        cm.return_value = True

        assert admin().select_choice() == True

    @mock.patch('AIMS.Admin.admin.delete_member')
    @mock.patch('AIMS.Admin.input')
    def test_select_choice3(self, input, cm):
        input.side_effect = ['3', '10']
        cm.return_value = True

        assert admin().select_choice() == True

    @mock.patch('AIMS.Admin.admin.create_team')
    @mock.patch('AIMS.Admin.input')
    def test_select_choice4(self, input, cm):
        input.side_effect = ['4', '10']
        cm.return_value = True

        assert admin().select_choice() == True

    @mock.patch('AIMS.Admin.admin.update_team')
    @mock.patch('AIMS.Admin.input')
    def test_select_choice5(self, input, cm):
        input.side_effect = ['5', '10']
        cm.return_value = True

        assert admin().select_choice() == True

    @mock.patch('AIMS.Admin.admin.delete_team')
    @mock.patch('AIMS.Admin.input')
    def test_select_choice6(self, input, cm):
        input.side_effect = ['6', '10']
        cm.return_value = True

        assert admin().select_choice() == True

    @mock.patch('AIMS.Admin.admin.final_judgement')
    @mock.patch('AIMS.Admin.input')
    def test_select_choice7(self, input, cm):
        input.side_effect = ['7', '10']
        cm.return_value = True

        assert admin().select_choice() == True

    @mock.patch('AIMS.Admin.admin.visualise_data')
    @mock.patch('AIMS.Admin.input')
    def test_select_choice8(self, input, cm):
        input.side_effect = ['8', '10']
        cm.return_value = True

        assert admin().select_choice() == True

    @mock.patch('AIMS.Admin.admin.visualise_accidents')
    @mock.patch('AIMS.Admin.input')
    def test_select_choice9(self, input, cm):
        input.side_effect = ['9', '10']
        cm.return_value = True

        assert admin().select_choice() == True

    @mock.patch('AIMS.Admin.input')
    def test_select_choice_invalid_option(self, input):
        input.side_effect = ['11', '10']

        assert admin().select_choice() == True

    @mock.patch('AIMS.Admin.repo.sql_connection')
    @mock.patch('AIMS.Admin.input')
    @mock.patch('AIMS.Admin.admin.input_username')
    @mock.patch('AIMS.Admin.admin.input_password')
    def test_create_member_success(self, pwd, usr, input, db):
        usr.return_value = 'abcd'
        pwd.return_value = 'xcvb'
        input.side_effect = ['Factory', 'abc', '9897043213']
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        db.cursor.return_value = mocksql
        mocksql.execute.return_value = mocksql

        assert admin().create_member() == True

    @mock.patch('AIMS.Admin.repo.sql_connection')
    @mock.patch('AIMS.Admin.input')
    @mock.patch('AIMS.Admin.admin.input_username')
    @mock.patch('AIMS.Admin.admin.input_password')
    def test_create_member_others_employee_validation_failed(self, pwd, usr, input, db):
        usr.return_value = 'abcd'
        pwd.return_value = 'xcvb'
        input.side_effect = ['Factory', 'ab2c', 'abc', '9897043213']
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        db.cursor.return_value = mocksql
        mocksql.execute.return_value = mocksql

        assert admin().create_member() == True

    @mock.patch('AIMS.Admin.repo.sql_connection')
    @mock.patch('AIMS.Admin.input')
    @mock.patch('AIMS.Admin.admin.input_username')
    @mock.patch('AIMS.Admin.admin.input_password')
    def test_create_member_password_validation_failed(self, pwd, usr, input, db):
        usr.return_value = 'abcd'
        pwd.side_effect = [None, 'abcdefgh']
        input.side_effect = ['Factory', 'ab2c', 'abc', '9897043213']
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        db.cursor.return_value = mocksql
        mocksql.execute.return_value = mocksql

        assert admin().create_member() == True

    @mock.patch('AIMS.Admin.repo.sql_connection')
    @mock.patch('AIMS.Admin.input')
    @mock.patch('AIMS.Admin.admin.input_username')
    @mock.patch('AIMS.Admin.admin.input_password')
    def test_create_member_number_validation_failed(self, pwd, usr, input, db):
        usr.return_value = 'abcd'
        pwd.side_effect = 'abcdefgh'
        input.side_effect = ['Factory', 'abc', 'ab123', '9897067188']
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        db.cursor.return_value = mocksql
        mocksql.execute.return_value = mocksql

        assert admin().create_member() == True

    @mock.patch('AIMS.Admin.repo.sql_connection', side_effect=_sqlite3.Error)
    @mock.patch('AIMS.Admin.input')
    @mock.patch('AIMS.Admin.admin.input_username')
    @mock.patch('AIMS.Admin.admin.input_password')
    def test_create_member_sqllite_error(self, pwd, usr, input, db):
        usr.return_value = 'abcd'
        pwd.return_value = 'akashadhikari'
        input.side_effect = ['Factory', 'ab2c', 'abc', '9897043213']

        assert admin().create_member() == False

    @mock.patch('AIMS.Admin.admin.is_updated')
    @mock.patch('AIMS.Admin.repo')
    def test_update__member_success(self, db, update):
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value = mocksql
        mocksql.fetchall.return_value = [['1915b58c-f7c3-4282-b997-76ef3bf75e71', 'C', 'Akash', '9899999999', 'False'],
                                         ['fwr', 'D', 'VK', '12345890', 'False']]
        update.return_value = mocksql

        assert admin().update_member() == True

    @mock.patch('AIMS.Admin.admin.is_updated')
    @mock.patch('AIMS.Admin.repo')
    def test_update__member_no_members(self, db, update):
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value = mocksql
        mocksql.fetchall.return_value = []
        update.return_value = mocksql

        assert admin().update_member() == False

    @mock.patch('AIMS.Admin.repo.sql_connection', side_effect=_sqlite3.Error)
    def test_update__member_sqlite_error(self, db):
        assert admin().update_member() == False

    @mock.patch('AIMS.Admin.input')
    @mock.patch('AIMS.Admin.repo')
    def test_delete_member(self, db, input):
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value = mocksql
        mocksql.fetchall.return_value = [['1915b58c-f7c3-4282-b997-76ef3bf75e71', 'C', 'Akash', '9899999999', 'False'],
                                         ['fwr', 'D', 'VK', '12345890', 'False']]
        input.side_effect = ['1', '1915b58c-f7c3-4282-b997-76ef3bf75e71', '2']
        mocksql.execute.return_value = mocksql

        assert admin().delete_member() == True

    @mock.patch('AIMS.Admin.input')
    @mock.patch('AIMS.Admin.repo')
    def test_delete_member_invalid_role_id(self, db, input):
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value = mocksql
        mocksql.fetchall.return_value = [['1915b58c-f7c3-4282-b997-76ef3bf75e71', 'C', 'Akash', '9899999999', 'False'],
                                         ['fwr', 'D', 'VK', '12345890', 'False']]
        input.side_effect = ['1', '4', '2']
        mocksql.execute.return_value = mocksql

        assert admin().delete_member() == True

    @mock.patch('AIMS.Admin.input')
    @mock.patch('AIMS.Admin.repo')
    def test_delete_member_invalid_user_choice(self, db, input):
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value = mocksql
        mocksql.fetchall.return_value = [['1915b58c-f7c3-4282-b997-76ef3bf75e71', 'C', 'Akash', '9899999999', 'False'],
                                         ['fwr', 'D', 'VK', '12345890', 'False']]
        input.side_effect = ['5', '2']

        assert admin().delete_member() == True

    @mock.patch('AIMS.Admin.repo')
    def test_delete_member_no_member_data(self, db):
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value = mocksql
        mocksql.fetchall.return_value = []

        assert admin().delete_member() == False

    @mock.patch('AIMS.Admin.repo.sql_connection', side_effect=_sqlite3.Error)
    def test_delete_member_sqlite_error(self, db):
        assert admin().delete_member() == False

    @mock.patch('AIMS.Admin.input')
    @mock.patch('AIMS.Admin.repo')
    def test_input_username(self, db, input):
        input.return_value = 'abcd'
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value = mocksql
        mocksql.fetchone.return_value = []
        # mocksql.fetchone.return_value = ['marcus','gAAAAABeuQUAIlvWQkfnrM6TpLGg7WscPttEWX0T7uvcY3UuCxeMxkIffoOIYm9wUSKlURmFT8YWszSpwKFvghn730P7AwtNxA==','employee','335fb7a4-b6d9-48ac-9a67-b9578d758d00','2020-05-11 13:25:44.334476','2020-05-10 17:05:11.008580','False']

        assert admin().input_username() == 'abcd'

    @mock.patch('AIMS.Admin.input')
    @mock.patch('AIMS.Admin.repo')
    def test_input_username_record_exists(self, db, input):
        input.side_effect = ['abcd', 'abc']
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value = mocksql
        mocksql.fetchone.side_effect = [['marcus',
                                         'gAAAAABeuQUAIlvWQkfnrM6TpLGg7WscPttEWX0T7uvcY3UuCxeMxkIffoOIYm9wUSKlURmFT8YWszSpwKFvghn730P7AwtNxA==',
                                         'employee', '335fb7a4-b6d9-48ac-9a67-b9578d758d00',
                                         '2020-05-11 13:25:44.334476', '2020-05-10 17:05:11.008580', 'False'], []]

        assert admin().input_username() == 'abcd'

    @mock.patch('AIMS.Admin.input')
    @mock.patch('AIMS.Admin.repo')
    def test_input_username_empty_username(self, db, input):
        input.side_effect = [None, 'qwerty']
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value = mocksql
        mocksql.fetchone.return_value = []

        assert admin().input_username() == None

    @mock.patch('AIMS.Admin.input')
    def test_is_updated_success_case1(self, input):
        input.side_effect = ['f3da47ee-937a-4f2d-9728-1bf8aa4a5ed5', '1', 'Factory', '4']
        mocksql = mock.Mock()
        mocksql.execute.return_value = mocksql

        assert admin().is_updated(mocksql) == False

    @mock.patch('AIMS.Admin.input')
    def test_is_updated_success_case2(self, input):
        input.side_effect = ['f3da47ee-937a-4f2d-9728-1bf8aa4a5ed5', '2', 'dummyname', '4']
        mocksql = mock.Mock()
        mocksql.execute.return_value = mocksql

        assert admin().is_updated(mocksql) == False

    @mock.patch('AIMS.Admin.input')
    def test_is_updated_success_case2_invalid_name(self, input):
        input.side_effect = ['f3da47ee-937a-4f2d-9728-1bf8aa4a5ed5', '2', 'dfg345', 'dummyname', '4']
        mocksql = mock.Mock()
        mocksql.execute.return_value = mocksql

        assert admin().is_updated(mocksql) == False

    @mock.patch('AIMS.Admin.input')
    def test_is_updated_success_case3(self, input):
        input.side_effect = ['f3da47ee-937a-4f2d-9728-1bf8aa4a5ed5', '3', '9999999999', '4']
        mocksql = mock.Mock()
        mocksql.execute.return_value = mocksql

        assert admin().is_updated(mocksql) == False

    @mock.patch('AIMS.Admin.input')
    def test_is_updated_success_case3_invalid_phoneno(self, input):
        input.side_effect = ['f3da47ee-937a-4f2d-9728-1bf8aa4a5ed5', '3', 'qwe', '9999999999', '4']
        mocksql = mock.Mock()
        mocksql.execute.return_value = mocksql

        assert admin().is_updated(mocksql) == False

    @mock.patch('AIMS.Admin.input')
    def test_is_updated_success_invalid_roleid(self, input):
        input.side_effect = [None, 'f3da47ee-937a-4f2d-9728-1bf8aa4a5ed5', '3', '9999999999', '4']
        mocksql = mock.Mock()
        mocksql.execute.return_value = mocksql

        assert admin().is_updated(mocksql) == None

    @mock.patch('AIMS.Admin.admin.validate_team_name', return_value=True)
    @mock.patch('AIMS.Admin.admin.input_password')
    @mock.patch('AIMS.Admin.input')
    @mock.patch('AIMS.Admin.repo')
    def test_create_team_success(self, db, input, pwd, vtn):
        data1 = [['125518f2-5908-4cb5-8754-a20aaac8d55b', 'desc', 'Factory', 'open', '2020-05-10 18:31:52.130590'],
                 ['ea384fc3-a083-425e-b80a-ea88827b39df', 'description', 'Warehouse', 'open',
                  '2019-05-10 18:31:52.130590']]
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value = mocksql
        mocksql.fetchall.return_value = data1
        input.side_effect = ['ea384fc3-a083-425e-b80a-ea88827b39df', '1', '5039220d-353d-4ce3-a189-48ec8c1a8566', '2',
                             'dummyteamname']
        pwd.return_value = 'xcvb'

        assert admin().create_team() == True

    @mock.patch('AIMS.Admin.admin.validate_team_name', return_value=True)
    @mock.patch('AIMS.Admin.admin.input_password')
    @mock.patch('AIMS.Admin.input')
    @mock.patch('AIMS.Admin.repo')
    def test_create_team_success_validate_team_id(self, db, input, pwd, vtn):
        data1 = [['125518f2-5908-4cb5-8754-a20aaac8d55b', 'desc', 'Factory', 'open', '2020-05-10 18:31:52.130590'],
                 ['ea384fc3-a083-425e-b80a-ea88827b39df', 'description', 'Warehouse', 'open',
                  '2019-05-10 18:31:52.130590']]
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value = mocksql
        mocksql.fetchall.return_value = data1
        input.side_effect = [None, 'ea384fc3-a083-425e-b80a-ea88827b39df', '1', '5039220d-353d-4ce3-a189-48ec8c1a8566',
                             '2',
                             'dummyteamname']
        pwd.return_value = 'xcvb'

        assert admin().create_team() == True

    @mock.patch('AIMS.Admin.repo')
    def test_create_team_no_complaints(self, db):
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value = mocksql
        mocksql.fetchall.return_value = []

        assert admin().create_team() == False

    @mock.patch('AIMS.Admin.admin.validate_team_name', return_value=True)
    @mock.patch('AIMS.Admin.admin.input_password')
    @mock.patch('AIMS.Admin.input')
    @mock.patch('AIMS.Admin.repo')
    def test_create_team_success_wrong_role_id(self, db, input, pwd, vtn):
        data1 = [['125518f2-5908-4cb5-8754-a20aaac8d55b', 'desc', 'Factory', 'open', '2020-05-10 18:31:52.130590'],
                 ['ea384fc3-a083-425e-b80a-ea88827b39df', 'description', 'Warehouse', 'open',
                  '2019-05-10 18:31:52.130590']]
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value = mocksql
        mocksql.fetchall.return_value = data1
        input.side_effect = [None, 'ea384fc3-a083-425e-b80a-ea88827b39df', '1', None, '1',
                             '5039220d-353d-4ce3-a189-48ec8c1a8566',
                             '2',
                             'dummyteamname']
        pwd.return_value = 'xcvb'

        assert admin().create_team() == True

    @mock.patch('AIMS.Admin.admin.validate_team_name')
    @mock.patch('AIMS.Admin.admin.input_password')
    @mock.patch('AIMS.Admin.input')
    @mock.patch('AIMS.Admin.repo')
    def test_create_team_team_already_exists(self, db, input, pwd, vtn):
        data1 = [['125518f2-5908-4cb5-8754-a20aaac8d55b', 'desc', 'Factory', 'open', '2020-05-10 18:31:52.130590'],
                 ['ea384fc3-a083-425e-b80a-ea88827b39df', 'description', 'Warehouse', 'open',
                  '2019-05-10 18:31:52.130590']]
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value = mocksql
        mocksql.fetchall.return_value = data1
        input.side_effect = ['ea384fc3-a083-425e-b80a-ea88827b39df', '1', '5039220d-353d-4ce3-a189-48ec8c1a8566', '2',
                             None,
                             'dummyteamname']
        vtn.side_effect = [False, True]
        pwd.return_value = 'xcvb'

        assert admin().create_team() == True

    @mock.patch('AIMS.Admin.admin.validate_team_name', return_value=True)
    @mock.patch('AIMS.Admin.admin.input_password')
    @mock.patch('AIMS.Admin.input')
    @mock.patch('AIMS.Admin.repo')
    def test_create_team_invalid_user_choice(self, db, input, pwd, vtn):
        data1 = [['125518f2-5908-4cb5-8754-a20aaac8d55b', 'desc', 'Factory', 'open', '2020-05-10 18:31:52.130590'],
                 ['ea384fc3-a083-425e-b80a-ea88827b39df', 'description', 'Warehouse', 'open',
                  '2019-05-10 18:31:52.130590']]
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value = mocksql
        mocksql.fetchall.return_value = data1
        input.side_effect = ['ea384fc3-a083-425e-b80a-ea88827b39df', '5', '1', '5039220d-353d-4ce3-a189-48ec8c1a8566',
                             '2',
                             'dummyteamname']
        pwd.return_value = 'xcvb'

        assert admin().create_team() == True

    @mock.patch('AIMS.Admin.admin.validate_complaintid', return_value=True)
    @mock.patch('AIMS.Admin.admin.validate_team_name', return_value=True)
    @mock.patch('AIMS.Admin.admin.input_password')
    @mock.patch('AIMS.Admin.input')
    @mock.patch('AIMS.Admin.repo')
    def test_create_team_invalid_teamname(self, db, input, pwd, vtn, vci):
        data1 = [['125518f2-5908-4cb5-8754-a20aaac8d55b', 'desc', 'Factory', 'open', '2020-05-10 18:31:52.130590'],
                 ['ea384fc3-a083-425e-b80a-ea88827b39df', 'description', 'Warehouse', 'open',
                  '2019-05-10 18:31:52.130590']]
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value = mocksql
        mocksql.fetchall.return_value = data1
        input.side_effect = ['ea384fc3-a083-425e-b80a-ea88827b39df', '2',
                             'ghnj78', 'teamA']
        pwd.return_value = 'xcvb'
        assert admin().create_team() == True

    @mock.patch('AIMS.Admin.admin.validate_team_name', return_value=True)
    @mock.patch('AIMS.Admin.admin.input_password')
    @mock.patch('AIMS.Admin.input')
    @mock.patch('AIMS.Admin.repo')
    def test_create_team_invalid_password(self, db, input, pwd, vtn):
        data1 = [['125518f2-5908-4cb5-8754-a20aaac8d55b', 'desc', 'Factory', 'open', '2020-05-10 18:31:52.130590'],
                 ['ea384fc3-a083-425e-b80a-ea88827b39df', 'description', 'Warehouse', 'open',
                  '2019-05-10 18:31:52.130590']]
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value = mocksql
        mocksql.fetchall.return_value = data1
        input.side_effect = ['ea384fc3-a083-425e-b80a-ea88827b39df', '1', '5039220d-353d-4ce3-a189-48ec8c1a8566', '2',
                             'dummyteamname']
        pwd.side_effect = [None, 'xcvb']

        assert admin().create_team() == True

    @mock.patch('AIMS.Admin.admin.validate_complaintid', return_value=True)
    @mock.patch('AIMS.Admin.input')
    @mock.patch('AIMS.Admin.repo')
    def test_create_team_no_member_records(self, db, input, vci):
        data1 = [['125518f2-5908-4cb5-8754-a20aaac8d55b', 'desc', 'Factory', 'open', '2020-05-10 18:31:52.130590'],
                 ['ea384fc3-a083-425e-b80a-ea88827b39df', 'description', 'Warehouse', 'open',
                  '2019-05-10 18:31:52.130590']]
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value = mocksql
        mocksql.fetchall.side_effect = [data1, None]
        input.return_value = 'ea384fc3-a083-425e-b80a-ea88827b39df'

        assert admin().create_team() == False

    @mock.patch('AIMS.Admin.repo.sql_connection', side_effect=_sqlite3.Error)
    def test_create_team_sqlite_error(self, db):
        assert admin().create_team() == False

    @mock.patch('AIMS.Admin.admin.validate_roleid', return_value=True)
    @mock.patch('AIMS.Admin.admin.validate_complaintid', return_value=True)
    @mock.patch('AIMS.Admin.input')
    @mock.patch('AIMS.Admin.repo')
    def test_update_team_success_case1(self, db, input, vci, vri):
        data1 = [('ea384fc3-a083-425e-b80a-ea88827b39df',
                  '125518f2-5908-4cb5-8754-a20aaac8d55b', '2019-05-10 18:31:52.130590')]
        data2 = [('1915b58c-f7c3-4282-b997-76ef3bf75e71'),
                 ('6c35d84e-e198-47ae-8bf8-4131978d806e')]
        data3 = [('335fb7a4-b6d9-48ac-9a67-b9578d758d00', 'C', 'Akash', '9897', 'False')]
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value = mocksql
        mocksql.fetchall.side_effect = [data1, data2, data3]
        input.side_effect = ['3161af3f-b810-46fd-8fca-7ac5e47966e5', '1', 'f3da47ee-937a-4f2d-9728-1bf8aa4a5ed5']

        assert admin().update_team() == True

    @mock.patch('AIMS.Admin.admin.validate_roleid', return_value=True)
    @mock.patch('AIMS.Admin.admin.validate_complaintid')
    @mock.patch('AIMS.Admin.input')
    @mock.patch('AIMS.Admin.repo')
    def test_update_team_success_invalid_complaint_id(self, db, input, vci, vri):
        data1 = [('ea384fc3-a083-425e-b80a-ea88827b39df',
                  '125518f2-5908-4cb5-8754-a20aaac8d55b', '2019-05-10 18:31:52.130590')]
        data2 = [('1915b58c-f7c3-4282-b997-76ef3bf75e71'),
                 ('6c35d84e-e198-47ae-8bf8-4131978d806e')]
        data3 = [('335fb7a4-b6d9-48ac-9a67-b9578d758d00', 'C', 'Akash', '9897', 'False')]
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value = mocksql
        mocksql.fetchall.side_effect = [data1, data2, data3]
        vci.side_effect = [False, True]
        input.side_effect = [None, '3161af3f-b810-46fd-8fca-7ac5e47966e5', '1', 'f3da47ee-937a-4f2d-9728-1bf8aa4a5ed5']

        assert admin().update_team() == True

    @mock.patch('AIMS.Admin.admin.validate_roleid')
    @mock.patch('AIMS.Admin.admin.validate_complaintid', return_value=True)
    @mock.patch('AIMS.Admin.input')
    @mock.patch('AIMS.Admin.repo')
    def test_update_team_success_invalid_role_id(self, db, input, vci, vri):
        data1 = [('ea384fc3-a083-425e-b80a-ea88827b39df',
                  '125518f2-5908-4cb5-8754-a20aaac8d55b', '2019-05-10 18:31:52.130590')]
        data2 = [('1915b58c-f7c3-4282-b997-76ef3bf75e71'),
                 ('6c35d84e-e198-47ae-8bf8-4131978d806e')]
        data3 = [('335fb7a4-b6d9-48ac-9a67-b9578d758d00', 'C', 'Akash', '9897', 'False')]
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value = mocksql
        mocksql.fetchall.side_effect = [data1, data2, data3]
        vri.side_effect = [False, True]
        input.side_effect = ['3161af3f-b810-46fd-8fca-7ac5e47966e5', '1', None, 'f3da47ee-937a-4f2d-9728-1bf8aa4a5ed5']

        assert admin().update_team() == True

    @mock.patch('AIMS.Admin.admin.validate_roleid', return_value=True)
    @mock.patch('AIMS.Admin.admin.validate_complaintid', return_value=True)
    @mock.patch('AIMS.Admin.input')
    @mock.patch('AIMS.Admin.repo')
    def test_update_team_no_members(self, db, input, vci, vri):
        data1 = [('ea384fc3-a083-425e-b80a-ea88827b39df',
                  '125518f2-5908-4cb5-8754-a20aaac8d55b', '2019-05-10 18:31:52.130590')]
        data2 = [('1915b58c-f7c3-4282-b997-76ef3bf75e71'),
                 ('6c35d84e-e198-47ae-8bf8-4131978d806e')]
        data3 = [('335fb7a4-b6d9-48ac-9a67-b9578d758d00', 'C', 'Akash', '9897', 'False')]
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value = mocksql
        mocksql.fetchall.side_effect = [data1, data2, None]
        input.side_effect = ['3161af3f-b810-46fd-8fca-7ac5e47966e5', '1']

        assert admin().update_team() == False

    @mock.patch('AIMS.Admin.admin.validate_roleid', return_value=True)
    @mock.patch('AIMS.Admin.admin.validate_complaintid', return_value=True)
    @mock.patch('AIMS.Admin.input')
    @mock.patch('AIMS.Admin.repo')
    def test_update_team_success_case2(self, db, input, vci, vri):
        data1 = [('ea384fc3-a083-425e-b80a-ea88827b39df',
                  '125518f2-5908-4cb5-8754-a20aaac8d55b', '2019-05-10 18:31:52.130590')]
        data2 = [('1915b58c-f7c3-4282-b997-76ef3bf75e71'),
                 ('6c35d84e-e198-47ae-8bf8-4131978d806e')]
        data3 = [('335fb7a4-b6d9-48ac-9a67-b9578d758d00', 'C', 'Akash', '9897', 'False')]
        data4 = [(('1915b58c-f7c3-4282-b997-76ef3bf75e71,'),
                  ('6c35d84e-e198-47ae-8bf8-4131978d806e'))]
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value = mocksql
        mocksql.fetchall.side_effect = [data1, data2, data4, data3]
        input.side_effect = ['3161af3f-b810-46fd-8fca-7ac5e47966e5', '2', '1915b58c-f7c3-4282-b997-76ef3bf75e71']

        assert admin().update_team() == True

    @mock.patch('AIMS.Admin.admin.validate_roleid')
    @mock.patch('AIMS.Admin.admin.validate_complaintid', return_value=True)
    @mock.patch('AIMS.Admin.input')
    @mock.patch('AIMS.Admin.repo')
    def test_update_team_success_case2_invalid_role_id(self, db, input, vci, vri):
        data1 = [('ea384fc3-a083-425e-b80a-ea88827b39df',
                  '125518f2-5908-4cb5-8754-a20aaac8d55b', '2019-05-10 18:31:52.130590')]
        data2 = [('1915b58c-f7c3-4282-b997-76ef3bf75e71'),
                 ('6c35d84e-e198-47ae-8bf8-4131978d806e')]
        data3 = [('335fb7a4-b6d9-48ac-9a67-b9578d758d00', 'C', 'Akash', '9897', 'False')]
        data4 = [(('1915b58c-f7c3-4282-b997-76ef3bf75e71,'),
                  ('6c35d84e-e198-47ae-8bf8-4131978d806e'))]
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value = mocksql
        mocksql.fetchall.side_effect = [data1, data2, data4, data3]
        vri.side_effect = [False, True]
        input.side_effect = ['3161af3f-b810-46fd-8fca-7ac5e47966e5', '2', None,
                             '1915b58c-f7c3-4282-b997-76ef3bf75e71']

        assert admin().update_team() == True

    @mock.patch('AIMS.Admin.admin.validate_roleid', return_value=True)
    @mock.patch('AIMS.Admin.admin.validate_complaintid', return_value=True)
    @mock.patch('AIMS.Admin.input')
    @mock.patch('AIMS.Admin.repo')
    def test_update_team_success_invalid_user_choice(self, db, input, vci, vri):
        data1 = [('ea384fc3-a083-425e-b80a-ea88827b39df',
                  '125518f2-5908-4cb5-8754-a20aaac8d55b', '2019-05-10 18:31:52.130590')]
        data2 = [('1915b58c-f7c3-4282-b997-76ef3bf75e71'),
                 ('6c35d84e-e198-47ae-8bf8-4131978d806e')]
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value = mocksql
        mocksql.fetchall.side_effect = [data1, data2]
        input.side_effect = ['3161af3f-b810-46fd-8fca-7ac5e47966e5', '5', '3']

        assert admin().update_team() == False

    @mock.patch('AIMS.Admin.repo.sql_connection', side_effect=_sqlite3.Error)
    def test_update_team_sqlite_error(self, db):
        assert admin().update_team() == False

    @mock.patch('AIMS.Admin.admin.validate_complaintid', return_value=True)
    @mock.patch('AIMS.Admin.input')
    @mock.patch('AIMS.Admin.repo')
    def test_delete_team(self, db, input, vci):
        data1 = [('ea384fc3-a083-425e-b80a-ea88827b39df',
                  '125518f2-5908-4cb5-8754-a20aaac8d55b', '2019-05-10 18:31:52.130590')]
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value = mocksql
        mocksql.fetchall.side_effect = data1
        input.return_value = '3161af3f-b810-46fd-8fca-7ac5e47966e5'

        assert admin().delete_team() == True

    @mock.patch('AIMS.Admin.admin.validate_complaintid')
    @mock.patch('AIMS.Admin.input')
    @mock.patch('AIMS.Admin.repo')
    def test_delete_team_invalid_complain_id(self, db, input, vci):
        data1 = [('ea384fc3-a083-425e-b80a-ea88827b39df',
                  '125518f2-5908-4cb5-8754-a20aaac8d55b', '2019-05-10 18:31:52.130590')]
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value = mocksql
        mocksql.fetchall.side_effect = data1
        input.side_effect = [None, '3161af3f-b810-46fd-8fca-7ac5e47966e5']
        vci.side_effect = [False, True]

        assert admin().delete_team() == True

    @mock.patch('AIMS.Admin.admin.validate_complaintid', return_value=True)
    @mock.patch('AIMS.Admin.input')
    @mock.patch('AIMS.Admin.repo')
    def test_delete_team_no_team_record(self, db, input, vci):
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value = mocksql
        mocksql.fetchall.return_value = []

        assert admin().delete_team() == False

    @mock.patch('AIMS.Admin.repo.sql_connection', side_effect=_sqlite3.Error)
    def test_delete_team_sqlite_error(self, db):
        assert admin().delete_team() == False

    @mock.patch('AIMS.Admin.repo')
    def test_validate_roleid_no_employee_data(self, db):
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value = mocksql
        mocksql.fetchall.return_value = []

        assert admin().validate_roleid('3161af3f-b810-46fd-8fca-7ac5e47966e5', mocksql) == False

    @mock.patch('AIMS.Admin.repo')
    def test_validate_roleid_in_valid_role_id(self, db):
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value = mocksql
        mocksql.fetchall.return_value = []

        assert admin().validate_roleid('f3da47ee-937a-4f2d-9728-1bf8aa4a5ed5,', mocksql) == False

    @mock.patch('AIMS.Admin.repo')
    def test_validate_complaintid_no_complains(self, db):
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value = mocksql
        mocksql.fetchall.return_value = []

        assert admin().validate_complaintid('3161af3f-b810-46fd-8fca-7ac5e47966e5', mocksql) == False

    def test_invalid_complain_id(self):
        pass

    @mock.patch('AIMS.Admin.admin.validate_complaintid', return_value=True)
    @mock.patch('AIMS.Admin.input')
    @mock.patch('AIMS.Admin.repo')
    def test_final_judgement_success(self, db, input, vci):
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value = mocksql
        mocksql.fetchall.return_value = [(
                                         '2d194d0b-43e1-45ed-8086-c3c7e674151d', '125518f2-5908-4cb5-8754-a20aaac8d55b',
                                         '2020-05-10 18:31:52.130590', 40, 20, 'fire broke out in welding zone', 'fire',
                                         'reason', '2020-05-11 12:46:10.316064')]
        input.side_effect = ['125518f2-5908-4cb5-8754-a20aaac8d55b', 'verdict']

        assert admin().final_judgement() == True

    @mock.patch('AIMS.Admin.admin.validate_complaintid')
    @mock.patch('AIMS.Admin.input')
    @mock.patch('AIMS.Admin.repo')
    def test_final_judgement_invalid_complaint_id(self, db, input, vci):
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value = mocksql
        mocksql.fetchall.return_value = [(
            '2d194d0b-43e1-45ed-8086-c3c7e674151d', '125518f2-5908-4cb5-8754-a20aaac8d55b',
            '2020-05-10 18:31:52.130590', 40, 20, 'fire broke out in welding zone', 'fire',
            'reason', '2020-05-11 12:46:10.316064')]
        vci.side_effect = [False, True]
        input.side_effect = [None, '125518f2-5908-4cb5-8754-a20aaac8d55b', 'verdict']

        assert admin().final_judgement() == True

    @mock.patch('AIMS.Admin.admin.validate_complaintid', return_value=True)
    @mock.patch('AIMS.Admin.input')
    @mock.patch('AIMS.Admin.repo')
    def test_final_judgement_invalid_verdict(self, db, input, vci):
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value = mocksql
        mocksql.fetchall.return_value = [(
            '2d194d0b-43e1-45ed-8086-c3c7e674151d', '125518f2-5908-4cb5-8754-a20aaac8d55b',
            '2020-05-10 18:31:52.130590', 40, 20, 'fire broke out in welding zone', 'fire',
            'reason', '2020-05-11 12:46:10.316064')]
        input.side_effect = ['125518f2-5908-4cb5-8754-a20aaac8d55b', 'verdict123', 'verdict']

        assert admin().final_judgement() == True

    @mock.patch('AIMS.Admin.repo')
    def test_final_judgement_no_reports_data(self, db):
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value = mocksql
        mocksql.fetchall.return_value = []

        assert admin().final_judgement() == True

    @mock.patch('AIMS.Admin.repo.sql_connection', side_effect=_sqlite3.Error)
    def test_final_judgement_sqlite_error(self, db):
        assert admin().final_judgement() == False

    @mock.patch('AIMS.Admin.repo')
    def test_validate_team_name(self, db):
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value = mocksql
        mocksql.fetchall.return_value = ['d', 'u', 'm', 'm', 'y', 'd', 'a', 't']

        assert admin().validate_team_name('dummyteam', mocksql) == False

    @mock.patch('AIMS.Admin.repo')
    def test_validate_team_name_no_team_data(self, db):
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value = mocksql
        mocksql.fetchall.return_value = []

        assert admin().validate_team_name('dummyteam', mocksql) == True

    @mock.patch('AIMS.Admin.repo.sql_connection')
    def test_validate_team_name_sqlite_error(self, db):
        mocksql = mock.Mock()
        db.sql_connection.return_value = mocksql
        mocksql.cursor.return_value = mocksql
        mocksql.execute.return_value = mocksql
        mocksql.fetchall.side_effect = _sqlite3.Error

        assert admin().validate_team_name('dummyteam', mocksql) == False
