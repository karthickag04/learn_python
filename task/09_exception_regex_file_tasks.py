"""
Exception, regex, and file-handling tasks.

Related course folders:
- 10_exception_handling
- 11_regular_expressions
- 12_file_handling
"""

import csv
import json
import re


# TASK 1
# Safely divide two numbers.
# Return the result, or "Cannot divide by zero".
def safe_divide(a, b):
    pass


# TASK 2
# Create a custom exception called InvalidAgeError.
# validate_age(age) should:
# - return True for age between 0 and 120
# - raise InvalidAgeError otherwise
class InvalidAgeError(Exception):
    pass


def validate_age(age):
    pass


# TASK 3
# Return True if an email looks valid.
# Keep the regex beginner-friendly.
def is_valid_email(email):
    pass


# TASK 4
# Extract all phone numbers that match 10 digits.
def extract_phone_numbers(text):
    pass


# TASK 5
# Write a list of student dictionaries to a JSON file.
def write_students_json(file_path, students):
    pass


# TASK 6
# Read a list of student dictionaries from a JSON file.
def read_students_json(file_path):
    pass


# TASK 7
# Write contacts to CSV.
# contacts example: [{"name": "A", "phone": "1234567890"}]
def write_contacts_csv(file_path, contacts):
    pass


if __name__ == "__main__":
    assert safe_divide(10, 2) == 5
    assert safe_divide(10, 0) == "Cannot divide by zero"
    assert validate_age(25) is True
    assert is_valid_email("test@example.com") is True
    assert extract_phone_numbers("Call 9876543210 or 12345") == ["9876543210"]
    print("Core exception/regex checks passed. Test file tasks after implementing them.")

