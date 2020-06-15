import unittest
import sys
sys.path.append('batch')
import log.batch_logger


class TestBatchLog(unittest.TestCase):
    def test_create_msg(self):
        logger = log.batch_logger.BatchLog("test")
        template = 'test value is {0}'
        res = logger.create_msg(template, "TEST")
        self.assertEqual(res, 'test value is TEST')

    def test_create_msg_mult_param(self):
        logger = log.batch_logger.BatchLog("TEST02")
        log_fmt = '{0} is a {1} onigiri manager... {2}'
        res = logger.create_msg(log_fmt, "onithon", "good", "hogehoge")
        self.assertEqual(res, 'onithon is a good onigiri manager... hogehoge')

if __name__ == "__main__":
    unittest.main()
