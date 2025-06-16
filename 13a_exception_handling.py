# Class to handle various exceptions with separate methods for each exception type
class ExceptionHandler:
    # Method to handle ArithmeticError
    def handle_arithmetic_error(self, numerator, denominator):
        """Handles division and catches ArithmeticError."""
        try:
            result = numerator / denominator
            print("Result:", result)
        except ArithmeticError as e:
            print("ArithmeticError occurred:", e)

    # Method to handle AssertionError
    def handle_assertion_error(self, condition, message):
        """Handles assertion and catches AssertionError."""
        try:
            assert condition, message
            print("Assertion passed.")
        except AssertionError as e:
            print("AssertionError occurred:", e)

    # Method to handle AttributeError
    def handle_attribute_error(self, obj, attribute):
        """Tries to access an attribute and catches AttributeError."""
        try:
            print(getattr(obj, attribute))
        except AttributeError as e:
            print("AttributeError occurred:", e)

    # Method to handle EOFError
    def handle_eof_error(self):
        """Handles EOFError when input is unexpectedly terminated."""
        try:
            data = input("Enter something (Ctrl+D to trigger EOF): ")
            print("You entered:", data)
        except EOFError as e:
            print("EOFError occurred:", e)

    # Method to handle FileNotFoundError
    def handle_file_not_found_error(self, filename):
        """Tries to open a file and catches FileNotFoundError."""
        try:
            with open(filename, 'r') as file:
                print(file.read())
        except FileNotFoundError as e:
            print("FileNotFoundError occurred:", e)

    # Method to handle IndexError
    def handle_index_error(self, lst, index):
        """Tries to access a list index and catches IndexError."""
        try:
            print(lst[index])
        except IndexError as e:
            print("IndexError occurred:", e)

    # Method to handle KeyError
    def handle_key_error(self, dictionary, key):
        """Tries to access a dictionary key and catches KeyError."""
        try:
            print(dictionary[key])
        except KeyError as e:
            print("KeyError occurred:", e)

    # Method to handle ZeroDivisionError
    def handle_zero_division_error(self, numerator, denominator):
        """Handles division and catches ZeroDivisionError."""
        try:
            result = numerator / denominator
            print("Result:", result)
        except ZeroDivisionError as e:
            print("ZeroDivisionError occurred:", e)

# Example usage
if __name__ == "__main__":
    handler = ExceptionHandler()

    # Example calls to the methods
    handler.handle_arithmetic_error(10, 0)
    handler.handle_assertion_error(2 > 3, "2 is not greater than 3")
    handler.handle_attribute_error([], "non_existent_attribute")
    handler.handle_eof_error()
    handler.handle_file_not_found_error("non_existent_file.txt")
    handler.handle_index_error([1, 2, 3], 5)
    handler.handle_key_error({"key1": "value1"}, "key2")
    handler.handle_zero_division_error(10, 0)