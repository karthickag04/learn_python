# LESSON 32: OOP Practice Exercises
# Practice creating classes with constructors, methods, and encapsulation

"""
EXERCISE 1: Library Book System
Create a Book class with:
- title, author, isbn (private)
- borrowed status
- Method to borrow/return
- Class variable for total books
"""

class Book:
    # Class variable
    total_books = 0
    
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.__isbn = isbn  # Private
        self._is_borrowed = False
        self._borrower = None
        Book.total_books += 1
    
    @property
    def isbn(self):
        """Read-only ISBN"""
        return self.__isbn
    
    @property
    def is_available(self):
        return not self._is_borrowed
    
    def borrow(self, borrower_name):
        """Borrow the book"""
        if self._is_borrowed:
            return f"Sorry, '{self.title}' is already borrowed by {self._borrower}"
        self._is_borrowed = True
        self._borrower = borrower_name
        return f"'{self.title}' borrowed by {borrower_name}"
    
    def return_book(self):
        """Return the book"""
        if not self._is_borrowed:
            return f"'{self.title}' was not borrowed"
        old_borrower = self._borrower
        self._is_borrowed = False
        self._borrower = None
        return f"'{self.title}' returned by {old_borrower}"
    
    def __str__(self):
        status = "Available" if self.is_available else f"Borrowed by {self._borrower}"
        return f"📚 {self.title} by {self.author} - {status}"

# Test Book class
print("=" * 60)
print("📚 LIBRARY SYSTEM TEST")
print("=" * 60)

book1 = Book("Python Basics", "John Doe", "978-1234567890")
book2 = Book("Advanced Python", "Jane Smith", "978-0987654321")

print(f"\nTotal books in library: {Book.total_books}")
print(book1)
print(book2)

print("\n--- Borrowing ---")
print(book1.borrow("Alice"))
print(book1)
print(book1.borrow("Bob"))  # Should fail

print("\n--- Returning ---")
print(book1.return_book())
print(book1)


"""
EXERCISE 2: Shopping Cart
Create a ShoppingCart class with:
- Items list (private)
- Add/remove items
- Calculate total
- Apply discount
"""

class CartItem:
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    @property
    def subtotal(self):
        return self.price * self.quantity
    
    def __str__(self):
        return f"{self.name} x{self.quantity} @ ${self.price:.2f} = ${self.subtotal:.2f}"

class ShoppingCart:
    def __init__(self, customer_name):
        self.customer = customer_name
        self.__items = []  # Private
        self._discount = 0
    
    @property
    def item_count(self):
        return sum(item.quantity for item in self.__items)
    
    @property
    def subtotal(self):
        return sum(item.subtotal for item in self.__items)
    
    @property
    def discount_amount(self):
        return self.subtotal * (self._discount / 100)
    
    @property
    def total(self):
        return self.subtotal - self.discount_amount
    
    def add_item(self, name, price, quantity=1):
        """Add item to cart"""
        # Check if item exists
        for item in self.__items:
            if item.name == name and item.price == price:
                item.quantity += quantity
                return f"Updated {name}: now {item.quantity}"
        
        self.__items.append(CartItem(name, price, quantity))
        return f"Added {name} to cart"
    
    def remove_item(self, name):
        """Remove item from cart"""
        for i, item in enumerate(self.__items):
            if item.name == name:
                removed = self.__items.pop(i)
                return f"Removed {removed.name}"
        return f"{name} not found in cart"
    
    def apply_discount(self, percent):
        """Apply percentage discount"""
        if 0 <= percent <= 100:
            self._discount = percent
            return f"Applied {percent}% discount"
        return "Invalid discount percentage"
    
    def view_cart(self):
        """Display cart contents"""
        print(f"\n🛒 Cart for {self.customer}")
        print("-" * 40)
        for item in self.__items:
            print(f"  {item}")
        print("-" * 40)
        print(f"  Subtotal: ${self.subtotal:.2f}")
        if self._discount > 0:
            print(f"  Discount ({self._discount}%): -${self.discount_amount:.2f}")
        print(f"  TOTAL: ${self.total:.2f}")
    
    def checkout(self):
        """Complete purchase"""
        if not self.__items:
            return "Cart is empty!"
        
        total = self.total
        self.__items.clear()
        self._discount = 0
        return f"Purchase complete! Charged: ${total:.2f}"

