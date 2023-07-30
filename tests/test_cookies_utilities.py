import unittest
import cookies_utilities as cu
import datetime
import types


class TestCookiesUtilities(unittest.TestCase):

    def test_copy_datetime(self):
        dt = datetime.datetime.strptime('2016-07-01 02:15:00', '%Y-%m-%d %H:%M:%S')
        dt_copy = cu.copy_datetime(dt)
        self.assertEqual(dt_copy, dt)

        dt = datetime.datetime.strptime('2016-07-01 02:15:00', '%Y-%m-%d %H:%M:%S')
        dt_copy = cu.copy_datetime(dt, {'minute': 0})
        dt_expected = datetime.datetime.strptime('2016-07-01 02:00:00', '%Y-%m-%d %H:%M:%S')
        self.assertEqual(dt_copy, dt_expected)

    def test_get_dates(self):
        dates = cu.get_dates(
            start='2016-07-01 02:00:00',
            end='2016-07-02 01:00:00',
            format='%Y-%m-%d %H:%M:%S',
            delta={'hours': 1})
        self.assertIs(type(dates), list)
        self.assertEqual(len(dates), 24)
        self.assertEqual(dates[1], '2016-07-01 03:00:00')

        dates = cu.get_dates(
            start='2016-07-01',
            end='2016-07-03',
            format='%Y-%m-%d',
            format_out='%Y/%m/%d',
            delta={'days': 1})
        self.assertIs(type(dates), list)
        self.assertEqual(dates, ['2016/07/01', '2016/07/02', '2016/07/03'])

        dates = cu.get_dates(
            start='2016-07-01',
            end='2016-07-03',
            format='%Y-%m-%d',
            delta={'days': 1},
            cast_str=False)
        self.assertIs(type(dates), list)
        self.assertIs(type(dates[1]), datetime.datetime)
        self.assertEqual(dates[1].year, 2016)
        self.assertEqual(dates[1].month, 7)
        self.assertEqual(dates[1].day, 2)

        dates = cu.get_dates(
            start='2016-07-01',
            end='2016-07-03',
            format='%Y-%m-%d',
            delta={'days': 1},
            geniter=True)
        self.assertIs(type(dates), types.GeneratorType)
        self.assertEqual(dates.__next__(), '2016-07-01')
        self.assertEqual(dates.__next__(), '2016-07-02')
        self.assertEqual(dates.__next__(), '2016-07-03')

        with self.assertRaises(ValueError):
            dates = cu.get_dates(
                start='2016-07-01',
                end='2016-07-03',
                format='%Y-%m-%d',
                delta={'days': 0})

    def test_convert_time_to_feature(self):
        dt = '2023-01-02 03:40:50'
        format = '%Y-%m-%d %H:%M:%S'

        fv = cu.convert_time_to_feature(dt, format, period='year', ceiling='day')
        self.assertAlmostEqual(fv, 1.0 / 366.0)

        fv = cu.convert_time_to_feature(dt, format, period='year', ceiling='hour')
        self.assertAlmostEqual(fv, 1.125 / 366.0)

        fv = cu.convert_time_to_feature(dt, format, period='day', ceiling='hour')
        self.assertAlmostEqual(fv, 0.125)
