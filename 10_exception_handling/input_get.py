# Exception Handling with Command Line Input
# This script demonstrates how to handle exceptions and get user input

# Run this file from terminal: python input_get.py

try:
    # This will intentionally cause a ZeroDivisionError
    print(22/0)
except ZeroDivisionError as e:
    # When ZeroDivisionError occurs, we handle it by asking user for input
    # input() function reads text from command line (terminal)
    x = input("enter a number: ")      # Gets first number as string
    y = input("enter another number: ")  # Gets second number as string
    
    # Convert strings to integers and perform division
    # Note: This could raise ValueError if user enters non-numeric input
    print(int(x) / int(y))