from cookies_utilities.stopwatch import Stopwatch
import datetime


def copy_datetime(dt, options={}):
    """ Create a copy of a datetime.datetime object.

    :param datetime.datetime dt: The original object.
    :param dict options: If you wish to overwrite certain fields,
                         please specify them using this dictionary (optional).
                         The keys must be in ['year', 'month', 'day', 'hour', 'minute',
                         'second', 'microsecond', 'tzinfo', 'fold'].
    :rtype: datetime.datetime
    """
    args = {
        'year': dt.year, 'month': dt.month, 'day': dt.day,
        'hour': dt.hour, 'minute': dt.minute, 'second': dt.second,
        'microsecond': dt.microsecond, 'tzinfo': dt.tzinfo,  'fold': dt.fold,
    }
    args.update(options)
    dt_new = datetime.datetime(**args)
    return dt_new


def get_dates(
    start='2016-07-01 02:00:00',
    end='2016-07-02 01:00:00',
    format='%Y-%m-%d %H:%M:%S',
    delta={'weeks': 0, 'days': 0, 'hours': 1, 'minutes': 0},
    geniter=False,
    cast_str=True,
    format_out=None,
):
    """ Returns a list of times from the 'start' time to the 'end' time,
    incremented by 'delta'.
    Please ensure 'delta' is greater than or equal to 1 microsecond.

    If you're using the result as an iterator, it is recommended to set *geniter=True*.

    :param string start: Start time string.
    :param string end: End time string (inclusive).
    :param string format: Conversion format for datetime.strptime.
    :param dict delta: Timedelta as args for datetime.timedelta (>= 1 microsecond).
    :param bool geniter: Whether to return as a generator iterator (default *False*).
    :param bool cast_str: Whether to convert output to string (default *True*).
    :param string format_out: Conversion format for output (default same to **format**).
    :rtype: list (or generator iterator) of string (or datetime.datetime)
    """
    if format_out is None:
        format_out = format

    dt_ = datetime.datetime.strptime(start, format)
    end_ = datetime.datetime.strptime(end, format)
    delta_ = datetime.timedelta(**delta)
    if delta_ < datetime.timedelta(microseconds=1):
        raise ValueError('Invalid argument: delta must be greater than or equal to 1 microsecond.')

    def _generator(dt_, end_, delta_, cast_str, format_out):
        while not end_ < dt_:
            dt_out = dt_
            if cast_str:
                dt_out = dt_out.strftime(format_out)
            yield dt_out
            dt_ += delta_

    geniter_ = _generator(dt_, end_, delta_, cast_str, format_out)
    if geniter:
        return geniter_
    return list(geniter_)


def convert_time_to_feature(dt, format='%Y-%m-%d %H:%M:%S', period='day', ceiling=None):
    """ Convert a time to a feature value between 0 and 1.
    The return feature value represents how much of a period has passed.

    For example, if the period is 1 day, a feature value of noon is 0.5.

    Note 1: When setting the period to a month, the cycle is considered as 31 days
    regardless of the actual number of days in that month. This is to ensure that
    the feature value for 'the 5th day of any month' is consistent.

    Note 2: When setting the period to a year, the cycle is considered as 366 days
    regardless of the actual number of days in that year. This is done to ensure that
    the feature value for 'the 5th day of any year' remains the same,
    regardless of the specific year.

    :param string dt: A time string.
    :param string format: Conversion format for datetime.strptime.
                          If you set this argument to None,
                          we expect 'dt' to originally be datetime.datetime object.
    :param string period: A time period to convert a time to a feature value.
                          This must be in ['year', 'month', 'week', 'day', 'hour', 'minute', 'second'].
    :param string ceiling: If you want to round the time when calculating the feature value,
                           specify the rounding granularity in this argument (optional).
                           This must be in ['year', 'month', 'day', 'hour', 'minute', 'second'].
    :rtype: float
    """
    if format is not None:
        dt = datetime.datetime.strptime(dt, format)

    template = [('year', 1), ('month', 1), ('day', 1), ('hour', 0),
                ('minute', 0), ('second', 0), ('microsecond', 0)]
    keys = [v[0] for v in template]

    if period == 'week':
        dt_0 = dt - datetime.timedelta(days=dt.weekday())
        dt_0 = copy_datetime(dt_0, dict(template[(keys.index('day') + 1):]))
    elif period in keys[:-1]:
        dt_0 = copy_datetime(dt, dict(template[(keys.index(period) + 1):]))
    else:
        li = keys[:-1] + ['week']
        raise ValueError(f'Invalid argument: \'period\' must be in {li}.')

    if ceiling is None:
        dt_1 = dt
    elif ceiling in keys[:-1]:
        dt_1 = copy_datetime(dt, dict(template[(keys.index(ceiling) + 1):]))
    else:
        raise ValueError(f'Invalid argument: \'ceiling\' must be in {keys[:-1]}.')

    offset_seconds = dt_1.timestamp() - dt_0.timestamp()

    if period == 'year':
        delta_seconds = 366.0 * 86400.0
    elif period == 'month':
        delta_seconds = 31.0 * 86400.0
    elif period == 'week':
        delta_seconds = 7.0 * 86400.0
    elif period == 'day':
        delta_seconds = 86400.0
    elif period == 'hour':
        delta_seconds = 3600.0
    elif period == 'minute':
        delta_seconds = 60.0
    elif period == 'second':
        delta_seconds = 1.0
    else:
        raise ValueError(f'Invalid argument: invalid \'period\'.')

    return offset_seconds / delta_seconds
