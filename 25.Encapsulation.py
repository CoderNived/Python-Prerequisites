"""
📌 ENCAPSULATION IN PYTHON - COMPLETE NOTES & EXAMPLES
----------------------------------------------------
Encapsulation = "Data Hiding"
It is the process of bundling **data (attributes)** and **methods** into a single unit (class)
and restricting direct access to some of the class's components.

🔑 Why Encapsulation?
- Protects the internal state of an object.
- Allows controlled access (via getters & setters).
- Improves security & data integrity.

Access Modifiers in Python:
1️⃣ Public (default)  - Accessible everywhere
2️⃣ Protected         - Prefix with _ (single underscore)
3️⃣ Private           - Prefix with __ (double underscore)
"""

# 🔑 SYNTAX:
"""
class ClassName:
    def __init__(self):
        self.public_var = value
        self._protected_var = value
        self.__private_var = value
"""

# ----------------------------------------------------------------------
# 1️⃣ PUBLIC VARIABLES & METHODS
# ----------------------------------------------------------------------
print("\n--- Public Variables & Methods Example ---")

class Student:
    def __init__(self, name, grade):
        self.name = name        # Public Attribute
        self.grade = grade      # Public Attribute

    def display(self):
        print(f"Student: {self.name}, Grade: {self.grade}")

s1 = Student("Nived", "A")
s1.display()

# Public attributes can be accessed directly
s1.grade = "A+"
s1.display()


# ----------------------------------------------------------------------
# 2️⃣ PROTECTED VARIABLES & METHODS
# ----------------------------------------------------------------------
print("\n--- Protected Variables & Methods Example ---")

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary  # Protected attribute (convention)

    def _calculate_bonus(self):
        return self._salary * 0.1

e1 = Employee("Krish", 50000)
print(f"Name: {e1.name}")
print(f"Protected Salary (Accessible but not recommended): {e1._salary}")
print(f"Bonus (via protected method): {e1._calculate_bonus()}")


# ----------------------------------------------------------------------
# 3️⃣ PRIVATE VARIABLES & METHODS
# ----------------------------------------------------------------------
print("\n--- Private Variables & Methods Example ---")

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds!")

    def get_balance(self):  # Getter method
        return self.__balance

account = BankAccount("Nived", 5000)
account.deposit(1500)
account.withdraw(1000)
print(f"Current Balance: {account.get_balance()}")

# Direct access to private variable will fail
# print(account.__balance)  # ❌ AttributeError


# ----------------------------------------------------------------------
# 4️⃣ GETTERS & SETTERS (BEST PRACTICE)
# ----------------------------------------------------------------------
print("\n--- Getters and Setters Example ---")

class Product:
    def __init__(self, name, price):
        self.__price = price
        self.name = name

    # Getter
    def get_price(self):
        return self.__price

    # Setter
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Invalid Price!")

p = Product("Laptop", 50000)
print(f"Product Price: {p.get_price()}")
p.set_price(55000)
print(f"Updated Price: {p.get_price()}")
p.set_price(-100)  # Invalid


# ----------------------------------------------------------------------
# 5️⃣ PROPERTY DECORATOR (PYTHONIC WAY)
# ----------------------------------------------------------------------
print("\n--- Property Decorator Example ---")

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if value > 0:
            self.__radius = value
        else:
            print("Radius must be positive!")

    @property
    def area(self):
        return 3.14 * self.__radius ** 2

c = Circle(5)
print(f"Radius: {c.radius}, Area: {c.area}")
c.radius = 10
print(f"Updated Radius: {c.radius}, Updated Area: {c.area}")
c.radius = -5  # Invalid


# ----------------------------------------------------------------------
# 6️⃣ PRACTICAL REAL-WORLD EXAMPLE
# ----------------------------------------------------------------------
print("\n--- Practical Example: ATM System ---")

class ATM:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}, New Balance: {self.__balance}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}, Remaining Balance: {self.__balance}")
        else:
            print("Invalid or Insufficient balance!")

    def check_balance(self):
        print(f"Your Current Balance: {self.__balance}")

atm = ATM(10000)
atm.check_balance()
atm.deposit(2000)
atm.withdraw(5000)
atm.withdraw(20000)  # Insufficient balance


# ----------------------------------------------------------------------
# 7️⃣ NAME MANGLING (ADVANCED)
# ----------------------------------------------------------------------
print("\n--- Name Mangling Example ---")

class Demo:
    def __init__(self):
        self.__private_var = "Hidden"

    def __private_method(self):
        return "This is a private method"

    def access_private(self):
        return self.__private_method()

d = Demo()
# Accessing private method using name mangling (not recommended)
print(d._Demo__private_var)
print(d._Demo__private_method())
