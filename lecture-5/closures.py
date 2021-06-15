from typing import Callable, Protocol

class Counter(Protocol):
    def __call__(self) -> int: ...

    def multiply(self, other: int) -> int: ...

# simple counter that also can multiply it's count by some value
class CounterClass(Counter):
    def __init__(self, initial: int = 0) -> None:
        self.count = initial

    def __call__(self) -> int:
        self.count += 1
        return self.count

    def multiply(self, other: int) -> int:
        return self.count * other  

class_counter = CounterClass(1)
class_counter() # 2
class_counter() # 3
class_counter.multiply(2) # 6
# count can be accessed freely
class_counter.count # 3

# classical closure that closes over count variable
# this variable is hidden from the outer world and can be changed using func returned
def counter(initial: int = 0) -> Callable[[], int]:
    count: int = initial

    def increment_and_return() -> int:
        nonlocal count
        count += 1
        return count

    return increment_and_return

closure_func_counter = counter(2)
closure_func_counter() # 2
closure_func_counter() # 3

# closure that returns type instead of simple func, 
# therefore can be parametrized with different behavior
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

closure_class_counter = counter(3)
closure_class_counter() # 4
closure_class_counter() # 5
closure_class_counter.multiply(3) # 15
# variable count is hidden from the outer world
closure_class_counter.count # AttributeError