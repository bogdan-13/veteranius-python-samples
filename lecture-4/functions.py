from typing import Any

# function is just an object with a method __call__
# so we can create our statefull functions by overriding __call__ method
class Person:
    def __init__(self, religion: str = 'Paganism') -> None:
        self.religion = religion

    # arguments can be defaulted with =
    def __call__(self, times: int, words: str = 'Hello World') -> str:
        return f'{self.religion} person says {words * times}'

    # variadic arguments * - list, ** - dictionary
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return f'''received 
        args: {args}
        kwargs: {kwds}'''

# default arguments are optional
Person()(3)
# arguments can be named and passed in any order
Person()(words='Lorem ipsum', times=2)

# pure function does nothing except for returning value
# it always returns the same value given the same params
def add_pure(a: int, b: int) -> int:
    return a + b

# impure functions (discouraged practices)

count = 0
def state_change() -> str:
    global count
    count += 1
    return 'Some outer state was changed'

def rely_on_state() -> str:
    return 'Relying on outer state' * count


def add_with_print(a: int, b: int) -> int:
    print('Printing some important details and then returning calculated value')
    return a + b 

# param a is changed
def append_to_list(a: list, b: Any) -> list:
    a.append(b)
    return a

# recommended way to signal about impurity is to create separate 
# procedure with None as a return type
# by this reader clearly understands that some side-effect(s) happen inside as no value is expected
def write_to_json_file(text: str) -> None:
    # write string as json to file
    pass