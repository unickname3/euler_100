from functools import wraps
import time


def timer(function):
    @wraps(function)
    def wrapped(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        print(f"Function {function.__qualname__} took {time.time() - start_time:.2f}s")
        return result

    return wrapped
