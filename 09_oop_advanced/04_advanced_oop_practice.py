# LESSON 36: Advanced OOP Practice
# Practice exercises for inheritance, polymorphism, and abstract classes

from abc import ABC, abstractmethod
from typing import List, Dict, Any

"""
EXERCISE 1: Shape Hierarchy with Abstract Base Class
Create a complete shape system with area and perimeter calculations.
"""

print("=" * 60)
print("📐 EXERCISE 1: SHAPE HIERARCHY")
print("=" * 60)

import math

class Shape(ABC):
    """Abstract base class for all shapes"""
    
    @property
    @abstractmethod
    def name(self) -> str:
        pass
    
    @abstractmethod
    def area(self) -> float:
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        pass
    
    def describe(self) -> str:
        return f"{self.name}: Area = {self.area():.2f}, Perimeter = {self.perimeter():.2f}"

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    
    @property
    def name(self) -> str:
        return "Rectangle"
    
    def area(self) -> float:
        return self.width * self.height
    
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

class Square(Rectangle):
    def __init__(self, side: float):
        super().__init__(side, side)
    
    @property
    def name(self) -> str:
        return "Square"

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius
    
    @property
    def name(self) -> str:
        return "Circle"
    
    def area(self) -> float:
        return math.pi * self.radius ** 2
    
    def perimeter(self) -> float:
        return 2 * math.pi * self.radius

class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        self.a, self.b, self.c = a, b, c
    
    @property
    def name(self) -> str:
        return "Triangle"
    
    def area(self) -> float:
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def perimeter(self) -> float:
        return self.a + self.b + self.c

# Calculate total area of all shapes
def total_area(shapes: List[Shape]) -> float:
    return sum(shape.area() for shape in shapes)

# Test
shapes = [
    Rectangle(10, 5),
    Square(4),
    Circle(3),
    Triangle(3, 4, 5)
]

print("\nShapes:")
for shape in shapes:
    print(f"  {shape.describe()}")

print(f"\nTotal area of all shapes: {total_area(shapes):.2f}")


"""
EXERCISE 2: Vehicle Rental System with Inheritance and Polymorphism
"""

print("\n" + "=" * 60)
print("🚗 EXERCISE 2: VEHICLE RENTAL SYSTEM")
print("=" * 60)

class Vehicle(ABC):
    """Abstract vehicle class"""
    
    _id_counter = 0
    
    def __init__(self, brand: str, model: str, daily_rate: float):
        Vehicle._id_counter += 1
        self.vehicle_id = Vehicle._id_counter
        self.brand = brand
        self.model = model
        self.daily_rate = daily_rate
        self.is_available = True
        self._current_renter = None
    
    @property
    @abstractmethod
    def vehicle_type(self) -> str:
        pass
    
    @abstractmethod
    def get_insurance_rate(self) -> float:
        pass
    
    def rent(self, renter_name: str) -> str:
        if not self.is_available:
            return f"Sorry, {self} is not available"
        self.is_available = False
        self._current_renter = renter_name
        return f"{renter_name} rented {self}"
    
    def return_vehicle(self, days: int) -> str:
        if self.is_available:
            return f"{self} was not rented"
        
        renter = self._current_renter
        total = self.calculate_total(days)
        self.is_available = True
        self._current_renter = None
        return f"{renter} returned {self}. Total: ${total:.2f}"
    
    def calculate_total(self, days: int) -> float:
        return days * (self.daily_rate + self.get_insurance_rate())
    
    def __str__(self):
        return f"{self.vehicle_type}: {self.brand} {self.model}"

class Car(Vehicle):
    def __init__(self, brand: str, model: str, daily_rate: float, seats: int):
        super().__init__(brand, model, daily_rate)
        self.seats = seats
    
    @property
    def vehicle_type(self) -> str:
        return "Car"
    
    def get_insurance_rate(self) -> float:
        return 15.00  # Fixed insurance for cars

