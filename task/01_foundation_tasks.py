"""
Foundation tasks: print, comments, variables, naming, and data types.

Related course folders:
- 01_basics
"""


# TASK 1
# Create variables for your profile and print a neat profile card.
# Required variables: first_name, last_name, age, city, is_learning_python
def print_profile_card():
    pass


# TASK 2
# Return a dictionary containing the type name of each value.
# Example: {"age": "int", "price": "float"}
def get_value_types():
    name = "Python"
    age = 30
    price = 99.99
    is_active = True
    items = ["book", "pen"]

    # TODO: return a dictionary with keys: name, age, price, is_active, items
    pass


# TASK 3
# Swap two values without using a temporary variable.
def swap_values(a, b):
    pass


# TASK 4
# Create a receipt header using print, escape characters, and string repetition.
def print_receipt_header(store_name):
    pass


if __name__ == "__main__":
    print("Foundation tasks")
    assert swap_values(10, 20) == (20, 10)
    assert get_value_types()["age"] == "int"
    print("Basic checks passed. Complete the print tasks manually.")

