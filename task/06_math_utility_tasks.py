"""
Math and utility tasks.

Related course folders:
- 07_math_and_utilities
"""

import math
import random


# TASK 1
# Return the hypotenuse of a right triangle using math.sqrt or math.hypot.
def hypotenuse(a, b):
    pass


# TASK 2
# Return the area of a circle rounded to 2 decimal places.
def circle_area(radius):
    pass


# TASK 3
# Convert degrees to radians rounded to 4 decimal places.
def degrees_to_radians(degrees):
    pass


# TASK 4
# Return a random OTP with the given number of digits.
# Hint: for 4 digits, return a number between 1000 and 9999.
def generate_otp(digits=4):
    pass


# TASK 5
# Return the ceiling, floor, and rounded value in a dictionary.
def number_rounding_report(value):
    pass


if __name__ == "__main__":
    assert hypotenuse(3, 4) == 5.0
    assert circle_area(7) == 153.94
    assert degrees_to_radians(180) == 3.1416
    assert len(str(generate_otp(4))) == 4
    assert number_rounding_report(4.7) == {"ceil": 5, "floor": 4, "round": 5}
    print("All math/utility checks passed.")

