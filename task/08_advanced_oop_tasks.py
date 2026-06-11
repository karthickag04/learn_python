"""
Advanced OOP tasks.

Related course folders:
- 09_oop_advanced
"""

from abc import ABC, abstractmethod


# TASK 1
# Create a base class Employee.
# Requirements:
# - attributes: name, base_salary
# - method calculate_salary() returns base_salary
class Employee:
    pass


# TASK 2
# Create Manager that inherits Employee.
# Requirements:
# - extra attribute: bonus
# - calculate_salary() returns base_salary + bonus
class Manager:
    pass


# TASK 3
# Create Developer that inherits Employee.
# Requirements:
# - extra attribute: overtime_pay
# - calculate_salary() returns base_salary + overtime_pay
class Developer:
    pass


# TASK 4
# Create an abstract Shape class with abstract method area().
# Then create Rectangle and Circle classes that implement area().
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle:
    pass


class Circle:
    pass


if __name__ == "__main__":
    employees = [Manager("Meena", 50000, 10000), Developer("Arun", 40000, 5000)]
    assert [employee.calculate_salary() for employee in employees] == [60000, 45000]

    rectangle = Rectangle(5, 4)
    circle = Circle(7)
    assert rectangle.area() == 20
    assert round(circle.area(), 2) == 153.94
    print("All advanced OOP checks passed.")