# Test ShoppingCart
print("\n" + "=" * 60)
print("🛒 SHOPPING CART TEST")
print("=" * 60)

cart = ShoppingCart("Bob")
print(cart.add_item("Laptop", 999.99))
print(cart.add_item("Mouse", 29.99, 2))
print(cart.add_item("Keyboard", 79.99))
print(cart.add_item("Mouse", 29.99, 1))  # Add more mice

cart.view_cart()

print("\n" + cart.apply_discount(10))
cart.view_cart()

print("\n" + cart.checkout())


"""
EXERCISE 3: Student Grade Tracker
Create a Student class that tracks grades and calculates GPA
"""

class Student:
    # Class variable for GPA scale
    GRADE_POINTS = {
        'A+': 4.0, 'A': 4.0, 'A-': 3.7,
        'B+': 3.3, 'B': 3.0, 'B-': 2.7,
        'C+': 2.3, 'C': 2.0, 'C-': 1.7,
        'D+': 1.3, 'D': 1.0, 'D-': 0.7,
        'F': 0.0
    }
    
    _next_id = 1
    
    def __init__(self, name):
        self.student_id = f"STU{Student._next_id:04d}"
        Student._next_id += 1
        self.name = name
        self.__grades = {}  # course: grade
    
    @property
    def courses(self):
        return list(self.__grades.keys())
    
    @property
    def gpa(self):
        if not self.__grades:
            return 0.0
        total_points = sum(Student.GRADE_POINTS.get(g, 0) 
                         for g in self.__grades.values())
        return total_points / len(self.__grades)
    
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
        """Add or update a grade"""
        grade = grade.upper()
        if grade not in Student.GRADE_POINTS:
            return f"Invalid grade: {grade}"
        self.__grades[course] = grade
        return f"Added {course}: {grade}"
    
    def get_grade(self, course):
        """Get grade for a course"""
        return self.__grades.get(course, "Not enrolled")
    
    def get_transcript(self):
        """Display transcript"""
        print(f"\n📜 TRANSCRIPT - {self.name} ({self.student_id})")
        print("=" * 40)
        for course, grade in self.__grades.items():
            points = Student.GRADE_POINTS[grade]
            print(f"  {course:<20} {grade:>3} ({points:.1f})")
        print("=" * 40)
        print(f"  GPA: {self.gpa:.2f} - {self.status}")
    
    @classmethod
    def valid_grades(cls):
        """Show valid grade options"""
        return list(cls.GRADE_POINTS.keys())

# Test Student
print("\n" + "=" * 60)
print("🎓 STUDENT GRADE TRACKER TEST")
print("=" * 60)

student = Student("Alice Johnson")
print(f"Created: {student.name} ({student.student_id})")
print(f"Valid grades: {Student.valid_grades()}")

print("\n--- Adding Grades ---")
print(student.add_grade("Python Programming", "A"))
print(student.add_grade("Data Structures", "B+"))
print(student.add_grade("Calculus", "A-"))
print(student.add_grade("English", "B"))
print(student.add_grade("Invalid Course", "X"))  # Invalid grade

student.get_transcript()


"""
EXERCISE 4: Bank Account with Transaction History
Complete bank account with security features
"""

class Transaction:
    def __init__(self, type_, amount, balance_after):
        from datetime import datetime
        self.timestamp = datetime.now()
        self.type = type_
        self.amount = amount
        self.balance_after = balance_after
    
    def __str__(self):
        date = self.timestamp.strftime("%Y-%m-%d %H:%M")
        sign = "+" if self.amount > 0 else ""
        return f"{date} | {self.type:<12} | {sign}${abs(self.amount):<10.2f} | ${self.balance_after:.2f}"

