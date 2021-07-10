# main module
# Python file is a module

# import module by name; we can use all members of a module using module name as prefix
import sys
import os

# sys.path holds path where interpreter searches requested modules
# technically we can add custom path to it and then import files from that path
sys.path.append(os.path.abspath('util'))

print(f'{sys.path=}')

import platform

# get your Python implementation
print(platform.python_implementation())

# we can import only specific module members
from db import main, get_connection
# we can alias module or its member
from rpc import get_connection as rpc_connection
# we can import all members of a module and use them without prefix
# not recommended practice due to potential unexpected name collisions
from array import *

get_connection()
rpc_connection()
main()

# with dir() func we can get members of current module
print(f'{dir()=}')
# or any other module
print(f'{dir(sys)=}')
# all 'standard' members live in __builtins__ module
print(f'{dir(__builtins__)=}')

# so these two expressions are equivalent
print(f'{type(str(5))=}')
print(f'{__builtins__.type(__builtins__.str(5))=}')

