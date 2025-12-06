"""
==============================================
LESSON 03: Variables and Naming Conventions
==============================================

Variables are containers that store data values.
Think of them as labeled boxes where you keep information.

Real-World Use Case:
- Storing user information (name, age, email)
- Keeping track of scores in a game
- Storing product prices in e-commerce
- Maintaining configuration settings
"""

# ==============================================
# 1. CREATING VARIABLES
# ==============================================

# Basic variable assignment (= is the assignment operator)
name = "John"
age = 25
height = 5.9
is_student = True

# Print variables
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)


# ==============================================
# 2. VARIABLE NAMING RULES
# ==============================================

# ✅ VALID variable names:
my_variable = 10          # Can use underscores
myVariable = 20           # Can use camelCase
MyVariable = 30           # Can start with uppercase
_private_var = 40         # Can start with underscore
var2 = 50                 # Can contain numbers (not at start)
CONSTANT_VALUE = 100      # Constants in UPPERCASE

# ❌ INVALID variable names (will cause errors):
# 2variable = 10          # Cannot start with a number
# my-variable = 20        # Cannot use hyphens
# my variable = 30        # Cannot use spaces
# class = 40              # Cannot use reserved keywords


# ==============================================
# 3. NAMING CONVENTIONS (PEP 8 Style Guide)
# ==============================================

# Variables: lowercase with underscores (snake_case)
student_name = "Alice"
total_price = 99.99
user_email = "alice@email.com"

# Constants: UPPERCASE with underscores
MAX_CONNECTIONS = 100
PI_VALUE = 3.14159
DATABASE_URL = "localhost:5432"

# Classes: PascalCase (each word capitalized)
# class StudentRecord:
# class ShoppingCart:

# Private variables: start with underscore
_internal_counter = 0
_private_data = "secret"

# "Really private": start with double underscore
__very_private = "top secret"


# ==============================================
# 4. DYNAMIC TYPING
# ==============================================

# Python allows changing variable types (dynamic typing)
data = 100          # Integer
print("data is:", data, "| Type:", type(data))

data = "Hello"      # Now it's a string!
print("data is:", data, "| Type:", type(data))

data = [1, 2, 3]    # Now it's a list!
print("data is:", data, "| Type:", type(data))


# ==============================================
# 5. MULTIPLE ASSIGNMENT
# ==============================================

# Assign same value to multiple variables
x = y = z = 0
print("x:", x, "y:", y, "z:", z)

# Assign different values in one line
name, age, city = "John", 25, "New York"
print(f"Name: {name}, Age: {age}, City: {city}")

# Swap values (Python's elegant way)
a = 10
b = 20
print(f"Before swap: a = {a}, b = {b}")

a, b = b, a  # Swap without temporary variable!
print(f"After swap: a = {a}, b = {b}")


# ==============================================
# 6. VARIABLE SCOPE PREVIEW
# ==============================================

global_var = "I'm accessible everywhere"

def my_function():
    local_var = "I'm only accessible inside this function"
    print(global_var)   # Can access global variable
    print(local_var)    # Can access local variable

my_function()
print(global_var)       # Can access global variable
# print(local_var)      # ERROR: local_var is not defined here


# ==============================================
# 7. REAL-WORLD EXAMPLES
# ==============================================

# Example 1: User Profile
user_id = 12345
username = "john_doe"
email = "john@example.com"
is_active = True
account_balance = 1500.75

print("\n--- User Profile ---")
print(f"ID: {user_id}")
print(f"Username: {username}")
print(f"Email: {email}")
print(f"Active: {is_active}")
print(f"Balance: ${account_balance}")

# Example 2: Product Information
product_name = "Laptop"
product_price = 999.99
quantity_in_stock = 50
is_available = quantity_in_stock > 0

print("\n--- Product Info ---")
print(f"Product: {product_name}")
print(f"Price: ${product_price}")
print(f"Stock: {quantity_in_stock}")
print(f"Available: {is_available}")

# Example 3: Configuration Settings
APP_NAME = "MyApp"
VERSION = "1.0.0"
DEBUG_MODE = False
MAX_USERS = 1000

print("\n--- App Configuration ---")
print(f"App: {APP_NAME} v{VERSION}")
print(f"Debug Mode: {DEBUG_MODE}")
print(f"Max Users: {MAX_USERS}")


# ==============================================
# 8. RESERVED KEYWORDS (Cannot use as variables)
# ==============================================

"""
List of Python reserved keywords:

False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield

To see all keywords:
import keyword
print(keyword.kwlist)
"""

import keyword
print("\n--- Python Reserved Keywords ---")
print(keyword.kwlist)


# ==============================================
# 9. CHECKING VARIABLE TYPE
# ==============================================

name = "Alice"
age = 25
price = 99.99
is_active = True
items = [1, 2, 3]

print("\n--- Variable Types ---")
print(f"name is type: {type(name)}")
print(f"age is type: {type(age)}")
print(f"price is type: {type(price)}")
print(f"is_active is type: {type(is_active)}")
print(f"items is type: {type(items)}")


# ==============================================
# PRACTICE EXERCISES
# ==============================================
"""
Try these exercises:

1. Create variables for a person: first_name, last_name, age, city
2. Create constants for app settings: APP_NAME, VERSION, MAX_RETRIES
3. Use multiple assignment to create x, y, z with values 1, 2, 3
4. Swap two variables without using a temporary variable
5. Create a "product inventory" with name, price, quantity, is_in_stock
"""


# ==============================================
# SUMMARY
# ==============================================
"""
Key Points:
1. Variables store data values using = assignment
2. Names can contain letters, numbers, underscores (not starting with number)
3. Use snake_case for variables, UPPERCASE for constants
4. Python is dynamically typed (variables can change type)
5. Multiple assignment: a, b, c = 1, 2, 3
6. Cannot use reserved keywords as variable names

Best Practices:
- Use descriptive names (user_age not ua)
- Use lowercase with underscores (snake_case)
- Use UPPERCASE for constants
- Avoid single-letter names except in loops (i, j, k)

Next Lesson: Data Types
"""