class Motorcycle(Vehicle):
    def __init__(self, brand: str, model: str, daily_rate: float, engine_cc: int):
        super().__init__(brand, model, daily_rate)
        self.engine_cc = engine_cc
    
    @property
    def vehicle_type(self) -> str:
        return "Motorcycle"
    
    def get_insurance_rate(self) -> float:
        return 10.00 if self.engine_cc < 600 else 20.00

class Truck(Vehicle):
    def __init__(self, brand: str, model: str, daily_rate: float, payload_kg: int):
        super().__init__(brand, model, daily_rate)
        self.payload_kg = payload_kg
    
    @property
    def vehicle_type(self) -> str:
        return "Truck"
    
    def get_insurance_rate(self) -> float:
        return 25.00 + (self.payload_kg / 1000) * 5  # Extra $5 per ton

class RentalAgency:
    def __init__(self, name: str):
        self.name = name
        self.vehicles: List[Vehicle] = []
    
    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles.append(vehicle)
    
    def available_vehicles(self) -> List[Vehicle]:
        return [v for v in self.vehicles if v.is_available]
    
    def find_by_type(self, vehicle_type: str) -> List[Vehicle]:
        return [v for v in self.vehicles if v.vehicle_type.lower() == vehicle_type.lower()]
    
    def display_fleet(self):
        print(f"\n{self.name} Fleet:")
        print("-" * 50)
        for v in self.vehicles:
            status = "✓ Available" if v.is_available else f"✗ Rented to {v._current_renter}"
            rate = v.daily_rate + v.get_insurance_rate()
            print(f"  [{v.vehicle_id}] {v} - ${rate:.2f}/day - {status}")

# Test
agency = RentalAgency("PyRentals")
agency.add_vehicle(Car("Toyota", "Camry", 45.00, 5))
agency.add_vehicle(Car("BMW", "X5", 85.00, 5))
agency.add_vehicle(Motorcycle("Honda", "CBR600", 35.00, 600))
agency.add_vehicle(Motorcycle("Harley", "Street 750", 55.00, 750))
agency.add_vehicle(Truck("Ford", "F-150", 75.00, 1500))

agency.display_fleet()

print("\n--- Rental Operations ---")
print(agency.vehicles[0].rent("Alice"))
print(agency.vehicles[2].rent("Bob"))

agency.display_fleet()

print("\n--- Returns ---")
print(agency.vehicles[0].return_vehicle(3))
print(agency.vehicles[2].return_vehicle(2))


"""
EXERCISE 3: Notification System with Polymorphism
"""

print("\n" + "=" * 60)
print("📨 EXERCISE 3: NOTIFICATION SYSTEM")
print("=" * 60)

class Notification(ABC):
    """Abstract notification"""
    
    def __init__(self, recipient: str, message: str):
        self.recipient = recipient
        self.message = message
        self.sent = False
    
    @abstractmethod
    def send(self) -> bool:
        pass
    
    @property
    @abstractmethod
    def channel(self) -> str:
        pass
    
    def get_status(self) -> str:
        return "✓ Sent" if self.sent else "○ Pending"

class EmailNotification(Notification):
    def __init__(self, email: str, subject: str, body: str):
        super().__init__(email, body)
        self.subject = subject
    
    @property
    def channel(self) -> str:
        return "Email"
    
    def send(self) -> bool:
        # Simulate sending email
        print(f"  📧 Email to {self.recipient}")
        print(f"     Subject: {self.subject}")
        print(f"     Body: {self.message[:50]}...")
        self.sent = True
        return True

class SMSNotification(Notification):
    MAX_LENGTH = 160
    
    @property
    def channel(self) -> str:
        return "SMS"
    
    def send(self) -> bool:
        msg = self.message[:self.MAX_LENGTH]
        print(f"  📱 SMS to {self.recipient}: {msg}")
        self.sent = True
        return True

