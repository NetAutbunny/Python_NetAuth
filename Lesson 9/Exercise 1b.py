# Exercise 202: Importing a module from a specific path
import sys
from rich import print

print()
print(sys.path)
print()

sys.path.append(r"C:\My Drive\Study\Python\bin")
import my_lib
