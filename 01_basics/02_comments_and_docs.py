"""
==============================================
LESSON 02: Comments and Documentation
==============================================

Comments are notes in your code that Python ignores.
They help you and others understand what your code does.

Real-World Use Case:
- Explaining complex logic
- Documenting functions and classes
- Temporarily disabling code for testing
- Adding TODO notes for future work
"""

# ==============================================
# 1. SINGLE LINE COMMENTS
# ==============================================

# This is a single line comment - starts with #
# Python ignores everything after the # symbol

# Comments can explain what code does:
age = 25  # Store the user's age

# Comments can explain WHY something is done:
price = price * 0.9  # Apply 10% discount for members

# Comments can mark sections of code:
# ---- User Authentication ----
# ---- Database Operations ----


# ==============================================
# 2. MULTI-LINE COMMENTS (DOCSTRINGS)
# ==============================================

"""
This is a multi-line comment using triple quotes.
It can span multiple lines without needing # on each line.

Use this for:
- Longer explanations
- Documentation
- Temporarily commenting out blocks of code
"""

"""
You can also use single quotes for multi-line comments.
Both triple double-quotes and triple single-quotes work the same way.
"""


# ==============================================
# 3. DOCSTRINGS - DOCUMENTING FUNCTIONS/CLASSES
# ==============================================

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Parameters:
        length (float): The length of the rectangle
        width (float): The width of the rectangle
    
    Returns:
        float: The area of the rectangle
    
    Example:
        >>> calculate_area(5, 3)
        15
    """
    return length * width


def greet_user(name, greeting="Hello"):
    """
    Display a personalized greeting message.
    
    Args:
        name (str): The name of the user
        greeting (str, optional): The greeting word. Defaults to "Hello".
    
    Returns:
        str: The complete greeting message
    """
    return f"{greeting}, {name}!"


# ==============================================
# 4. COMMENTING BEST PRACTICES
# ==============================================

# ❌ BAD: Obvious comments (don't state the obvious)
x = 5  # Set x to 5

# ✅ GOOD: Explain WHY, not WHAT
x = 5  # Default retry count for API calls

# ❌ BAD: Outdated or incorrect comments
a, b = 10, 20  # Define two numbers
# Calculate sum of two numbers
result = a * b  # This multiplies, not sums! (Comment is wrong)

# ✅ GOOD: Keep comments updated with code
# Calculate product of two numbers
result = a * b


# ==============================================
# 5. TODO AND FIXME COMMENTS
# ==============================================

# TODO: Add input validation for negative numbers
# FIXME: This function crashes when list is empty
# NOTE: This algorithm has O(n²) complexity
# HACK: Temporary fix until API is updated
# XXX: Critical bug - needs immediate attention


# ==============================================
# 6. SECTION DIVIDERS
# ==============================================

# ==================================================
# CONFIGURATION SECTION
# ==================================================

# --------------------------------------------------
# Helper Functions
# --------------------------------------------------

# ############## DATABASE OPERATIONS ##############


# ==============================================
# 7. REAL-WORLD EXAMPLE: DOCUMENTED CODE
# ==============================================

class ShoppingCart:
    """
    A class to represent a shopping cart for an e-commerce platform.
    
    Attributes:
        items (list): List of items in the cart
        discount_code (str): Applied discount code, if any
    
    Example:
        >>> cart = ShoppingCart()
        >>> cart.add_item("Laptop", 999.99)
        >>> cart.get_total()
        999.99
    """
    
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = []  # Store items as (name, price) tuples
        self.discount_code = None
    
    def add_item(self, name, price):
        """
        Add an item to the cart.
        
        Args:
            name (str): Product name
            price (float): Product price
        
        Raises:
            ValueError: If price is negative
        """
        # Validate price before adding
        if price < 0:
            raise ValueError("Price cannot be negative")
        
        self.items.append((name, price))
    
    def get_total(self):
        """
        Calculate the total price of all items.
        
        Returns:
            float: Total price of items in cart
        
        Note:
            Does not include tax or shipping
        """
        # Sum up all item prices
        return sum(price for name, price in self.items)


# ==============================================
# 8. COMMENTING OUT CODE FOR DEBUGGING
# ==============================================

def process_data(data):
    # Original implementation (keeping for reference)
    # result = slow_algorithm(data)
    
    # New optimized version
    result = data  # Placeholder: fast_algorithm(data)
    
    # Debug: Print intermediate results
    # print(f"Debug: result = {result}")
    
    return result


# ==============================================
# PRACTICE EXERCISES
# ==============================================
"""
Try these exercises:

1. Write a function with a proper docstring
2. Add comments explaining a complex calculation
3. Create section dividers for organizing code
4. Add TODO comments for future improvements
5. Document a class with attributes and methods
"""


# ==============================================
# SUMMARY
# ==============================================
"""
Key Points:
1. Use # for single-line comments
2. Use triple quotes (''' or \""") for multi-line comments
3. Docstrings document functions, classes, and modules
4. Comment WHY, not WHAT (avoid obvious comments)
5. Use TODO, FIXME, NOTE for tracking issues
6. Keep comments updated when code changes

Next Lesson: Variables and Naming Conventions
"""
