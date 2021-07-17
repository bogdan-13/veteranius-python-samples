
# we can import separate modules from package
import util.rpc.rpc

util.rpc.rpc.get_connection()

# this is preferred way of importing modules from packages, 
# we won't need to fully qualify them after such import
from util.rpc import rpc

rpc.get_connection()

# we can perform same import tricks as with modules
from util.connection.db import get_connection as db_connection

db_connection()

# useful links:
# https://python-packaging.readthedocs.io/en/latest/minimal.html

# https://stackoverflow.com/a/41573588/12018844 - virtualenv/pyenv/virtualenvwrapper/pipenv/venv
# https://stackoverflow.com/a/39928067/12018844 - pip/pyenv/virtualenv/conda

# https://www.anaconda.com/blog/understanding-conda-and-pip
# https://pypa.github.io/pipx/comparisons/