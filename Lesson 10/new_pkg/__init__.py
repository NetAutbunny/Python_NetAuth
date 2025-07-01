# Importing the functions from mod1 and mod2

from new_pkg.mod1 import func1
from new_pkg.mod2 import func2

# Creating __all__ and adding func1, func2 to it

__all__ = ['func1', 'func2']

