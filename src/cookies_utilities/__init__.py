from cookies_utilities.stopwatch import Stopwatch
import datetime


def get_dates(
    start='2016-07-01 02:00:00',
    end='2016-07-02 01:00:00',
    format='%Y-%m-%d %H:%M:%S',
    delta={'weeks': 0, 'days': 0, 'hours': 1, 'minutes': 0},
    cast_str=True,
    format_out=None,
):
    """ Returns a list of times from the 'start' time to the 'end' time,
    incremented by 'delta'.

    :param string start: Start time string.
    :param string end: End time string (inclusive).
    :param string format: Conversion format for datetime.strptime.
    :param dict delta: Timedelta as args for datetime.timedelta.
    :param bool cast_str: Whether to convert output to string (default true).
    :param string format_out: Conversion format for output (default same to **format**).
    :rtype: list of string (or datetime.datetime)
    """
    if format_out is None:
        format_out = format
    dt_ = datetime.datetime.strptime(start, format)
    end_ = datetime.datetime.strptime(end, format)
    delta_ = datetime.timedelta(**delta)
    out_ = []
    for i in range(1000000):
        if end_ < dt_:
            break
        dt__ = dt_
        if cast_str:
            dt__ = dt__.strftime(format_out)
        out_.append(dt__)
        dt_ += delta_
    return out_
