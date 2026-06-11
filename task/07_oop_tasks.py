"""
OOP basics tasks.

Related course folders:
- 08_oop_basics
"""


# TASK 1
# Create a Student class.
# Requirements:
# - attributes: name, roll_no, marks
# - method average_marks() returns average
# - method has_passed() returns True if average >= 50
class Student:
    pass


# TASK 2
# Create a BankAccount class.
# Requirements:
# - attributes: account_holder, balance
# - deposit(amount)
# - withdraw(amount), return "Insufficient balance" if amount is too high
# - get_balance()
class BankAccount:
    pass


# TASK 3
# Create a Product class.
# Requirements:
# - class variable tax_percent = 18
# - attributes: name, price
# - method final_price() returns price including tax
class Product:
    pass


if __name__ == "__main__":
    student = Student("Anu", 101, [80, 70, 90])
    assert student.average_marks() == 80.0
    assert student.has_passed() is True

    account = BankAccount("Ravi", 1000)
    account.deposit(500)
    assert account.get_balance() == 1500
    assert account.withdraw(2000) == "Insufficient balance"

    product = Product("Keyboard", 1000)
    assert product.final_price() == 1180.0
    print("All OOP basics checks passed.")

