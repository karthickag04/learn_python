class MyClass:
    public_var = "I am public (class variable)"           # Public class variable
    _protected_var = "I am protected (class variable)"    # Protected class variable
    __private_var = "I am private (class variable)"       # Private class variable

    def __init__(self):
        self.instance_public = "I am public (instance variable)"
        self._instance_protected = "I am protected (instance variable)"
        self.__instance_private = "I am private (instance variable)"

   
    # Instance method demonstrating access
    def show_instance_vars(self):
        print("Instance Public:", self.instance_public)
        print("Instance Protected:", self._instance_protected)
        print("Instance Private:", self.__instance_private)
        # print(self.__private_var)  # Not possible: __private_var is a class variable, not instance

        # # Accessing class variables from instance (possible, but not recommended for private)
        # print("Class Public from instance:", self.public_var)  # Possible
        # print("Class Protected from instance:", self._protected_var)  # Possible
        # # print(self.__private_var)  # Not possible: name mangling prevents direct access

    # Class method demonstrating access
    @classmethod
    def show_class_vars(cls):
        print("Class Public:", cls.public_var)
        print("Class Protected:", cls._protected_var)
        print("Class Private:", cls.__private_var)
        # print(cls.instance_public)  # Not possible: instance variable, not accessible from class

    # # # Static method (cannot access instance or class variables directly)
    @staticmethod
    def static_method_demo():
        print("Static methods can't access instance or class variables directly.")
        print("Class Public:", MyClass.public_var)
        print("Class Protected:", MyClass._protected_var)
        print("Class Private:", MyClass._MyClass__private_var)

        # print("Instance Public:", self.instance_public) # Not possible: no self in static method
        # print("Instance Protected:", self._instance_protected) # Not possible: no self in static method
        # print("Instance Private:", self.__instance_private)  # Not possible: no self in static method
        # print(MyClass.public_var)  # Possible, but not recommended (should use classmethod)
        # print(self.instance_public)  # Not possible: no self in static method

# Example usage:
obj = MyClass()
obj.show_instance_vars()
obj.public_var = "Modified public variable"
obj._protected_var = "Modified protected variable"
obj.__private_var = "Modified private variable"  # This won't change the class variable, due to name mangling
obj.show_instance_vars()
# # print("---")
# MyClass.show_class_vars()

# MyClass.public_var = "Modified public variable"
# MyClass._protected_var = "Modified protected variable"
# MyClass.__private_var = "Modified private variable"
# MyClass.show_class_vars()

# print("---")
# obj.static_method_demo()
# print("---")
# print("---")
# print("---")
# print("---")
# print("Class Public:", MyClass.public_var)
# print("Class Protected:", MyClass._protected_var)
# print("Class Private:", MyClass.__private_var)

# # Direct access examples:
# print(obj.instance_public)         # Possible
# print(obj._instance_protected)     # Possible (but discouraged)
# print(obj.__instance_private)      # Not possible: AttributeError due to name mangling
# print(MyClass.public_var)          # Possible
# print(MyClass._protected_var)      # Possible (but discouraged)
# print(MyClass.__private_var)       # Not possible: AttributeError due to name mangling
