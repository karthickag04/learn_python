class College:
    def __init__(self, name, location, founded_year):
        self.name = name
        self.location = location
        self.founded_year = founded_year
        self.departments = []
        self.students = []
        self.professors = []

    def add_department(self, department_name):
        if department_name not in self.departments:
            self.departments.append(department_name)
            print(f"Department '{department_name}' added to {self.name}.")
        else:
            print(f"Department '{department_name}' already exists in {self.name}.")

    def remove_department(self, department_name):
        if department_name in self.departments:
            self.departments.remove(department_name)
            print(f"Department '{department_name}' removed from {self.name}.")
        else:
            print(f"Department '{department_name}' not found in {self.name}.")

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            print(f"Student '{student.name}' added to {self.name}.")
        else:
            print(f"Student '{student.name}' already enrolled in {self.name}.")

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
            print(f"Student '{student.name}' removed from {self.name}.")
        else:
            print(f"Student '{student.name}' not found in {self.name}.")

    def add_professor(self, professor):
        if professor not in self.professors:
            self.professors.append(professor)
            print(f"Professor '{professor.name}' added to {self.name}.")
        else:
            print(f"Professor '{professor.name}' already working at {self.name}.")

    def remove_professor(self, professor):
        if professor in self.professors:
            self.professors.remove(professor)
            print(f"Professor '{professor.name}' removed from {self.name}.")
        else:
            pass


collegOBJ = College("BHC","Trichy", 1990)

collegOBJ.add_department("CSE")
collegOBJ.add_department("ECE")