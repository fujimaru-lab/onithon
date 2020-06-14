import sys
sys.path.append('batch')
import conf.onithon_config
import unittest


class TestOnithonConfig(unittest.TestCase):
    def test_getvalue(self):
        config = conf.onithon_config.OnithonConfig()
        self.assertEqual(config.getvalue('DB_CONN_INFO', 'ONITHON_DB'), 'mydb')
        self.assertEqual(config.getvalue('DB_CONN_INFO', 'ONITHON_DB_USER'), 'training')
        self.assertEqual(config.getvalue('DB_CONN_INFO', 'ONITHON_DB_PW'), 'training')
        self.assertEqual(config.getvalue('DB_CONN_INFO', 'ONITHON_DB_HST'), 'localhost')
        self.assertEqual(config.getvalue('DB_CONN_INFO', 'ONITHON_DB_PORT'), '5432')


if __name__ == '__main__':
    unittest.main()
