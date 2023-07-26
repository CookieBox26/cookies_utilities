import unittest
import cookies_utilities as cu


class TestStopwatch(unittest.TestCase):
    def test_init(self):
        sw = cu.Stopwatch()
        sw.press('0')
        sw.press('1')
        sw.press('2')
        self.assertEqual(len(sw.cache), 3)
