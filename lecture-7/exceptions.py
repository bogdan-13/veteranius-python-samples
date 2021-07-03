class ParentError(Exception):
    pass

class ChildError(ParentError):
    pass

class AnotherChildError(ParentError):
    pass

for cls in [ParentError, ChildError, AnotherChildError]:
    try:
        raise ParentError()
    except ParentError:
        print("MyError")
    except ChildError:
        print("D")
    except AnotherChildError:
        print("C")
    


def divide(a: int, b: int) -> float:
    result = 0.0
    try:
        result = a / b
    except ZeroDivisionError:
        print("dividing by zero...")
        return 0.0
    else:
        print("not dividing by zero...")
        return result
    finally:
        print("finally...")

def divide_if(a: int, b: int) -> float:
    if b == 0:
        return 0.0
    else:
        return a / b