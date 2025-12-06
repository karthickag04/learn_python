"""
LESSON 12: Control Flow Practice Tasks

This file contains practice exercises for control flow concepts:
- If-Else statements
- Nested conditions
- Match-case (Python 3.10+)

Complete each exercise by implementing the function.
Test cases are provided to verify your solutions.

Target Audience: Beginners (10th-12th standard syllabus level)
"""

# ============================================================
# EXERCISE 1: Leap Year Checker
# ============================================================
def is_leap_year(year):
    """
    Check if a year is a leap year.
    
    Rules:
    1. Divisible by 4 AND
    2. If divisible by 100, must also be divisible by 400
    
    Args:
        year (int): The year to check
    
    Returns:
        bool: True if leap year, False otherwise
    
    Examples:
        is_leap_year(2024) → True
        is_leap_year(2023) → False
        is_leap_year(2000) → True
        is_leap_year(1900) → False
    """
    # TODO: Implement this function
    # Hint: Use nested if or combined conditions
    pass


# ============================================================
# EXERCISE 2: Number Sign Checker
# ============================================================
def check_number_sign(num):
    """
    Check if a number is positive, negative, or zero.
    
    Args:
        num (int or float): The number to check
    
    Returns:
        str: "Positive", "Negative", or "Zero"
    
    Examples:
        check_number_sign(5) → "Positive"
        check_number_sign(-3) → "Negative"
        check_number_sign(0) → "Zero"
    """
    # TODO: Implement this function
    pass


# ============================================================
# EXERCISE 3: Grade Calculator
# ============================================================
def calculate_grade(marks):
    """
    Calculate grade based on marks.
    
    Grading Scale:
        90-100: A+
        80-89: A
        70-79: B
        60-69: C
        50-59: D
        Below 50: F
        Invalid: Return "Invalid marks"
    
    Args:
        marks (int): Marks obtained (0-100)
    
    Returns:
        str: Grade (A+, A, B, C, D, F) or "Invalid marks"
    
    Examples:
        calculate_grade(95) → "A+"
        calculate_grade(72) → "B"
        calculate_grade(45) → "F"
        calculate_grade(105) → "Invalid marks"
    """
    # TODO: Implement this function
    pass


# ============================================================
# EXERCISE 4: Triangle Type Checker
# ============================================================
def check_triangle_type(a, b, c):
    """
    Determine the type of triangle based on side lengths.
    
    Types:
        - Equilateral: All sides equal
        - Isosceles: Two sides equal
        - Scalene: No sides equal
        - Invalid: Cannot form a triangle
    
    Triangle Validity Rule:
        Sum of any two sides > third side
    
    Args:
        a, b, c (int or float): Length of three sides
    
    Returns:
        str: Triangle type or "Invalid"
    
    Examples:
        check_triangle_type(3, 3, 3) → "Equilateral"
        check_triangle_type(3, 3, 4) → "Isosceles"
        check_triangle_type(3, 4, 5) → "Scalene"
        check_triangle_type(1, 2, 10) → "Invalid"
    """
    # TODO: Implement this function
    pass


# ============================================================
# EXERCISE 5: Electricity Bill Calculator
# ============================================================
def calculate_electricity_bill(units):
    """
    Calculate electricity bill based on units consumed.
    
    Rate Structure:
        First 100 units: ₹5 per unit
        Next 100 units (101-200): ₹7 per unit
        Next 100 units (201-300): ₹10 per unit
        Above 300 units: ₹15 per unit
    
    Args:
        units (int): Units of electricity consumed
    
    Returns:
        float: Total bill amount in rupees
    
    Examples:
        calculate_electricity_bill(50) → 250.0 (50 × 5)
        calculate_electricity_bill(150) → 850.0 (100×5 + 50×7)
        calculate_electricity_bill(350) → 2650.0 (100×5 + 100×7 + 100×10 + 50×15)
    """
    # TODO: Implement this function
    pass


# ============================================================
# EXERCISE 6: Age Category Classifier
# ============================================================
def classify_age(age):
    """
    Classify a person's age into categories.
    
    Categories:
        0-2: Infant
        3-12: Child
        13-19: Teenager
        20-35: Young Adult
        36-55: Middle Age
        56-75: Senior
        76+: Elderly
        Negative: Invalid
    
    Args:
        age (int): Person's age
    
    Returns:
        str: Age category
    
    Examples:
        classify_age(5) → "Child"
        classify_age(25) → "Young Adult"
        classify_age(70) → "Senior"
    """
    # TODO: Implement this function
    pass


