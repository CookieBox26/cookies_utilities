import time


class Timer:
    def __init__(self):
        self.cache = []
    def press(self, key=''):
        self.cache.append((key, time.perf_counter()))
    def show(self):
        if len(self.cache) < 2:
            return
        for i in range(1, len(self.cache)):
            k = f'{self.cache[i-1][0]}-{self.cache[i][0]}'
            t = self.cache[i][1] - self.cache[i-1][1]
            print(f'time{i}({k}): {t:.3f}s')
        t = self.cache[-1][1] - self.cache[0][1]
        print(f'total: {t:.3f}s')
