# Example 3: Complete Demonstration - Instance vs Class Variables/Methods
# Focus: Side-by-side comparison and what's possible vs not possible

class Library:
    """
    Complete demonstration of Instance vs Class concepts
    This class shows ALL combinations and what works vs what doesn't
    """
    
    # CLASS VARIABLES (shared by all instances)
    library_name = "Central Library"                # Public class variable
    _book_limit = 5                                 # Protected class variable
    __admin_code = "LIB123"                         # Private class variable
    
    def __init__(self, member_name, member_id):
        # INSTANCE VARIABLES (unique to each object)
        self.member_name = member_name              # Public instance variable
        self._member_id = member_id                 # Protected instance variable
        self.__books_borrowed = 0                   # Private instance variable
    
    # INSTANCE METHOD - can access BOTH instance and class variables
    def show_member_details(self):
        """Instance method: ✅ CAN access both instance and class variables"""
        print("=== Instance Method Demo ===")
        # Accessing instance variables
        print(f"Member: {self.member_name}")                      # ✅ POSSIBLE
        print(f"ID: {self._member_id}")                           # ✅ POSSIBLE
        print(f"Books Borrowed: {self.__books_borrowed}")         # ✅ POSSIBLE
        
        # Accessing class variables from instance method
        print(f"Library: {Library.library_name}")                 # ✅ POSSIBLE (recommended)
        print(f"Book Limit: {Library._book_limit}")               # ✅ POSSIBLE
        print(f"Admin Code: {Library.__admin_code}")              # ✅ POSSIBLE (within class)
    
    def borrow_book(self):
        """Instance method modifying both instance and class variables"""
        if self.__books_borrowed < Library._book_limit:
            self.__books_borrowed += 1                             # ✅ POSSIBLE: Modify instance variable
            print(f"Book borrowed! Total: {self.__books_borrowed}")
        else:
            print("Book limit reached!")
    
    # CLASS METHOD - can access ONLY class variables
    @classmethod
    def show_library_info(cls):
        """Class method: ✅ CAN access class variables, ❌ CANNOT access instance variables"""
        print("=== Class Method Demo ===")
        print(f"Library Name: {cls.library_name}")                # ✅ POSSIBLE
        print(f"Book Limit: {cls._book_limit}")                   # ✅ POSSIBLE
        print(f"Admin Code: {cls.__admin_code}")                  # ✅ POSSIBLE
        
        # What's NOT possible in class methods:
        # print(f"Member: {cls.member_name}")                     # ❌ NOT POSSIBLE: Instance variable
        # print(f"Books: {cls.__books_borrowed}")                 # ❌ NOT POSSIBLE: Instance variable
    
    @classmethod
    def change_book_limit(cls, new_limit):
        """Class method modifying class variable"""
        cls._book_limit = new_limit                                # ✅ POSSIBLE
        print(f"Book limit changed to: {cls._book_limit}")
    
    # STATIC METHOD - NO direct access to instance or class variables
    @staticmethod
    def library_rules():
        """Static method: ❌ CANNOT access instance or class variables directly"""
        print("=== Static Method Demo ===")
        print("Library Rules:")
        print("1. Return books on time")
        print("2. Keep books in good condition")
        
        # Accessing class variables via class name (only way in static method)
        print(f"Max books allowed: {Library._book_limit}")        # ✅ POSSIBLE via class name
        print(f"Library: {Library.library_name}")                 # ✅ POSSIBLE via class name
        
        # What's NOT possible in static methods:
        # print(f"Member: {self.member_name}")                    # ❌ NOT POSSIBLE: No self
        # print(f"Library: {cls.library_name}")                   # ❌ NOT POSSIBLE: No cls
    
    # Method showing what's NOT POSSIBLE
    def demonstrate_restrictions(self):
        """Demonstrating access restrictions"""
        print("=== What's NOT POSSIBLE ===")
        
        # These would cause AttributeError:
        # print(self.non_existent_variable)                       # ❌ Variable doesn't exist
        
        # Private variables from outside need name mangling:
        print(f"Admin code via name mangling: {Library._Library__admin_code}")  # ✅ POSSIBLE but not recommended

# Testing all concepts
print("=== COMPLETE DEMONSTRATION ===")

# Create instances
member1 = Library("Alice", "M001")
member2 = Library("Bob", "M002")

print("\n--- Instance Methods with Instance and Class Variables ---")
member1.show_member_details()
print()
member2.show_member_details()

print("\n--- Instance Method Modifying Variables ---")
member1.borrow_book()
member1.borrow_book()

print("\n--- Class Method with Class Variables Only ---")
Library.show_library_info()

print("\n--- Static Method with No Direct Variable Access ---")
Library.library_rules()

print("\n--- Direct Access from Outside Class ---")
print("✅ POSSIBLE:")
print(f"Member name: {member1.member_name}")                     # Public instance variable
print(f"Library name: {Library.library_name}")                  # Public class variable

print("\n⚠️  POSSIBLE but DISCOURAGED:")
print(f"Member ID: {member1._member_id}")                        # Protected instance variable
print(f"Book limit: {Library._book_limit}")                     # Protected class variable

print("\n❌ NOT POSSIBLE (will cause AttributeError):")
# print(f"Books borrowed: {member1.__books_borrowed}")           # Private instance variable
# print(f"Admin code: {Library.__admin_code}")                   # Private class variable

print("\n--- Name Mangling for Private Variables ---")
print(f"Books borrowed: {member1._Library__books_borrowed}")     # ✅ POSSIBLE but not recommended
print(f"Admin code: {Library._Library__admin_code}")            # ✅ POSSIBLE but not recommended

print("\n--- Class Method Modifying Class Variable ---")
Library.change_book_limit(10)
Library.show_library_info()

print("\n=== SUMMARY OF WHAT'S POSSIBLE vs NOT POSSIBLE ===")
print("""
INSTANCE METHODS:
✅ CAN access: Instance variables (all types)
✅ CAN access: Class variables (all types)
✅ CAN modify: Instance variables
✅ CAN modify: Class variables

CLASS METHODS:
✅ CAN access: Class variables (all types)
✅ CAN modify: Class variables
❌ CANNOT access: Instance variables
❌ CANNOT modify: Instance variables

STATIC METHODS:
✅ CAN access: Class variables (via class name only)
❌ CANNOT access: Instance variables
❌ CANNOT access: Class variables directly (need class name)

OUTSIDE CLASS:
✅ CAN access: Public variables (instance and class)
⚠️  CAN access: Protected variables (but discouraged)
❌ CANNOT access: Private variables (without name mangling)
✅ CAN modify: Public variables
⚠️  CAN modify: Protected variables (but discouraged)
❌ CANNOT modify: Private variables directly
""")
