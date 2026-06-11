"""
Function tasks.

Related course folders:
- 06_functions
"""


# TASK 1
# Write a function that returns the area of a rectangle.
def rectangle_area(length, width):
    pass


# TASK 2
# Return both total and average of a list of numbers.
def total_and_average(numbers):
    pass


# TASK 3
# Use a lambda with sorted() to sort students by marks.
# Input: [{"name": "A", "marks": 80}, {"name": "B", "marks": 95}]
def sort_students_by_marks(students):
    pass


# TASK 4
# Return all numbers greater than or equal to pass_mark.
# Use filter or a list comprehension.
def passing_marks(marks, pass_mark=50):
    pass


# TASK 5
# Return factorial using recursion.
def factorial_recursive(n):
    pass


# TASK 6
# Return nth Fibonacci number using recursion.
# fibonacci(0) -> 0, fibonacci(1) -> 1, fibonacci(6) -> 8
def fibonacci(n):
    pass


if __name__ == "__main__":
    assert rectangle_area(5, 4) == 20
    assert total_and_average([10, 20, 30]) == (60, 20.0)
    assert sort_students_by_marks([{"name": "A", "marks": 80}, {"name": "B", "marks": 95}])[0]["name"] == "B"
    assert passing_marks([40, 50, 90]) == [50, 90]
    assert factorial_recursive(5) == 120
    assert fibonacci(6) == 8
    print("All function checks passed.")

