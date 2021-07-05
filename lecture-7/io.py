file_path = 'temp.file'
name = 'John'

# modern Python's string interpolation, use it for new code
# supports a lot of formatting options for details see https://docs.python.org/3/library/string.html#formatspec
print(f'Hello, {name}')

# string format
print('Hello, {}'.format(name))
# modulo string formatting
print('Hello, %s' % name)

# write string values to file
# different modes are listed in https://docs.python.org/3/library/functions.html#open
with open(file_path, 'w') as temp:
    temp.writelines(['Hello Python World!', 'What do we want?', 'Multi-line lambda!'])

# read file as string
with open(file_path, 'r') as temp:
    print(f'{temp.read()=}')

# to work with big files you should not load all file to memory, but read it partially
with open(file_path, 'r') as temp:
    for line in temp:
        print(f'{line=}')

# old-school way of working with files (without with keyword)
try:
    temp = open(file_path, 'r')
    print(f'{temp.read()=}')
finally:
    temp.close()

# if your class should open and reuse opened resources this is how to make it work with with
class MyCloseable:
    def __init__(self):
        self.resource = open(file_path, 'r+')

    def write_str(self, value: str = 'Hello'):
        self.resource.write(value)

    def __enter__(self):
        print('Opening MyCloseable...')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print('Closing MyCloseable...')
        self.resource.close()

with MyCloseable() as temp:
    value = 'My Python created file'
    print(f'Writing "{value}" to resource')
    temp.write_str()

import os
os.remove(file_path)