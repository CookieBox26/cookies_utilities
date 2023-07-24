import unittest
import cookies_utilities as cu


class TestTimer(unittest.TestCase):
    def test_init(self):
        timer = cu.Timer()
        timer.press('0')
        timer.press('1')
        timer.press('2')
        self.assertEqual(len(timer.cache), 3)
