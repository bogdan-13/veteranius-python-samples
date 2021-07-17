# inside package imports start with project's root directory, so we need to specify full path to module
import util.connection.db
# ...or we can use relative imports with . for current package and .. for parent package
from ..rpc import rpc

# magic variable __all__ is used to specify which members to export for usage with *
# e.g. with such config when somepackage imports this package like: 
# from .connection import *
# only db module will be imported
__all__ = ['db']

# when someone is importing this package __init__ script is executed
print(f'Executing code inside {__name__}')