class SecureBankAccount:
    _next_account = 100000
    
    def __init__(self, owner, pin, initial_deposit=0):
        self.account_number = SecureBankAccount._next_account
        SecureBankAccount._next_account += 1
        
        self.owner = owner
        self.__pin = pin  # Private
        self.__balance = 0
        self.__transactions = []  # Private
        self.__failed_attempts = 0
        self.__locked = False
        
        if initial_deposit > 0:
            self.__balance = initial_deposit
            self._record_transaction("DEPOSIT", initial_deposit)
    
    def _verify_pin(self, pin):
        """Verify PIN with lockout protection"""
        if self.__locked:
            return False, "Account is locked. Contact support."
        
        if pin != self.__pin:
            self.__failed_attempts += 1
            if self.__failed_attempts >= 3:
                self.__locked = True
                return False, "Account locked after 3 failed attempts!"
            remaining = 3 - self.__failed_attempts
            return False, f"Wrong PIN. {remaining} attempts remaining."
        
        self.__failed_attempts = 0
        return True, "PIN verified"
    
    def _record_transaction(self, type_, amount):
        """Record a transaction"""
        self.__transactions.append(
            Transaction(type_, amount, self.__balance)
        )
    
    @property
    def balance(self):
        return self.__balance
    
    def deposit(self, amount):
        """Deposit money (no PIN needed)"""
        if amount <= 0:
            return "Amount must be positive"
        self.__balance += amount
        self._record_transaction("DEPOSIT", amount)
        return f"Deposited ${amount:.2f}. New balance: ${self.__balance:.2f}"
    
    def withdraw(self, amount, pin):
        """Withdraw money (PIN required)"""
        verified, message = self._verify_pin(pin)
        if not verified:
            return message
        
        if amount <= 0:
            return "Amount must be positive"
        if amount > self.__balance:
            return f"Insufficient funds. Available: ${self.__balance:.2f}"
        
        self.__balance -= amount
        self._record_transaction("WITHDRAWAL", -amount)
        return f"Withdrew ${amount:.2f}. New balance: ${self.__balance:.2f}"
    
    def change_pin(self, old_pin, new_pin):
        """Change account PIN"""
        verified, message = self._verify_pin(old_pin)
        if not verified:
            return message
        
        if len(new_pin) != 4 or not new_pin.isdigit():
            return "PIN must be 4 digits"
        
        self.__pin = new_pin
        return "PIN changed successfully"
    
    def get_statement(self, pin, last_n=10):
        """Get account statement (PIN required)"""
        verified, message = self._verify_pin(pin)
        if not verified:
            return message
        
        print(f"\n{'=' * 70}")
        print(f"  ACCOUNT STATEMENT - {self.owner}")
        print(f"  Account #: {self.account_number}")
        print(f"{'=' * 70}")
        print(f"  {'Date':<18} | {'Type':<12} | {'Amount':<12} | Balance")
        print(f"  {'-' * 60}")
        
        for trans in self.__transactions[-last_n:]:
            print(f"  {trans}")
        
        print(f"  {'-' * 60}")
        print(f"  Current Balance: ${self.__balance:.2f}")
        print(f"{'=' * 70}")

# Test SecureBankAccount
print("\n" + "=" * 60)
print("🏦 SECURE BANK ACCOUNT TEST")
print("=" * 60)

account = SecureBankAccount("John Doe", "1234", 1000)
print(f"Account created: #{account.account_number}")

print("\n--- Transactions ---")
print(account.deposit(500))
print(account.deposit(250.50))
print(account.withdraw(200, "1234"))
print(account.withdraw(100, "9999"))  # Wrong PIN
print(account.withdraw(100, "1234"))  # Correct PIN

# Statement
account.get_statement("1234")

# PIN change
print("\n--- Security Features ---")
print(account.change_pin("1234", "5678"))
print(account.withdraw(50, "1234"))  # Old PIN
print(account.withdraw(50, "5678"))  # New PIN

print("\n" + "=" * 60)
print("✅ All OOP practice exercises completed!")
print("=" * 60)
