# Define a class with a constructor that accepts a single parameter
class NewClassWithConstructor:

    # Constructor (__init__ method) is automatically called when an object is created
    def __init__(self, name):
        # Print a welcome message and store the name in an instance variable
        print("Welcome to constructor under the session arranged by ", name)
        self.name = name  # Store the name so it can be used in other methods

    # Define a method to print a message using the name passed during object creation
    def printMsg(self):
        print("Welcome to python class and constructor session and method name is printMsg", self.name)

    # Define a method to print a personalized welcome message based on the name
    def printwelcome(self):
        if self.name == "Gtec":
            print("Hi...", self.name, " welcome to constructor class")
        else:
            print("user is not in the database")  # If name doesn't match, print this message

    # Define a method to print a goodbye message (no condition here)
    def printGoodbye(self):
        print("Welcome to python class and constructor session")

    # Another method to print a fixed message (can be used for testing)
    def printFoOutput(self):
        print("Welcome to python class and constructor session and method name is printforoutput")
   

# Define another class that includes conditional logic using two parameters: name and location
class NewClassWithConstructorForIF:

    # Constructor takes two arguments and stores them
    def __init__(self, name, location):
        print("Welcome to constructor under the session arranged by ", name)
        self.name = name
        self.location = location

    # Same message function as in the previous class
    def printMsg(self):
        print("Welcome to python class and constructor session and method name is printMsg", self.name)

    # Personalized welcome based on name and location using if-elif-else logic
    def printwelcome(self):
        if self.name == "Gtec" and self.location == "Trichy":
            print("Hi...", self.name, " welcome to constructor class under the center location of", self.location)
        elif self.name == "Gtec" and self.location == "Chennai":
            print("Hi...", self.name, " welcome to constructor class under the center location of", self.location)
        else:
            print("user is not in the database")  # No match found

    # Simple goodbye message (common method pattern)
    def printGoodbye(self):
        print("Welcome to python class and constructor session")

    # Additional method with a fixed output
    def printFoOutput(self):
        print("Welcome to python class and constructor session and method name is printforoutput")
   

# Create an object from the first class and call its methods
ncwc = NewClassWithConstructor("Gtec")  # Object created and constructor executed
ncwc.printMsg()         # Calling printMsg method
ncwc.printwelcome()     # Conditional check based on name

# Separator for clarity
print("**********")
print("**********")
print("**********")

# Create an object from the second class with name and location
ncwc = NewClassWithConstructorForIF("Gtec", "Trichy")  # Object created and constructor executed
ncwc.printMsg()         # Calling printMsg method
ncwc.printwelcome()     # Conditional check based on both name and location
