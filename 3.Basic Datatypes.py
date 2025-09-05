# ==============================
# Integer Example
# ==============================
age = 35  # Integer value
print("Age:", age)           # Output: Age: 35
print("Type of age:", type(age))  # Output: <class 'int'>

# 🏋️ Practice:
# 1. Change 'age' to a different number and re-run the code.
# 2. Try adding another integer variable (like year = 2025) and print its type.

# ==============================
# Floating Point Example
# ==============================
height = 5.11  # Float (decimal number)
print("Height:", height)           # Output: 5.11
print("Type of height:", type(height))  # Output: <class 'float'>

# 🏋️ Practice:
# 1. Change height to a whole number (like 6) and check if type changes.
# 2. Try multiplying height by 2 and print the result.

# ==============================
# String Example
# ==============================
name = "Nived"  # String value
print("Name:", name)          # Output: Nived
print("Type of name:", type(name))  # Output: <class 'str'>

# String concatenation
full_name = name + " Shenoy"
print("Full Name:", full_name)  # Output: Nived Shenoy

# 🏋️ Practice:
# 1. Try concatenating your first name and last name.
# 2. Replace "Nived" with your own name.

# ==============================
# Boolean Example
# ==============================
is_true = True  # Boolean value (True or False)
print("Boolean value:", is_true)        # Output: True
print("Type of is_true:", type(is_true))  # Output: <class 'bool'>

# bool() function converts a value to True/False
print(bool())           # Output: False (empty values are False)
print(bool(10))         # Output: True (non-zero numbers are True)
print(bool(0))          # Output: False (zero is considered False)
print(bool(""))         # Output: False (empty string is False)
print(bool("Python"))   # Output: True (non-empty string is True)

# 🏋️ Practice:
# 1. Try passing other numbers like -5, 100, or 0.0 into bool() and see results.
# 2. Try bool([]) and bool([1, 2, 3]) and see what happens.

# ==============================
# Comparison Operations return Boolean values
# ==============================
a = 10
b = 20
print("a == b:", a == b)        # False (10 is not equal to 20)
print("a != b:", a != b)        # True (10 is not equal to 20)
print("a < b:", a < b)          # True
print("a > b:", a > b)          # False
print("Type of (a==b):", type(a == b))  # <class 'bool'>

# 🏋️ Practice:
# 1. Try changing values of a and b and check the results.
# 2. Try using >= and <= comparisons as well.

# ==============================
# Common Errors and Fixes
# ==============================

# ❌ This will raise a TypeError (you cannot add string + integer directly)
# result = "hello" + 5  # Uncomment to see error

# ✅ Correct way: convert int to string before concatenation
result = "hello" + str(5)
print("Fixed result:", result)  # Output: hello5

# ⚠️ Avoid overwriting built-in names like 'str'
# str = "Hello"  # ❌ This will override the built-in 'str' type

# ✅ Use descriptive variable names instead:
greeting = "Hello"
print(str(123))  # Output: '123'

# 🏋️ Practice:
# 1. Try combining two numbers as strings: str(10) + str(20)
# 2. Try combining a string and float using str() and print result.