# ============================================================
# EXERCISE 7: Simple Calculator
# ============================================================
def calculator(num1, operator, num2):
    """
    Perform basic arithmetic operations.
    
    Supported operators: +, -, *, /, %, //
    
    Args:
        num1 (float): First number
        operator (str): Operator (+, -, *, /, %, //)
        num2 (float): Second number
    
    Returns:
        float or str: Result or error message
    
    Examples:
        calculator(10, '+', 5) → 15
        calculator(10, '/', 0) → "Error: Division by zero"
        calculator(10, '^', 2) → "Error: Invalid operator"
    """
    # TODO: Implement this function
    pass


# ============================================================
# EXERCISE 8: BMI Calculator
# ============================================================
def calculate_bmi(weight_kg, height_m):
    """
    Calculate BMI and return category.
    
    Formula: BMI = weight / (height * height)
    
    Categories:
        Below 18.5: Underweight
        18.5-24.9: Normal weight
        25.0-29.9: Overweight
        30.0+: Obese
    
    Args:
        weight_kg (float): Weight in kilograms
        height_m (float): Height in meters
    
    Returns:
        tuple: (bmi_value, category)
    
    Examples:
        calculate_bmi(70, 1.75) → (22.86, "Normal weight")
        calculate_bmi(90, 1.70) → (31.14, "Obese")
    """
    # TODO: Implement this function
    pass


# ============================================================
# SOLUTIONS (Scroll down after attempting)
# ============================================================


def _solutions():
    """Reference solutions - Try to solve first before looking!"""
    
    # Solution 1: Leap Year
    def is_leap_year_solution(year):
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                return False
            return True
        return False
    
    # Solution 2: Number Sign
    def check_number_sign_solution(num):
        if num > 0:
            return "Positive"
        elif num < 0:
            return "Negative"
        else:
            return "Zero"
    
    # Solution 3: Grade Calculator
    def calculate_grade_solution(marks):
        if marks < 0 or marks > 100:
            return "Invalid marks"
        elif marks >= 90:
            return "A+"
        elif marks >= 80:
            return "A"
        elif marks >= 70:
            return "B"
        elif marks >= 60:
            return "C"
        elif marks >= 50:
            return "D"
        else:
            return "F"
    
    # Solution 4: Triangle Type
    def check_triangle_type_solution(a, b, c):
        # Check validity
        if a + b <= c or b + c <= a or c + a <= b:
            return "Invalid"
        
        # Check type
        if a == b == c:
            return "Equilateral"
        elif a == b or b == c or c == a:
            return "Isosceles"
        else:
            return "Scalene"
    
    # Solution 5: Electricity Bill
    def calculate_electricity_bill_solution(units):
        if units <= 0:
            return 0.0
        
        bill = 0.0
        
        if units > 300:
            bill += (units - 300) * 15
            units = 300
        
        if units > 200:
            bill += (units - 200) * 10
            units = 200
        
        if units > 100:
            bill += (units - 100) * 7
            units = 100
        
        bill += units * 5
        
        return bill
    
    # Solution 6: Age Category
    def classify_age_solution(age):
        if age < 0:
            return "Invalid"
        elif age <= 2:
            return "Infant"
        elif age <= 12:
            return "Child"
        elif age <= 19:
            return "Teenager"
        elif age <= 35:
            return "Young Adult"
        elif age <= 55:
            return "Middle Age"
        elif age <= 75:
            return "Senior"
        else:
            return "Elderly"
    
    # Solution 7: Calculator
    def calculator_solution(num1, operator, num2):
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            if num2 == 0:
                return "Error: Division by zero"
            return num1 / num2
        elif operator == '%':
            if num2 == 0:
                return "Error: Division by zero"
            return num1 % num2
        elif operator == '//':
            if num2 == 0:
                return "Error: Division by zero"
            return num1 // num2
        else:
            return "Error: Invalid operator"
    
    # Solution 8: BMI Calculator
    def calculate_bmi_solution(weight_kg, height_m):
        if height_m <= 0 or weight_kg <= 0:
            return (0, "Invalid input")
        
        bmi = weight_kg / (height_m ** 2)
        bmi = round(bmi, 2)
        
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"
        
        return (bmi, category)


# ============================================================
# TEST RUNNER
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("    CONTROL FLOW PRACTICE - TEST YOUR SOLUTIONS!")
    print("=" * 60)
    print("\nImplement each function and run this file to test.")
    print("Solutions are available in the _solutions() function.\n")
    
    # Test Exercise 1
    print("Exercise 1: Leap Year Checker")
    if is_leap_year:
        try:
            result = is_leap_year(2024)
            print(f"  is_leap_year(2024) = {result} (Expected: True)")
        except:
            print("  ❌ Function not implemented yet")
    
    # Test Exercise 3
    print("\nExercise 3: Grade Calculator")
    if calculate_grade:
        try:
            result = calculate_grade(85)
            print(f"  calculate_grade(85) = {result} (Expected: A)")
        except:
            print("  ❌ Function not implemented yet")
    
    print("\n" + "=" * 60)
    print("Complete all exercises and run again to verify!")
    print("=" * 60)
