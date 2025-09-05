"""
📌 POLYMORPHISM IN PYTHON - COMPLETE NOTES & EXAMPLES
----------------------------------------------------
Polymorphism = "Many Forms"
It allows the same interface (method/function) to be used for different data types or classes.

Types of Polymorphism:
1️⃣ Method Overriding (Runtime Polymorphism)
2️⃣ Method Overloading (Not natively supported, but can be simulated)
3️⃣ Operator Overloading
4️⃣ Polymorphism with Abstract Base Classes
5️⃣ Polymorphism with Functions
"""

# 🔑 SYNTAX
"""
class Parent:
    def method(self):
        pass

class Child(Parent):
    def method(self):  # Method overriding
        pass
"""

# ----------------------------------------------------------------------
# 1️⃣ METHOD OVERRIDING (RUNTIME POLYMORPHISM)
# ----------------------------------------------------------------------
print("\n--- Method Overriding Example ---")

class Animal:
    def speak(self):
        return "Some generic animal sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Function that demonstrates polymorphism
def animal_speak(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()
animal_speak(dog)
animal_speak(cat)


# ----------------------------------------------------------------------
# 2️⃣ POLYMORPHISM WITH FUNCTIONS
# ----------------------------------------------------------------------
print("\n--- Polymorphism with Functions Example ---")

class Shape:
    def area(self):
        return "Area not defined"

class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

shapes = [Rectangle(4, 5), Circle(5)]

for shape in shapes:
    print(f"Area: {shape.area()}")


# ----------------------------------------------------------------------
# 3️⃣ OPERATOR OVERLOADING
# ----------------------------------------------------------------------
print("\n--- Operator Overloading Example ---")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading + operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(2, 3)
p2 = Point(4, 5)
p3 = p1 + p2  # Uses __add__()
print(p3)


# ----------------------------------------------------------------------
# 4️⃣ POLYMORPHISM WITH ABSTRACT BASE CLASSES
# ----------------------------------------------------------------------
print("\n--- Polymorphism with Abstract Base Class Example ---")

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started 🚗"

class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle engine started 🏍️"

vehicles = [Car(), Motorcycle()]

for v in vehicles:
    print(v.start_engine())


# ----------------------------------------------------------------------
# 5️⃣ PRACTICAL REAL-WORLD EXAMPLE
# ----------------------------------------------------------------------
print("\n--- Practical Example: Payment Gateway ---")

class Payment:
    def pay(self, amount):
        raise NotImplementedError("Subclass must implement this method")

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card ✅")

class UpiPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI ✅")

class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal ✅")

# Function that accepts any payment method (Polymorphism)
def process_payment(payment_method, amount):
    payment_method.pay(amount)

process_payment(CreditCardPayment(), 5000)
process_payment(UpiPayment(), 1500)
process_payment(PayPalPayment(), 3000)


# ----------------------------------------------------------------------
# 6️⃣ METHOD OVERLOADING (SIMULATED)
# ----------------------------------------------------------------------
print("\n--- Simulated Method Overloading Example ---")

class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(5))       # One argument
print(calc.add(5, 10))   # Two arguments
print(calc.add(5, 10, 15))  # Three arguments
# Note: Python does not support traditional method overloading based on parameter types or counts.