from abc import ABC, abstractmethod

# ==========================================
# BLOCK 1: THE BLUEPRINT (Operation ABC)
# Workflow: This block defines the 'rules' for all mathematical operations.
# Every operation must have a 'calculate' method.
# ==========================================
# 1. ABSTRACTION (Logic used: Abstract Base Class)
class Operation(ABC):
    
    @abstractmethod
    def calculate(self, a, b):
        """This method MUST be implemented by any child class."""
        pass

# ==========================================
# BLOCK 2: THE REAL TOOLS (Concrete Subclasses)
# Workflow: These blocks implement the actual math logic for each specific type.
# Each class 'overrides' the calculate method from the Blueprint.
# ==========================================
# 2. INHERITANCE (Logic used: Child classes inheriting from Parent)
class Addition(Operation):
    def calculate(self, a, b):
        return a + b

class Subtraction(Operation):
    def calculate(self, a, b):
        return a - b

class Multiplication(Operation):
    def calculate(self, a, b):
        return a * b

class Division(Operation):
    def calculate(self, a, b):
        # Basic validation: Preventing errors before they happen
        if b == 0:
            return "Error: Division by zero!"
        return a / b

# ==========================================
# BLOCK 3: THE MANAGER (Calculator Class)
# Workflow: This block acts as the brain. It manages the operations,
# stores the history, and provides a clean way to interact with the math logic.
# ==========================================
# 3. ENCAPSULATION (Logic used: Private attributes and methods)
class Calculator:
    def __init__(self):
        # Setup: Create a private list to hold the history of calculations
        self.__history = []

    def perform_operation(self, operation_obj, a, b):
        # Workflow Step:
        # 1. Take an operation (like Addition) and two numbers.
        # 2. Call the common 'calculate' method (Polymorphism).
        # 3. Store the result in history.
        # 4. Return the answer to the user.
        
        # 4. POLYMORPHISM (Logic used: Unified interface)
        result = operation_obj.calculate(a, b)
        
        # Keep a record: Class name tells us which operation was used
        self.__history.append(f"{a} {operation_obj.__class__.__name__} {b} = {result}")
        return result

    def show_history(self):
        # Workflow: Print all stored records in a pretty format
        print("\n--- Calculation History ---")
        if not self.__history:
            print("No calculations yet.")
        for record in self.__history:
            print(record)
        print("---------------------------\n")

# ==========================================
# BLOCK 4: THE USER INTERFACE (Main Menu)
# Workflow: This is the entry point. It handles user input in a loop,
# calls the Manager (Calculator), and displays the results.
# ==========================================
def main():
    # 1. Initialize the Calculator brain
    calc = Calculator()
    
    # 2. Map user choices to the actual classes (Objects)
    operations = {
        "1": (Addition(), "Addition"),
        "2": (Subtraction(), "Subtraction"),
        "3": (Multiplication(), "Multiplication"),
        "4": (Division(), "Division")
    }

    print("Welcome to the OOP Terminal Calculator!")
    
    # 3. Start the Interaction Loop
    while True:
        # Display Menu
        print("\nAvailable Operations:")
        for key, value in operations.items():
            print(f"{key}. {value[1]}")
        print("5. Show History")
        print("6. Exit")

        # Get User Choice
        choice = input("\nEnter choice (1-6): ")

        if choice == "6":
            print("Goodbye!")
            break
        
        if choice == "5":
            calc.show_history()
            continue

        if choice in operations:
            try:
                # Get User Inputs
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                # Retrieve the operation object based on choice
                op_obj, op_name = operations[choice]
                
                # Execute the operation via the Calculator manager
                result = calc.perform_operation(op_obj, num1, num2)
                
                print(f"\nResult of {op_name}: {result}")
            except ValueError:
                print("Invalid input! Please enter numbers.")
        else:
            print("Invalid choice! Please select 1-6.")

# ==========================================
# STARTING THE PROGRAM
# Workflow: Ensures the main function runs only when this file is executed.
# ==========================================
if __name__ == "__main__":
    main()
