# PRACTICE PROJECT: Student Management System
# A complete CRUD application demonstrating OOP, exception handling, and file I/O

import json
from abc import ABC, abstractmethod
from datetime import datetime

# ============================================================================
# EXCEPTIONS
# ============================================================================

class StudentError(Exception):
    """Base exception for student operations"""
    pass

class StudentNotFoundError(StudentError):
    """Raised when student is not found"""
    def __init__(self, student_id):
        super().__init__(f"Student with ID {student_id} not found")
        self.student_id = student_id

class DuplicateStudentError(StudentError):
    """Raised when trying to add duplicate student"""
    def __init__(self, student_id):
        super().__init__(f"Student with ID {student_id} already exists")
        self.student_id = student_id

class ValidationError(StudentError):
    """Raised for validation errors"""
    pass

# ============================================================================
# MODELS
# ============================================================================

class Student:
    """Student model with validation"""
    
    VALID_GRADES = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D', 'F']
    GRADE_POINTS = {
        'A+': 4.0, 'A': 4.0, 'A-': 3.7,
        'B+': 3.3, 'B': 3.0, 'B-': 2.7,
        'C+': 2.3, 'C': 2.0, 'C-': 1.7,
        'D': 1.0, 'F': 0.0
    }
    
    def __init__(self, student_id, name, email, grades=None):
        self._student_id = None
        self._name = None
        self._email = None
        self._grades = {}
        self._created_at = datetime.now()
        
        # Use setters for validation
        self.student_id = student_id
        self.name = name
        self.email = email
        
        if grades:
            for course, grade in grades.items():
                self.add_grade(course, grade)
    
    # Properties with validation
    @property
    def student_id(self):
        return self._student_id
    
    @student_id.setter
    def student_id(self, value):
        if not value or len(str(value)) < 3:
            raise ValidationError("Student ID must be at least 3 characters")
        self._student_id = str(value).upper()
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value or len(value.strip()) < 2:
            raise ValidationError("Name must be at least 2 characters")
        self._name = value.strip().title()
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if not value or '@' not in value:
            raise ValidationError("Invalid email format")
        self._email = value.lower().strip()
    
    @property
    def gpa(self):
        if not self._grades:
            return 0.0
        total = sum(self.GRADE_POINTS.get(g, 0) for g in self._grades.values())
        return round(total / len(self._grades), 2)
    
    @property
    def status(self):
        gpa = self.gpa
        if gpa >= 3.5:
            return "Dean's List"
        elif gpa >= 2.0:
            return "Good Standing"
        elif gpa > 0:
            return "Academic Probation"
        return "No Grades"
    
    def add_grade(self, course, grade):
        """Add a grade for a course"""
        grade = grade.upper()
        if grade not in self.VALID_GRADES:
            raise ValidationError(f"Invalid grade: {grade}")
        self._grades[course] = grade
    
    def remove_grade(self, course):
        """Remove a grade"""
        if course in self._grades:
            del self._grades[course]
    
    def to_dict(self):
        """Convert to dictionary for serialization"""
        return {
            'student_id': self._student_id,
            'name': self._name,
            'email': self._email,
            'grades': self._grades,
            'created_at': self._created_at.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create student from dictionary"""
        student = cls(
            data['student_id'],
            data['name'],
            data['email'],
            data.get('grades', {})
        )
        if 'created_at' in data:
            student._created_at = datetime.fromisoformat(data['created_at'])
        return student
    
    def __str__(self):
        return f"[{self._student_id}] {self._name} <{self._email}> GPA: {self.gpa}"

# ============================================================================
# STORAGE
# ============================================================================

class Storage(ABC):
    """Abstract storage interface"""
    
    @abstractmethod
    def save(self, data):
        pass
    
    @abstractmethod
    def load(self):
        pass

class MemoryStorage(Storage):
    """In-memory storage (for testing)"""
    
    def __init__(self):
        self._data = {}
    
    def save(self, data):
        self._data = data
    
    def load(self):
        return self._data

class JSONStorage(Storage):
    """JSON file storage"""
    
    def __init__(self, filename='students.json'):
        self.filename = filename
    
    def save(self, data):
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load(self):
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            return {}

# ============================================================================
# MANAGER
# ============================================================================

class StudentManager:
    """Main student management class"""
    
    def __init__(self, storage=None):
        self.storage = storage or MemoryStorage()
        self.students = {}
        self._load()
    
    def _load(self):
        """Load students from storage"""
        data = self.storage.load()
        for sid, student_data in data.items():
            try:
                self.students[sid] = Student.from_dict(student_data)
            except (ValidationError, KeyError) as e:
                print(f"Warning: Could not load student {sid}: {e}")
    
    def _save(self):
        """Save students to storage"""
        data = {sid: s.to_dict() for sid, s in self.students.items()}
        self.storage.save(data)
    
    def add_student(self, student_id, name, email):
        """Add a new student"""
        student_id = student_id.upper()
        if student_id in self.students:
            raise DuplicateStudentError(student_id)
        
        student = Student(student_id, name, email)
        self.students[student_id] = student
        self._save()
        return student
    
    def get_student(self, student_id):
        """Get a student by ID"""
        student_id = student_id.upper()
        if student_id not in self.students:
            raise StudentNotFoundError(student_id)
        return self.students[student_id]
    
    def update_student(self, student_id, **kwargs):
        """Update student fields"""
        student = self.get_student(student_id)
        
        if 'name' in kwargs:
            student.name = kwargs['name']
        if 'email' in kwargs:
            student.email = kwargs['email']
        
        self._save()
        return student
    
    def delete_student(self, student_id):
        """Delete a student"""
        student = self.get_student(student_id)
        del self.students[student_id.upper()]
        self._save()
        return student
    
    def add_grade(self, student_id, course, grade):
        """Add grade to a student"""
        student = self.get_student(student_id)
        student.add_grade(course, grade)
        self._save()
        return student
    
    def search(self, query):
        """Search students by name or email"""
        query = query.lower()
        return [s for s in self.students.values() 
                if query in s.name.lower() or query in s.email.lower()]
    
    def get_all(self):
        """Get all students"""
        return list(self.students.values())
    
    def get_by_status(self, status):
        """Get students by academic status"""
        return [s for s in self.students.values() if s.status == status]

# ============================================================================
# CLI INTERFACE
# ============================================================================

class StudentCLI:
    """Command-line interface for student management"""
    
    def __init__(self, manager):
        self.manager = manager
        self.commands = {
            '1': ('List all students', self.list_students),
            '2': ('Add new student', self.add_student),
            '3': ('View student details', self.view_student),
            '4': ('Update student', self.update_student),
            '5': ('Delete student', self.delete_student),
            '6': ('Add grade', self.add_grade),
            '7': ('Search students', self.search_students),
            '8': ('View by status', self.view_by_status),
            '0': ('Exit', None)
        }
    
    def run(self):
        """Run the CLI interface"""
        print("\n" + "=" * 60)
        print("🎓 STUDENT MANAGEMENT SYSTEM")
        print("=" * 60)
        
        while True:
            print("\n📋 MENU:")
            for key, (desc, _) in self.commands.items():
                print(f"  {key}. {desc}")
            
            choice = input("\nEnter choice: ").strip()
            
            if choice == '0':
                print("\n👋 Goodbye!")
                break
            
            if choice in self.commands:
                _, action = self.commands[choice]
                if action:
                    try:
                        action()
                    except StudentError as e:
                        print(f"\n❌ Error: {e}")
                    except ValidationError as e:
                        print(f"\n❌ Validation Error: {e}")
            else:
                print("\n❌ Invalid choice")
    
    def list_students(self):
        """List all students"""
        students = self.manager.get_all()
        if not students:
            print("\n📭 No students found")
            return
        
        print(f"\n📚 Students ({len(students)}):")
        print("-" * 60)
        for s in sorted(students, key=lambda x: x.name):
            print(f"  {s}")
    
    def add_student(self):
        """Add a new student"""
        print("\n➕ ADD NEW STUDENT")
        student_id = input("Student ID: ").strip()
        name = input("Name: ").strip()
        email = input("Email: ").strip()
        
        student = self.manager.add_student(student_id, name, email)
        print(f"\n✅ Added: {student}")
    
    def view_student(self):
        """View student details"""
        student_id = input("\nStudent ID: ").strip()
        student = self.manager.get_student(student_id)
        
        print(f"\n👤 STUDENT DETAILS")
        print("=" * 40)
        print(f"ID: {student.student_id}")
        print(f"Name: {student.name}")
        print(f"Email: {student.email}")
        print(f"GPA: {student.gpa}")
        print(f"Status: {student.status}")
        
        if student._grades:
            print("\n📊 Grades:")
            for course, grade in student._grades.items():
                print(f"  {course}: {grade}")
    
    def update_student(self):
        """Update student info"""
        student_id = input("\nStudent ID to update: ").strip()
        student = self.manager.get_student(student_id)
        
        print(f"\nUpdating: {student}")
        print("(Press Enter to keep current value)")
        
        name = input(f"Name [{student.name}]: ").strip()
        email = input(f"Email [{student.email}]: ").strip()
        
        updates = {}
        if name:
            updates['name'] = name
        if email:
            updates['email'] = email
        
        if updates:
            student = self.manager.update_student(student_id, **updates)
            print(f"\n✅ Updated: {student}")
        else:
            print("\n⚠️ No changes made")
    
    def delete_student(self):
        """Delete a student"""
        student_id = input("\nStudent ID to delete: ").strip()
        student = self.manager.get_student(student_id)
        
        confirm = input(f"Delete {student.name}? (y/n): ").strip().lower()
        if confirm == 'y':
            self.manager.delete_student(student_id)
            print(f"\n✅ Deleted: {student.name}")
        else:
            print("\n⚠️ Cancelled")
    
    def add_grade(self):
        """Add grade to student"""
        student_id = input("\nStudent ID: ").strip()
        course = input("Course name: ").strip()
        grade = input("Grade (A+, A, A-, B+, ...): ").strip()
        
        student = self.manager.add_grade(student_id, course, grade)
        print(f"\n✅ Added grade. New GPA: {student.gpa}")
    
    def search_students(self):
        """Search for students"""
        query = input("\nSearch (name or email): ").strip()
        results = self.manager.search(query)
        
        if not results:
            print("\n📭 No results found")
        else:
            print(f"\n🔍 Found {len(results)} result(s):")
            for s in results:
                print(f"  {s}")
    
    def view_by_status(self):
        """View students by status"""
        print("\nStatuses: Dean's List, Good Standing, Academic Probation, No Grades")
        status = input("Enter status: ").strip()
        
        results = self.manager.get_by_status(status)
        if not results:
            print(f"\n📭 No students with status '{status}'")
        else:
            print(f"\n👥 {status} ({len(results)}):")
            for s in results:
                print(f"  {s}")

# ============================================================================
# DEMO
# ============================================================================

def demo():
    """Run a demo of the system"""
    print("🎓 STUDENT MANAGEMENT SYSTEM - DEMO")
    print("=" * 60)
    
    # Use memory storage for demo
    manager = StudentManager(MemoryStorage())
    
    # Add sample students
    print("\n📝 Adding sample students...")
    students = [
        ("STU001", "Alice Johnson", "alice@university.edu"),
        ("STU002", "Bob Smith", "bob@university.edu"),
        ("STU003", "Charlie Brown", "charlie@university.edu"),
        ("STU004", "Diana Ross", "diana@university.edu"),
    ]
    
    for sid, name, email in students:
        student = manager.add_student(sid, name, email)
        print(f"  Added: {student}")
    
    # Add grades
    print("\n📊 Adding grades...")
    grades = [
        ("STU001", "Python", "A"),
        ("STU001", "Math", "A-"),
        ("STU001", "English", "B+"),
        ("STU002", "Python", "B"),
        ("STU002", "Math", "C+"),
        ("STU003", "Python", "A+"),
        ("STU003", "Math", "A"),
        ("STU003", "English", "A"),
        ("STU004", "Python", "D"),
    ]
    
    for sid, course, grade in grades:
        manager.add_grade(sid, course, grade)
        print(f"  {sid}: {course} = {grade}")
    
    # Show all students
    print("\n📚 All Students:")
    print("-" * 60)
    for student in manager.get_all():
        print(f"  {student} - {student.status}")
    
    # Search
    print("\n🔍 Search 'alice':")
    for s in manager.search("alice"):
        print(f"  {s}")
    
    # By status
    print("\n🏆 Dean's List:")
    for s in manager.get_by_status("Dean's List"):
        print(f"  {s}")
    
    print("\n" + "=" * 60)
    print("✅ Demo complete!")
    print("=" * 60)

# Run demo or CLI
if __name__ == "__main__":
    print("\n1. Run Demo")
    print("2. Run Interactive CLI")
    choice = input("\nChoice (1/2): ").strip()
    
    if choice == "2":
        # Use JSON storage for persistence
        manager = StudentManager(JSONStorage("students.json"))
        cli = StudentCLI(manager)
        cli.run()
    else:
        demo()
