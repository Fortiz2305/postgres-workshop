import time


def measure(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print('query time: {} sec'.format(te-ts))
        return result
    return timed
