"""
Mini project tasks.

Related course folders:
- practice_projects
"""


# PROJECT 1: Student Management Lite
# Build these functions using a list of dictionaries.

def add_student(students, roll_no, name, marks):
    """Add one student and return the updated list."""
    pass


def find_student(students, roll_no):
    """Return the student dictionary for the roll number, or None."""
    pass


def class_average(students):
    """Return average marks of the class."""
    pass


# PROJECT 2: Calculator With History

def calculate_with_history(history, a, operator, b):
    """
    Perform a calculation and store it in history.
    Return tuple: (result, updated_history)
    History item example: "10 + 5 = 15"
    """
    pass


# PROJECT 3: Contact Book Lite

def add_contact(contacts, name, phone, email):
    """Add a contact dictionary and return updated contacts."""
    pass


def search_contacts(contacts, keyword):
    """Return all contacts where keyword appears in name, phone, or email."""
    pass


# PROJECT 4: Quiz Game Lite

def check_answer(question, user_answer):
    """
    question example:
    {"question": "2 + 2?", "answer": "4"}
    Return True if user_answer matches answer, ignoring case and extra spaces.
    """
    pass


def calculate_score(questions, user_answers):
    """Return total correct answers."""
    pass


if __name__ == "__main__":
    students = []
    students = add_student(students, 1, "Anu", 90)
    assert find_student(students, 1)["name"] == "Anu"
    assert class_average(students) == 90.0

    history = []
    result, history = calculate_with_history(history, 10, "+", 5)
    assert result == 15
    assert history == ["10 + 5 = 15"]

    contacts = add_contact([], "Ravi", "9876543210", "ravi@example.com")
    assert len(search_contacts(contacts, "ravi")) == 1

    questions = [{"question": "2 + 2?", "answer": "4"}, {"question": "Python type?", "answer": "language"}]
    assert check_answer(questions[0], " 4 ") is True
    assert calculate_score(questions, ["4", "wrong"]) == 1
    print("All mini-project checks passed.")

