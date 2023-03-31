import time
import os
# ... your definition of log decorator...
def log(func):
    def wrapper(*args, **kwargs):
        f = open("machine.log", "a")
        print(f"({os.environ['USER']})Running:", end=' ', file=f)
        print("{: <19}".format(func.__name__.replace('_', ' ').capitalize()), end='', file=f)
        start_time = time.time() * 1000
        ret = func(*args, **kwargs)
        end_time = (time.time() * 1000) - start_time
        end_time = "{:.3f} s".format(end_time / 1000) if int(end_time / 1000) > 0 else "{:.3f} ms".format(end_time)
        print("[ exec-time = {} ]".format(end_time), file=f)
        return ret
    return wrapper