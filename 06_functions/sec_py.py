# Demonstrating how to import functions from other Python files

# Method 1: Import the entire module
# This imports first_py.py from the same directory
import first_py

# Method 2: Import from a subfolder (package)
# 'file' is a subfolder containing third_py.py
# from file import third_py  # This imports with original name
from file import third_py as tp  # Using alias 'tp' for shorter reference

# Using functions from imported modules:
# Access function using: module_name.function_name()
print(first_py.addition(10, 20))  # Calls addition() from first_py.py

# Using the aliased import:
# print(third_py.multiply(10, 20))  # Would work with original import
print(tp.multiply(10, 20))  # Calls multiply() from file/third_py.py using alias