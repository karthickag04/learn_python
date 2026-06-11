"""
Loop tasks.

Related course folders:
- 05_loops
"""


# TASK 1
# Return the multiplication table for a number as a list of strings.
# Example for 5:
# ["5 x 1 = 5", "5 x 2 = 10", ... "5 x 10 = 50"]
def multiplication_table(number):
    pass


# TASK 2
# Return the sum of all even numbers from 1 to limit.
def sum_even_numbers(limit):
    pass


# TASK 3
# Return factorial of n using a loop.
def factorial_loop(n):
    pass


# TASK 4
# Return a right triangle pattern as a list of strings.
# Example for 4:
# ["*", "**", "***", "****"]
def star_pattern(rows):
    pass


# TASK 5
# Find the first number divisible by 7 between start and end.
# Return None if no number is found.
def first_divisible_by_7(start, end):
    pass


# TASK 6
# Remove vowels from a string using a loop and continue.
def remove_vowels(text):
    pass


if __name__ == "__main__":
    assert multiplication_table(3)[2] == "3 x 3 = 9"
    assert sum_even_numbers(10) == 30
    assert factorial_loop(5) == 120
    assert star_pattern(3) == ["*", "**", "***"]
    assert first_divisible_by_7(10, 20) == 14
    assert remove_vowels("Python") == "Pythn"
    print("All loop checks passed.")

