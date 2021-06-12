from typing import Any, Callable, Protocol


name = 'Alyna'

def greet():
    name = 'Yulia'   

    def inner_greet():
        global name
        name = 'Stephan'
        print(f'Inner inner: {name}')

    inner_greet()
    print(f'inner: {name}')

greet()
print(f'Outer: {name}')


multiply_anonymous = lambda a, b: a / 0

def multiply(self: 'Counter', other: int):
    return self.count * other

# class Counter:
#     def __init__(self, action: Callable[..., Any], initial: int = 0) -> None:
#         self.count = initial
#         self.execute = action

class Counter(Protocol):
    def __call__(self) -> int: ...

    def multiply(self, other: int) -> int: ...

class CounterClass(Counter):
    def __init__(self, initial: int = 0) -> None:
        self.count = initial

    def __call__(self) -> int:
        self.count += 1
        return self.count

    def multiply(self, other: int) -> int:
        return self.count * other  


# def counter(initial: int = 0) -> Callable[[], int]:
#     count: int = initial

#     def increment_and_return() -> int:
#         nonlocal count
#         count += 1
#         return count

#     return increment_and_return

def counter(initial: int = 0) -> Counter:
    count: int = initial
    class InnerCounter(Counter):
        def __call__(self) -> int: 
            nonlocal count
            count += 1
            return count

        def multiply(self, other: int) -> int:
            return count * other

    return InnerCounter()

print(multiply_anonymous(2, 3))