"""
📌 INHERITANCE IN PYTHON - COMPLETE NOTES & EXAMPLES
---------------------------------------------------
This file covers:
✅ Concept & Syntax of Inheritance
✅ All Types of Inheritance (Single, Multiple, Multilevel, Hierarchical, Hybrid)
✅ super() Function
✅ Method Overriding
✅ Practical Examples
"""

# 🔑 BASICS OF INHERITANCE
print("\n--- Simple Inheritance Example ---")

# Parent Class
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} vehicle is starting...")

# Child Class
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  # Call parent constructor
        self.model = model

    def drive(self):
        print(f"{self.brand} {self.model} is now driving!")

# Create Object
my_car = Car("Tesla", "Model X")
my_car.start()
my_car.drive()


# ✅ Tesla Example (Inheritance + super())
print("\n--- Tesla Example ---")

class CarBase:
    def __init__(self, windows, gears, doors, engines):
        self.windows = windows
        self.gears = gears
        self.doors = doors
        self.engines = engines

    def drive(self):
        print("Car is driving...")

class Tesla(CarBase):
    def __init__(self, windows, gears, doors, engines, is_selfdriving):
        super().__init__(windows, gears, doors, engines)
        self.is_selfdriving = is_selfdriving

    def selfdriving(self):
        print(f"Tesla supports self driving: {self.is_selfdriving}")

tesla1 = Tesla(2, 6, 4, "Electric", True)
tesla1.drive()
tesla1.selfdriving()


# 📚 TYPES OF INHERITANCE
print("\n--- Single Inheritance ---")

class Parent:
    def greet(self):
        print("Hello from Parent!")

class Child(Parent):
    pass

obj = Child()
obj.greet()


print("\n--- Multiple Inheritance ---")
# Multiple Inheritance Example

class Animal:
    def __init__(self, name):
        self.name = name

class Pet:
    def __init__(self, owner):
        self.owner = owner

class Dog(Animal, Pet):
    def __init__(self, name, owner):
        Animal.__init__(self, name)
        Pet.__init__(self, owner)

dog = Dog("Buddy", "Krish")
print(dog.name, "owned by", dog.owner)


print("\n--- Multilevel Inheritance ---")

class GrandParent:
    def greet(self):
        print("Hello from GrandParent!")

class Parent(GrandParent):
    pass

class Child(Parent):
    pass

obj = Child()
obj.greet()


print("\n--- Hierarchical Inheritance ---")

class ParentClass:
    def greet(self):
        print("Hello from ParentClass!")

class Child1(ParentClass):
    pass

class Child2(ParentClass):
    pass

obj1 = Child1()
obj2 = Child2()
obj1.greet()
obj2.greet()


print("\n--- Hybrid Inheritance ---")

class A:
    def methodA(self):
        print("Class A method")

class B(A):
    def methodB(self):
        print("Class B method")

class C(A):
    def methodC(self):
        print("Class C method")

class D(B, C):  # Inherits from both B and C
    pass

d = D()
d.methodA()
d.methodB()
d.methodC()


# 🔄 super() FUNCTION USAGE
print("\n--- Using super() ---")

class Parent:
    def __init__(self):
        print("Parent Constructor Called")

class Child(Parent):
    def __init__(self):
        super().__init__()  # Calls Parent's __init__()
        print("Child Constructor Called")

child_obj = Child()


# 🎯 METHOD OVERRIDING EXAMPLE
print("\n--- Method Overriding ---")

class Shape:
    def area(self):
        print("Area of Shape is undefined")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):  # Overriding parent method
        return self.length * self.width

rect = Rectangle(5, 4)
print("Area of Rectangle:", rect.area())


# 🏁 PRACTICAL USE CASE (BANK ACCOUNT)
print("\n--- Practical Example: Bank Account ---")

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def show_balance(self):
        print(f"{self.owner}'s balance: {self.balance}")

class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Interest added: {interest}")

acc = SavingsAccount("Nived", 10000, 5)
acc.show_balance()
acc.add_interest()
acc.show_balance()
