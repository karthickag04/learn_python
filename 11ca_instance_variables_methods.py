# Example 1: Instance Variables and Instance Methods
# Focus: How instance methods work with instance variables

class StudentRecord:
    """
    This class demonstrates INSTANCE VARIABLES and INSTANCE METHODS
    Instance variables: Belong to each individual object/instance
    Instance methods: Can access and modify instance variables
    """
    
    def __init__(self, name, roll_no):
        # Instance variables - each object has its own copy
        self.name = name                           # Public instance variable
        self._roll_no = roll_no                    # Protected instance variable (by convention)
        self.__grade = "A"                         # Private instance variable (name mangling)
    
    # Instance method - can access ALL instance variables
    def display_student_info(self):
        """Instance method accessing all types of instance variables"""
        print(f"Name: {self.name}")               # ✅ POSSIBLE: Access public instance variable
        print(f"Roll No: {self._roll_no}")        # ✅ POSSIBLE: Access protected instance variable
        print(f"Grade: {self.__grade}")           # ✅ POSSIBLE: Access private instance variable (within class)
    
    # Instance method to update variables
    def update_grade(self, new_grade):
        """Instance method can modify instance variables"""
        self.__grade = new_grade                   # ✅ POSSIBLE: Modify private variable within class
        print(f"Grade updated to: {self.__grade}")
    
    # Instance method showing what's NOT possible
    def demonstrate_limitations(self):
        """Showing what instance methods CANNOT do"""
        # Instance methods cannot directly access class variables that don't exist
        # print(f"School Name: {self.school_name}")  # ❌ NOT POSSIBLE: No such class variable defined

# Creating objects and testing
print("=== INSTANCE VARIABLES AND METHODS DEMO ===")

# Create two different objects
student1 = StudentRecord("Alice", 101)
student2 = StudentRecord("Bob", 102)

print("\n--- Student 1 Info ---")
student1.display_student_info()

print("\n--- Student 2 Info ---")
student2.display_student_info()

print("\n--- Direct Access from Outside Class ---")
print(f"Student1 Name: {student1.name}")           # ✅ POSSIBLE: Public access
print(f"Student1 Roll: {student1._roll_no}")       # ⚠️  POSSIBLE but DISCOURAGED: Protected access
# print(f"Student1 Grade: {student1.__grade}")     # ❌ NOT POSSIBLE: AttributeError due to name mangling

print("\n--- Direct Modification from Outside Class ---")
student1.name = "Alice Smith"                       # ✅ POSSIBLE: Modify public variable
student1._roll_no = 201                            # ⚠️  POSSIBLE but DISCOURAGED: Modify protected
# student1.__grade = "B"                           # ❌ NOT POSSIBLE: Creates new attribute, doesn't modify original

print("\n--- After Modification ---")
student1.display_student_info()

print("\n--- Accessing Private Variable (Name Mangling) ---")
# Python name mangling makes private variables accessible but with modified name
print(f"Grade via name mangling: {student1._StudentRecord__grade}")  # ✅ POSSIBLE but NOT RECOMMENDED

print("\n--- What's NOT POSSIBLE with Instance Variables ---")
# student1.__grade = "C"                           # ❌ This creates NEW attribute, doesn't modify original
# print(student1.__grade)                          # ❌ This would show the NEW attribute, not original
