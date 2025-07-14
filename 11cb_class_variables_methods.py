# Example 2: Class Variables with Instance Method, Class Method, and Static Method
# Focus: How different method types work with CLASS VARIABLES

class School:
    """
    This class demonstrates CLASS VARIABLES with different method types
    Class variables: Shared by ALL instances of the class
    """
    
    # Class variables - shared by all instances
    school_name = "Python High School"              # Public class variable
    _total_students = 0                             # Protected class variable
    __accreditation_id = "PY2025"                   # Private class variable
    
    def __init__(self, student_name):
        self.student_name = student_name            # Instance variable
        School._total_students += 1                 # Modifying class variable from instance method
    
    # INSTANCE METHOD with class variables
    def show_school_info(self):
        """Instance method accessing class variables"""
        print(f"Student: {self.student_name}")                    # ✅ POSSIBLE: Access instance variable
        print(f"School: {School.school_name}")                    # ✅ POSSIBLE: Access public class variable
        print(f"Total Students: {School._total_students}")        # ✅ POSSIBLE: Access protected class variable
        print(f"Accreditation: {School.__accreditation_id}")      # ✅ POSSIBLE: Access private class variable (within class)
    
    # CLASS METHOD with class variables
    @classmethod
    def display_school_stats(cls):
        """Class method can access class variables but NOT instance variables"""
        print(f"School Name: {cls.school_name}")                  # ✅ POSSIBLE: Access public class variable
        print(f"Total Students: {cls._total_students}")           # ✅ POSSIBLE: Access protected class variable
        print(f"Accreditation: {cls.__accreditation_id}")         # ✅ POSSIBLE: Access private class variable
        # print(f"Student Name: {cls.student_name}")              # ❌ NOT POSSIBLE: Cannot access instance variables
    
    @classmethod
    def update_school_name(cls, new_name):
        """Class method can modify class variables"""
        cls.school_name = new_name                                 # ✅ POSSIBLE: Modify class variable
        print(f"School name updated to: {cls.school_name}")
    
    # STATIC METHOD with class variables
    @staticmethod
    def show_static_info():
        """Static method cannot access instance or class variables directly"""
        print("=== Static Method Demo ===")
        # Static methods have NO access to self or cls, so must use class name explicitly
        print(f"School: {School.school_name}")                    # ✅ POSSIBLE: Access via class name
        print(f"Total: {School._total_students}")                 # ✅ POSSIBLE: Access via class name
        print(f"ID: {School._School__accreditation_id}")          # ✅ POSSIBLE: Access private via name mangling
        
        # What's NOT possible in static methods:
        # print(f"School: {cls.school_name}")                     # ❌ NOT POSSIBLE: No cls parameter
        # print(f"Student: {self.student_name}")                  # ❌ NOT POSSIBLE: No self parameter

# Testing the class
print("=== CLASS VARIABLES WITH DIFFERENT METHODS DEMO ===")

# Create instances
student1 = School("John")
student2 = School("Jane")

print("\n--- Instance Method Accessing Class Variables ---")
student1.show_school_info()
print()
student2.show_school_info()

print("\n--- Class Method Accessing Class Variables ---")
School.display_school_stats()

print("\n--- Static Method Accessing Class Variables ---")
School.show_static_info()

print("\n--- Direct Access to Class Variables from Outside ---")
print(f"School Name: {School.school_name}")                      # ✅ POSSIBLE: Public class variable
print(f"Total Students: {School._total_students}")               # ⚠️  POSSIBLE but DISCOURAGED: Protected
# print(f"Accreditation: {School.__accreditation_id}")           # ❌ NOT POSSIBLE: Private class variable

print("\n--- Direct Modification of Class Variables from Outside ---")
School.school_name = "Advanced Python School"                    # ✅ POSSIBLE: Modify public class variable
School._total_students = 100                                     # ⚠️  POSSIBLE but DISCOURAGED: Modify protected
# School.__accreditation_id = "PY2026"                           # ❌ NOT POSSIBLE: Cannot modify private directly

print("\n--- After Direct Modification ---")
School.display_school_stats()

print("\n--- Class Method Modifying Class Variable ---")
School.update_school_name("Elite Python Academy")

print("\n--- What's NOT POSSIBLE with Class Variables ---")
# Class methods cannot access instance variables
# Static methods cannot access variables without explicit class name
# Private class variables cannot be accessed directly from outside
