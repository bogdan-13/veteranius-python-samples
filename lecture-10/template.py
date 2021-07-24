# simple template for creating your custom decorators
from functools import wraps, partial

def repeat(_func=None, *, times=5):
    if _func is None:
        return partial(repeat, times=times)

    @wraps(_func)
    def wrapper(*args, **kwargs):
        for _ in range(times):
            result = _func(*args, **kwargs)
        return result
    return wrapper

@repeat(times=3)
def say_hi():
    print('Hi World!')

@repeat
def say_hello():
    print('Hello World!')