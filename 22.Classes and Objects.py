# =========================================================
# OBJECT ORIENTED PROGRAMMING (OOP) IN PYTHON
# =========================================================

# A class is a blueprint for creating objects.
# Objects are instances of a class and can have attributes (variables) and methods (functions).

# =========================================================
# CLASS SYNTAX
# =========================================================
# Syntax:
# class ClassName:
#     """Optional Docstring"""
#     def __init__(self, parameters):
#         # Constructor to initialize instance variables
#         self.attribute = value
#     
#     def instance_method(self):
#         # Method that operates on instance variables
#         pass

# =========================================================
# BASIC CLASS EXAMPLE
class Car:
    pass

audi = Car()
bmw = Car()

print(type(audi))  # <class '__main__.Car'>


# =========================================================
# CONSTRUCTOR (__init__) & INSTANCE VARIABLES
class Dog:
    def __init__(self, name, age):
        self.name = name        # Instance Variable
        self.age = age

# Creating objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Tommy", 4)

print(dog1.name, dog1.age)
print(dog2.name, dog2.age)


# =========================================================
# INSTANCE METHODS
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name} says Woof!")

dog1 = Dog("Lucy", 3)
dog1.bark()  # Lucy says Woof!


# =========================================================
# CLASS ATTRIBUTES & CLASS METHODS
class Employee:
    company = "TechCorp"  # Class Attribute (shared across all objects)
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

emp1 = Employee("Nived", 50000)
emp2 = Employee("Krish", 60000)

print(emp1.company, emp2.company)  # TechCorp TechCorp
Employee.change_company("OpenAI")
print(emp1.company, emp2.company)  # OpenAI OpenAI


# =========================================================
# STATIC METHODS
# Static methods don't need access to instance (self) or class (cls)
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(10, 20))  # 30


# =========================================================
# ENCAPSULATION (PRIVATE VARIABLES)
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance   # Private variable (name mangling)
    
    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}, New Balance: {self.__balance}")
    
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}, Remaining Balance: {self.__balance}")
    
    def get_balance(self):
        return self.__balance

account = BankAccount("Nived", 50000)
account.deposit(1000)
account.withdraw(6000)
print("Final Balance:", account.get_balance())


# =========================================================
# INHERITANCE
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):  # Inheriting from Animal
    def speak(self):
        print(f"{self.name} barks!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows!")

dog = Dog("Buddy")
cat = Cat("Kitty")
dog.speak()  # Buddy barks!
cat.speak()  # Kitty meows!


# =========================================================
# MULTIPLE INHERITANCE
class Father:
    def skills(self):
        print("Father: Gardening")

class Mother:
    def skills(self):
        print("Mother: Cooking")

class Child(Father, Mother):
    def skills(self):
        super().skills()  # Calls Father.skills() due to MRO
        print("Child: Playing Football")

child = Child()
child.skills()


# =========================================================
# POLYMORPHISM
# The ability to use a single interface to represent different data types
animals = [Dog("Max"), Cat("Simba")]
for animal in animals:
    animal.speak()  # Calls the respective speak() method


# =========================================================
# DUNDER METHODS (MAGIC METHODS)
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(2, 3)
p2 = Point(4, 5)
p3 = p1 + p2
print(p3)  # Point(6, 8)


# =========================================================
# PRACTICAL EXAMPLES
# =========================================================

# 1. Student Management System
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        else:
            return "C"

students = [Student("Nived", 92), Student("Krish", 81)]
for student in students:
    print(f"{student.name}: {student.get_grade()}")


# 2. Library System
class Book:
    def __init__(self, title, author):
        self.title, self.author = title, author
        self.is_issued = False
    
    def issue_book(self):
        if not self.is_issued:
            self.is_issued = True
            print(f"{self.title} issued successfully.")
        else:
            print(f"{self.title} is already issued.")

book1 = Book("Atomic Habits", "James Clear")
book1.issue_book()
book1.issue_book()
