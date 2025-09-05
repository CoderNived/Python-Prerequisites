"""
📌 ABSTRACTION IN PYTHON - COMPLETE NOTES & EXAMPLES
---------------------------------------------------
Abstraction = "Hiding the Implementation Details"
It allows you to focus on **what an object does**, not **how it does it**.

🔑 Why Abstraction?
- Reduces complexity by hiding unnecessary details.
- Promotes modular programming (cleaner, more reusable code).
- Makes future updates easier (only internal implementation changes).

In Python, Abstraction is achieved by:
1️⃣ Abstract Classes (using abc module)
2️⃣ Abstract Methods (methods with no implementation in base class)
3️⃣ Interfaces (achieved via abstract classes with only abstract methods)

📦 Syntax:
from abc import ABC, abstractmethod

class ClassName(ABC):
    @abstractmethod
    def method_name(self):
        pass

class DerivedClass(ClassName):
    def method_name(self):
        # implementation
"""

# ----------------------------------------------------------------------
# 1️⃣ BASIC EXAMPLE - Abstract Class & Method
# ----------------------------------------------------------------------
print("\n--- Basic Abstraction Example ---")

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass  # No implementation (forces subclasses to implement)

    def drive(self):
        print("This vehicle can be driven.")

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started!")

class Motorcycle(Vehicle):
    def start_engine(self):
        print("Motorcycle engine started!")

# Using abstraction:
car = Car()
motorcycle = Motorcycle()
car.start_engine()
motorcycle.start_engine()
car.drive()

# ----------------------------------------------------------------------
# 2️⃣ MULTIPLE ABSTRACT METHODS
# ----------------------------------------------------------------------
print("\n--- Example with Multiple Abstract Methods ---")

class Payment(ABC):
    @abstractmethod
    def authenticate(self):
        pass

    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def authenticate(self):
        print("Authenticating credit card...")

    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

class UPIBasedPayment(Payment):
    def authenticate(self):
        print("UPI PIN Verified ✅")

    def pay(self, amount):
        print(f"Paid {amount} using UPI")

payment1 = CreditCardPayment()
payment1.authenticate()
payment1.pay(1500)

payment2 = UPIBasedPayment()
payment2.authenticate()
payment2.pay(500)

# ----------------------------------------------------------------------
# 3️⃣ PARTIAL ABSTRACTION (Abstract + Concrete Methods)
# ----------------------------------------------------------------------
print("\n--- Partial Abstraction Example ---")

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def info(self):  # Concrete method (no need to override)
        print("All shapes have area.")

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

rect = Rectangle(5, 10)
circle = Circle(7)
rect.info()
print(f"Rectangle area = {rect.area()}")
print(f"Circle area = {circle.area()}")

# ----------------------------------------------------------------------
# 4️⃣ REAL-WORLD PRACTICAL EXAMPLE
# ----------------------------------------------------------------------
print("\n--- Real-World Example: Notification System ---")

class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotification(Notification):
    def send(self, message):
        print(f"Sending Email: {message}")

class SMSNotification(Notification):
    def send(self, message):
        print(f"Sending SMS: {message}")

class PushNotification(Notification):
    def send(self, message):
        print(f"Sending Push Notification: {message}")

def notify_user(notifier: Notification, message: str):
    notifier.send(message)

# Client Code
email = EmailNotification()
sms = SMSNotification()
push = PushNotification()

notify_user(email, "Your order has been shipped!")
notify_user(sms, "Your OTP is 123456")
notify_user(push, "You have a new message.")

# ----------------------------------------------------------------------
# 5️⃣ ADVANCED EXAMPLE: FACTORY PATTERN USING ABSTRACTION
# ----------------------------------------------------------------------
print("\n--- Advanced Example: Factory Pattern ---")

class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass

class Truck(Transport):
    def deliver(self):
        print("Delivering goods by road in a truck 🚚")

class Ship(Transport):
    def deliver(self):
        print("Delivering goods by sea in a ship 🚢")

def transport_factory(transport_type):
    if transport_type == "truck":
        return Truck()
    elif transport_type == "ship":
        return Ship()
    else:
        raise ValueError("Unknown transport type")

# Using factory + abstraction
t1 = transport_factory("truck")
t2 = transport_factory("ship")
t1.deliver()
t2.deliver()
