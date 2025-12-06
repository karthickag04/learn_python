"""
==============================================
LESSON 01: Hello World - Your First Python Program
==============================================

Welcome to Python! This is traditionally the first program every programmer writes.
The print() function displays output to the console.

Real-World Use Case:
- Displaying welcome messages in applications
- Logging system status messages
- Outputting results to users
"""

# ==============================================
# 1. BASIC PRINT STATEMENT
# ==============================================

# The simplest Python program - print a message
print("Hello, World!")

# You can print any text inside quotes (single or double)
print('Welcome to Python Programming!')
print("Let's learn Python together!")


# ==============================================
# 2. PRINTING NUMBERS AND CALCULATIONS
# ==============================================

# Print numbers directly
print(42)
print(3.14159)

# Print calculations - Python evaluates the expression first
print(2 + 3)          # Output: 5
print(10 - 4)         # Output: 6
print(5 * 6)          # Output: 30
print(20 / 4)         # Output: 5.0


# ==============================================
# 3. PRINTING MULTIPLE VALUES
# ==============================================

# Use commas to print multiple items (adds space between them)
print("The answer is", 42)
print("Sum of 5 + 3 =", 5 + 3)
print("Name:", "John", "Age:", 25)


# ==============================================
# 4. REAL-WORLD EXAMPLES
# ==============================================

# Example 1: Welcome message for an app
print("=" * 40)
print("   Welcome to Student Portal   ")
print("=" * 40)

# Example 2: Displaying a receipt header
print("\n")  # Empty line for spacing
print("*" * 35)
print("     GROCERY STORE RECEIPT")
print("     Date: 2024-01-15")
print("*" * 35)

# Example 3: Simple status messages
print("\n[INFO] Application started successfully")
print("[INFO] Loading user data...")
print("[SUCCESS] Data loaded!")


# ==============================================
# 5. ESCAPE CHARACTERS
# ==============================================

# \n = new line
print("Line 1\nLine 2\nLine 3")

# \t = tab (indentation)
print("Name:\tJohn")
print("Age:\t25")
print("City:\tNew York")

# \\ = backslash
print("File path: C:\\Users\\Documents")

# \" or \' = quotes inside string
print("He said, \"Python is awesome!\"")
print('It\'s a beautiful day!')


# ==============================================
# 6. PRACTICE EXERCISES
# ==============================================
"""
Try these exercises:

1. Print your name
2. Print your age
3. Print: I am learning Python!
4. Print a simple math calculation (like 100 + 200)
5. Create a simple "business card" display with your details
"""

# Your practice code here:
# print("Your Name")
# print("Your Age:", 20)


# ==============================================
# SUMMARY
# ==============================================
"""
Key Points:
1. print() displays output to the console
2. Text must be inside quotes (single or double)
3. Numbers can be printed directly without quotes
4. Use commas to print multiple values
5. Escape characters: \n (newline), \t (tab), \\ (backslash)

Next Lesson: Comments and Documentation
"""
