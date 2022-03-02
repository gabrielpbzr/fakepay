import imp
import unittest
from fakepay import config
from os import environ

DATABASE_URL = "postgres://username:password@database.host.dev:5432/fakepay"


class ConfigTest(unittest.TestCase):
    def setUp(self) -> None:
        environ.setdefault("DATABASE_URL", DATABASE_URL)

    def test_load_database_config(self):
        self.assertEqual(DATABASE_URL, config.database_url())
