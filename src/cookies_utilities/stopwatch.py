import time


class Stopwatch:
    """ Stopwatch for measuring processing time.
    """
    def __init__(self):
        self.cache = []

    def press(self, key=''):
        """ Press the stopwatch.

        :param string key: The idenficator for the time (optional).
        """
        self.cache.append((key, time.perf_counter()))

    def show(self):
        """ Show lap times.
        """
        if len(self.cache) < 2:
            return
        for i in range(1, len(self.cache)):
            k = f'{self.cache[i-1][0]}-{self.cache[i][0]}'
            t = self.cache[i][1] - self.cache[i-1][1]
            print(f'time{i}({k}): {t:.3f}s')
        t = self.cache[-1][1] - self.cache[0][1]
        print(f'total: {t:.3f}s')
