"""
Operator and control-flow tasks.

Related course folders:
- 02_operators
- 03_control_flow
"""


# TASK 1
# Calculate final price after discount and tax.
# discount_percent and tax_percent are given as numbers like 10 for 10%.
def calculate_final_price(price, discount_percent, tax_percent):
    pass


# TASK 2
# Return True if a student passes.
# Rules:
# - average mark must be at least 50
# - attendance must be at least 75
def has_student_passed(mark1, mark2, mark3, attendance_percent):
    pass


# TASK 3
# Return "Positive", "Negative", or "Zero".
def number_sign(number):
    pass


# TASK 4
# Return grade using this scale:
# 90-100: A+
# 80-89: A
# 70-79: B
# 60-69: C
# 50-59: D
# 0-49: F
# Otherwise: Invalid
def grade_from_marks(marks):
    pass


# TASK 5
# Build a simple calculator.
# Supported operators: +, -, *, /, //, %, **
# Return "Division by zero" when needed.
# Return "Invalid operator" for unknown operators.
def calculator(a, operator, b):
    pass


if __name__ == "__main__":
    assert calculate_final_price(1000, 10, 18) == 1062.0
    assert has_student_passed(60, 55, 50, 80) is True
    assert number_sign(-5) == "Negative"
    assert grade_from_marks(95) == "A+"
    assert grade_from_marks(120) == "Invalid"
    assert calculator(2, "**", 3) == 8
    assert calculator(10, "/", 0) == "Division by zero"
    print("All operator/control-flow checks passed.")

