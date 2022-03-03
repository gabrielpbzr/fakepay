import os
from unittest import TestCase, mock
from fakepay import config


DATABASE_URL = "postgres://username:password@database.host.dev:5432/fakepay"


@mock.patch.dict(os.environ, {"DATABASE_URL": DATABASE_URL})
class ConfigTest(TestCase):

    def test_load_database_config(self):
        config.load_values()
        self.assertEqual("username", config.database['user'])
        self.assertEqual("password", config.database['password'])
        self.assertEqual("database.host.dev", config.database['host'])
        self.assertEqual("5432", config.database['port'])
        self.assertEqual("fakepay", config.database['dbname'])
