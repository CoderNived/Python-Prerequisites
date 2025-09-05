# ==============================
# Basic Syntax Rules in Python
# ==============================

# 1. Case Sensitivity:
# Python is case-sensitive. This means "Var", "var", and "VAR" are treated as three different variables.
# Example:
# name = "Alice"
# Name = "Bob"
# print(name, Name)  # Output: Alice Bob

# 2. Indentation:
# Python uses indentation (spaces or tabs) to define code blocks instead of curly braces {}.
# Indentation is mandatory and consistent indentation is required.
# Example:
# if True:
#     print("This is indented correctly!")
# print("This is outside the if block.")

# 3. Line Continuation:
# Use a backslash "\" to continue a long line of code onto the next line.
# Example:
# total = 10 + 20 + 30 + \
#         40 + 50
# print(total)  # Output: 150

# 4. Semantics:
# Semantics is about meaning. Even if the syntax is correct, code should make sense logically.
# Example of wrong semantics:
# print(10 / 0)  # ❌ Syntax is correct but throws ZeroDivisionError at runtime.

# 5. Type Inference:
# Python automatically infers the type of a variable based on the value assigned.
# You don't need to explicitly mention types like int, float, etc.
# Example:
# a = 5       # a is inferred as int
# b = 3.14    # b is inferred as float
# c = "Hello" # c is inferred as string

# ==============================
# Example Program
# ==============================

# Printing "Hello World" (classic first program)
print("Hello, world!")  # Output: Hello, world!
