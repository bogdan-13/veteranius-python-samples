from typing import Any

# function is just an object with a method __call__
# so we can create our statefull functions by overriding __call__ method
class Person:
    def __init__(self, religion: str = 'Paganism') -> None:
        self.religion = religion

    # arguments can be defaulted with =
    def __call__(self, times: int, words: str = 'Hello World') -> str:
        return f'{self.religion}ic person says {words * times}'

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return f'''received 
        args: {args}
        kwargs: {kwds}'''

count = 0

def add(a: int, b: int) -> int:
    print(f'add func received {a} and {b} args')
    return a + b 

def add_lists(a: list, b: list) -> list:
    return a.append(b)

def write_to_json_file(text: str) -> None:
    # write string as json to file
    pass