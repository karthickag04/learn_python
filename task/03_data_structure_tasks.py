"""
Data structure tasks.

Related course folders:
- 04_data_structures
"""


# TASK 1
# Return the largest, smallest, and average value from a list of marks.
# Return a dictionary: {"largest": ..., "smallest": ..., "average": ...}
def summarize_marks(marks):
    pass


# TASK 2
# Add an item to a shopping cart list only if it is not already present.
# Return the updated cart.
def add_unique_item(cart, item):
    pass


# TASK 3
# Count how many times each word appears in a sentence.
# Return a dictionary.
# Example: "python is fun python" -> {"python": 2, "is": 1, "fun": 1}
def word_count(sentence):
    pass


# TASK 4
# Return common subjects between two students.
# Use sets.
def common_subjects(student1_subjects, student2_subjects):
    pass


# TASK 5
# Format a student tuple.
# Input tuple: ("Ravi", 17, "Chennai")
# Return: "Ravi is 17 years old and lives in Chennai."
def format_student(student_tuple):
    pass


# TASK 6
# Clean a username:
# - remove leading/trailing spaces
# - convert to lowercase
# - replace spaces with underscores
def clean_username(username):
    pass


if __name__ == "__main__":
    assert summarize_marks([80, 90, 70]) == {"largest": 90, "smallest": 70, "average": 80.0}
    assert add_unique_item(["pen"], "pen") == ["pen"]
    assert add_unique_item(["pen"], "book") == ["pen", "book"]
    assert word_count("python is fun python") == {"python": 2, "is": 1, "fun": 1}
    assert common_subjects({"Math", "Python"}, {"Python", "English"}) == {"Python"}
    assert format_student(("Ravi", 17, "Chennai")) == "Ravi is 17 years old and lives in Chennai."
    assert clean_username("  John Doe  ") == "john_doe"
    print("All data-structure checks passed.")

