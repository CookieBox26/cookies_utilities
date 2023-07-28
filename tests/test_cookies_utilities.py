import unittest
import cookies_utilities as cu


class TestCookiesUtilities(unittest.TestCase):

    def test_get_dates(self):
        dates = cu.get_dates(
            start='2016-07-01 02:00:00',
            end='2016-07-02 01:00:00',
            format='%Y-%m-%d %H:%M:%S',
            delta={'hours': 1})
        self.assertEqual(len(dates), 24)
        self.assertEqual(dates[1], '2016-07-01 03:00:00')

        dates = cu.get_dates(
            start='2016-07-01',
            end='2016-07-03',
            format='%Y-%m-%d',
            format_out='%Y/%m/%d',
            delta={'days': 1})
        self.assertEqual(dates, ['2016/07/01', '2016/07/02', '2016/07/03'])