class PushNotification(Notification):
    def __init__(self, device_id: str, title: str, body: str):
        super().__init__(device_id, body)
        self.title = title
    
    @property
    def channel(self) -> str:
        return "Push"
    
    def send(self) -> bool:
        print(f"  🔔 Push to device {self.recipient[:8]}...")
        print(f"     Title: {self.title}")
        print(f"     Body: {self.message}")
        self.sent = True
        return True

class NotificationService:
    def __init__(self):
        self.notifications: List[Notification] = []
    
    def queue(self, notification: Notification):
        self.notifications.append(notification)
    
    def send_all(self):
        print("\nSending notifications...")
        for notif in self.notifications:
            notif.send()
            print()
    
    def get_summary(self) -> Dict[str, int]:
        summary = {}
        for notif in self.notifications:
            channel = notif.channel
            summary[channel] = summary.get(channel, 0) + 1
        return summary

# Test
service = NotificationService()

service.queue(EmailNotification(
    "user@example.com",
    "Welcome!",
    "Thank you for signing up for our service. We're excited to have you!"
))

service.queue(SMSNotification(
    "+1234567890",
    "Your verification code is 123456"
))

service.queue(PushNotification(
    "device_abc123xyz",
    "New Message",
    "You have a new message from Alice"
))

service.send_all()

print("Summary:", service.get_summary())


"""
EXERCISE 4: File Handler with Abstract Factory Pattern
"""

print("\n" + "=" * 60)
print("📁 EXERCISE 4: FILE HANDLER SYSTEM")
print("=" * 60)

class FileHandler(ABC):
    """Abstract file handler"""
    
    def __init__(self, filename: str):
        self.filename = filename
    
    @abstractmethod
    def read(self) -> Any:
        pass
    
    @abstractmethod
    def write(self, data: Any) -> bool:
        pass
    
    @property
    @abstractmethod
    def extension(self) -> str:
        pass

class JSONHandler(FileHandler):
    @property
    def extension(self) -> str:
        return ".json"
    
    def read(self) -> Any:
        # Simulate reading JSON
        print(f"  Reading JSON from {self.filename}")
        return {"sample": "data"}
    
    def write(self, data: Any) -> bool:
        import json
        print(f"  Writing JSON to {self.filename}")
        print(f"  Content: {json.dumps(data, indent=2)}")
        return True

class CSVHandler(FileHandler):
    @property
    def extension(self) -> str:
        return ".csv"
    
    def read(self) -> Any:
        print(f"  Reading CSV from {self.filename}")
        return [["col1", "col2"], ["val1", "val2"]]
    
    def write(self, data: Any) -> bool:
        print(f"  Writing CSV to {self.filename}")
        for row in data:
            print(f"  {','.join(str(c) for c in row)}")
        return True

class XMLHandler(FileHandler):
    @property
    def extension(self) -> str:
        return ".xml"
    
    def read(self) -> Any:
        print(f"  Reading XML from {self.filename}")
        return {"root": {"element": "value"}}
    
    def write(self, data: Any) -> bool:
        print(f"  Writing XML to {self.filename}")
        print(f"  <data>{data}</data>")
        return True

# Factory
class FileHandlerFactory:
    @staticmethod
    def get_handler(filename: str) -> FileHandler:
        ext = filename.split('.')[-1].lower()
        handlers = {
            'json': JSONHandler,
            'csv': CSVHandler,
            'xml': XMLHandler
        }
        handler_class = handlers.get(ext)
        if not handler_class:
            raise ValueError(f"Unsupported file type: {ext}")
        return handler_class(filename)

# Test
print("\nFile operations:")
files = ["config.json", "data.csv", "settings.xml"]

for filename in files:
    print(f"\n{filename}:")
    handler = FileHandlerFactory.get_handler(filename)
    data = handler.read()
    handler.write({"test": "data"})

print("\n" + "=" * 60)
print("✅ All advanced OOP exercises completed!")
print("=" * 60)
