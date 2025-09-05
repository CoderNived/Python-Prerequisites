# ==============================
# Arithmetic Operators
# ==============================
a = 10
b = 20

print("a + b =", a + b)   # Addition → 10 + 20 = 30
print("a - b =", a - b)   # Subtraction → 10 - 20 = -10
print("a * b =", a * b)   # Multiplication → 10 * 20 = 200
print("a / b =", a / b)   # Division → Always returns float (10 / 20 = 0.5)
print("a // b =", a // b) # Floor Division → Returns whole number result (0)
print("a % b =", a % b)   # Modulus → Returns remainder (10 % 20 = 10)
print("a ** b =", a ** b) # Exponentiation → 10 raised to power 20

# 🏋️ Practice:
# 1. Try changing a and b to other numbers (like 15 and 4) and observe results.
# 2. Check the difference between normal division (/) and floor division (//).
# 3. Try modulus with different numbers (like 15 % 4, 9 % 3).

# ==============================
# Comparison Operators
# ==============================
a = 10
b = 20

print("a == b:", a == b)  # Equal to → False
print("a != b:", a != b)  # Not equal to → True
print("a > b:", a > b)    # Greater than → False
print("a < b:", a < b)    # Less than → True
print("a >= b:", a >= b)  # Greater than or equal → False
print("a <= b:", a <= b)  # Less than or equal → True

# 🏋️ Practice:
# 1. Change values of a and b and check how results change.
# 2. Try using equal comparison (==) with strings like ("hello" == "Hello").

# ==============================
# Logical Operators
# ==============================
a = 0  # False (because 0 is considered False)
b = 1  # True (non-zero numbers are considered True)

print("a and b:", a and b)  # AND → Returns first False value → 0
print("not a:", not a)      # NOT → Inverts the value of a → True
print("a or b:", a or b)    # OR → Returns first True value → 1

# 🏋️ Practice:
# 1. Try setting a = True and b = False and see results.
# 2. Replace a and b with numbers like 5 and 0, then test again.
# 3. Use logical operators with comparison results (Example: (a < b) and (b > 5)).

