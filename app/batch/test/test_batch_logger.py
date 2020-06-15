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


if __name__ == "__main__":
    unittest.main()
