# Example 4: Advanced Concepts and Edge Cases
# Focus: Tricky scenarios and common mistakes

class BankAccount:
    """
    Advanced demonstration showing edge cases and common mistakes
    """
    
    # Class variables
    bank_name = "Python Bank"                       # Public class variable
    _interest_rate = 0.05                          # Protected class variable
    __security_key = "SECURE123"                   # Private class variable
    total_accounts = 0                             # Public class variable for counting
    
    def __init__(self, account_holder, initial_balance):
        # Instance variables
        self.account_holder = account_holder        # Public instance variable
        self._account_number = f"ACC{BankAccount.total_accounts + 1:03d}"  # Protected
        self.__balance = initial_balance            # Private instance variable
        BankAccount.total_accounts += 1             # Increment class variable
    
    # Instance method showing TRICKY SCENARIOS
    def demonstrate_tricky_access(self):
        """Showing some tricky access scenarios"""
        print("=== Tricky Access Scenarios ===")
        
        # 1. Accessing class variable through instance (creates confusion)
        print(f"Bank name via instance: {self.bank_name}")        # ✅ POSSIBLE but confusing
        print(f"Bank name via class: {BankAccount.bank_name}")    # ✅ BETTER practice
        
        # 2. What happens when you assign to class variable via instance?
        self.bank_name = "My Personal Bank"                       # Creates NEW instance variable!
        print(f"After assignment - instance: {self.bank_name}")   # Shows "My Personal Bank"
        print(f"After assignment - class: {BankAccount.bank_name}") # Still shows "Python Bank"
        
        # 3. Accessing private variables within class
        print(f"Balance (private): {self.__balance}")             # ✅ POSSIBLE within class
    
    # Instance method showing COMMON MISTAKES
    def common_mistakes_demo(self):
        """Demonstrating common mistakes people make"""
        print("=== Common Mistakes Demo ===")
        
        # Mistake 1: Thinking instance assignment changes class variable
        print(f"Original class interest rate: {BankAccount._interest_rate}")
        self._interest_rate = 0.10                                # This creates instance variable!
        print(f"Instance interest rate: {self._interest_rate}")   # 0.10
        print(f"Class interest rate: {BankAccount._interest_rate}") # Still 0.05
        
        # Mistake 2: Trying to access private variables incorrectly
        # print(f"Balance: {self.__balance}")                     # ✅ WORKS within class
    
    # Class method showing what it CAN and CANNOT do
    @classmethod
    def class_method_limitations(cls):
        """Class method showing its limitations"""
        print("=== Class Method Limitations ===")
        
        print(f"✅ Can access bank name: {cls.bank_name}")
        print(f"✅ Can access total accounts: {cls.total_accounts}")
        print(f"✅ Can access private class var: {cls.__security_key}")
        
        # What class methods CANNOT do:
        # print(f"❌ Cannot access account holder: {cls.account_holder}")  # No instance context
        # print(f"❌ Cannot access balance: {cls.__balance}")              # No instance context
    
    # Static method showing access patterns
    @staticmethod
    def static_method_patterns():
        """Static method showing different access patterns"""
        print("=== Static Method Access Patterns ===")
        
        # Only way to access variables in static method is via class name
        print(f"✅ Bank name: {BankAccount.bank_name}")
        print(f"✅ Total accounts: {BankAccount.total_accounts}")
        print(f"✅ Interest rate: {BankAccount._interest_rate}")
        
        # Accessing private class variable via name mangling
        print(f"✅ Security key: {BankAccount._BankAccount__security_key}")
        
        # What static methods CANNOT do:
        # print(f"❌ Cannot use self: {self.account_holder}")      # No self parameter
        # print(f"❌ Cannot use cls: {cls.bank_name}")             # No cls parameter
    
    def show_balance(self):
        """Simple method to show balance"""
        print(f"Balance for {self.account_holder}: ${self.__balance}")

# Testing advanced concepts
print("=== ADVANCED CONCEPTS AND EDGE CASES ===")

# Create accounts
account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 2000)

print("\n--- Basic Info ---")
account1.show_balance()
account2.show_balance()
print(f"Total accounts created: {BankAccount.total_accounts}")

print("\n--- Tricky Access Scenarios ---")
account1.demonstrate_tricky_access()

print("\n--- Common Mistakes ---")
account1.common_mistakes_demo()

print("\n--- Class Method Limitations ---")
BankAccount.class_method_limitations()

print("\n--- Static Method Access Patterns ---")
BankAccount.static_method_patterns()

print("\n--- The Confusion of Instance vs Class Variables ---")
print("Before any changes:")
print(f"Account1 bank_name: {account1.bank_name}")               # From class
print(f"Account2 bank_name: {account2.bank_name}")               # From class
print(f"Class bank_name: {BankAccount.bank_name}")               # Class variable

# This creates an INSTANCE variable, not modifying class variable
account1.bank_name = "Alice's Bank"

print("\nAfter account1.bank_name = 'Alice's Bank':")
print(f"Account1 bank_name: {account1.bank_name}")               # Instance variable
print(f"Account2 bank_name: {account2.bank_name}")               # Still from class
print(f"Class bank_name: {BankAccount.bank_name}")               # Unchanged

# To actually change class variable, use class name
BankAccount.bank_name = "Global Python Bank"

print("\nAfter BankAccount.bank_name = 'Global Python Bank':")
print(f"Account1 bank_name: {account1.bank_name}")               # Still instance variable
print(f"Account2 bank_name: {account2.bank_name}")               # Now from updated class
print(f"Class bank_name: {BankAccount.bank_name}")               # Updated

print("\n=== KEY TAKEAWAYS ===")
print("""
1. Instance variable assignment via instance (self.var = value) creates/modifies instance variable
2. Class variable assignment via instance (instance.class_var = value) creates NEW instance variable
3. Class variable assignment via class (Class.class_var = value) modifies class variable for all
4. Private variables use name mangling: __var becomes _ClassName__var
5. Instance methods: ✅ Access both instance and class variables
6. Class methods: ✅ Access class variables, ❌ Cannot access instance variables
7. Static methods: ✅ Access via class name only, ❌ No direct access to any variables
8. Outside class: ✅ Public access, ⚠️ Protected (discouraged), ❌ Private (need name mangling)
""")
