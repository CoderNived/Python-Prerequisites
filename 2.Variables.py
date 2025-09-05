# ==============================
# Declaring and Assigning Variables
# ==============================

# Variables store data values. You don't need to declare their type explicitly.
age = 32         # integer
height = 6.1     # float (decimal number)
name = "Krish"   # string
is_True = True   # boolean (True/False)

# ==============================
# Printing the Variables
# ==============================

print("age:", age)
print("height:", height)
print("name:", name)
print("is_True:", is_True)

# ==============================
# Naming Conventions
# ==============================

# ✅ Rules for naming variables:
# 1. Must start with a letter (a-z, A-Z) or underscore (_)
# 2. Can contain letters, numbers, and underscores
# 3. Case-sensitive (name, Name, NAME are all different variables)
# 4. Use descriptive names for better readability

first_name = "Nived"
last_name = "Shenoy"

# Example of case sensitivity:
name = "Nived"
Name = "Shenoy"
print(name)  # Output: Nived
print(Name)  # Output: Shenoy

# ==============================
# Understanding Variable Types
# ==============================

# Python is *dynamically typed*: type of a variable is determined at runtime.
age = 25           # int
salary = 25000.45  # float
name = "Nived"     # str
is_student = True  # bool

# Check variable types using type()
print(type(name))        # <class 'str'>
print(type(age))         # <class 'int'>
print(type(salary))      # <class 'float'>
print(type(is_student))  # <class 'bool'>

# ==============================
# Type Checking and Conversion
# ==============================

age = 25
print(type(age))  # <class 'int'>

# Convert int → str
age_str = str(age)
print(age_str)           # '25'
print(type(age_str))     # <class 'str'>

# Convert str → int
age = '25'
print(int(age))          # 25
print(type(int(age)))    # <class 'int'>

# ⚠️ Be careful: trying to convert a non-numeric string to int will cause an error
# Example: int("Krish") ❌ will throw ValueError

# Convert float → int (truncates decimal part)
height = 15.11
print(int(height))       # 15
# Convert int back to float
print(float(int(height)))  # 15.0

# ==============================
# Dynamic Typing
# ==============================

# Python allows variable type to change during execution
var = 10
print(var, type(var))  # 10 <class 'int'>
var = "Hello"
print(var, type(var))  # Hello <class 'str'>

# ==============================
# Simple Calculator
# ==============================

# Taking input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Performing basic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2  # Division always returns a float

# Display results
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
