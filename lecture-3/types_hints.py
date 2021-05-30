# simple type hinting

def add(a: int, b: int) -> int: # typed function example
    return a + b

print(add(1, 2)) # 3
print(add('1', '2')) # 12 - linter produces error, but works in runtime due 
# to duck (structural) typing of Python 
# and the fact that str class has method __add__(str)

a: str = '5' # variables can be type hinted as well
