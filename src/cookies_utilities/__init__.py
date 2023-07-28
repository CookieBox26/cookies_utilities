from cookies_utilities.stopwatch import Stopwatch
import datetime


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

    If you're using the result as an iterator, it is recommended to set *geniter=True*.

    :param string start: Start time string.
    :param string end: End time string (inclusive).
    :param string format: Conversion format for datetime.strptime.
    :param dict delta: Timedelta as args for datetime.timedelta.
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
