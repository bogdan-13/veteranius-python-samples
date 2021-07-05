# you could throw any exception with raise keyword
raise ValueError('Hello my first error!')

def divide(a: int, b: int) -> float:
    result = 0.0
    try:
        result = a / b
    except ZeroDivisionError as err: # you can catch exceptions from try block
        print("dividing by zero...")
        raise # you can re-raise caught exception
        raise ValueError from err # you can throw new exception that reuses caught one
    else: # else block executes only if no exception was thrown
        print("not dividing by zero...")  
        return result
    finally: # finally blocks executes in either case
        print("finally...")

# to create your custom exceptions
# create module-specific Error class
class Error(Exception):
    pass

# inherit your Error class through your custom exception(s)
class ChildError(Error):
    pass

class AnotherChildError(Error):
    pass

for cls in [Error, ChildError, AnotherChildError]:
    try:
        raise cls()
    except Error: # in such scenario all 3 exceptions will be caught in the first block
                  # because all 3 of them are instances on your custom Error class
        print("MyError")
    except ChildError:
        print("D")
    except AnotherChildError:
        print("C")
    


