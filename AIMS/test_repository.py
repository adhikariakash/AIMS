import sqlite3
import unittest

import mock
# import AIMS.Repository as sql_connection
from AIMS.Repository import sql_connection


class TestRepository(unittest.TestCase):
    def test_sql_connection_try(self):
        assert isinstance(sql_connection(), type(sqlite3.Connection("")))

    @mock.patch('AIMS.Repository.sqlite3')
    def test_sql_connection_failure(self, mock_sql):
        mock_sql.connect.side_effect = sqlite3.Error
        assert sql_connection() == False
