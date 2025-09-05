# =========================================================
# MODULES & PACKAGES IN PYTHON
# =========================================================

# 1️⃣ WHAT IS A MODULE?
# A module is a file containing Python code (functions, classes, variables)
# It helps in organizing code and reusing functionality.

# =========================================================
# IMPORTING MODULES
# =========================================================

# Syntax 1: Import entire module
import math   # 'math' is a built-in Python module
print(math.sqrt(16))   # Access using module_name.function_name
print(math.pi)

# Syntax 2: Import specific function(s) or variable(s) from a module
from math import sqrt, pi
print(sqrt(16))   # No need to use math.
print(pi)

# Syntax 3: Import all functions from a module (NOT recommended)
from math import *   # Imports everything from math module
print(sin(0))
print(cos(0))

# Syntax 4: Import module with an alias (Best Practice)
import math as m
print(m.sqrt(25))
print(m.pi)

# Syntax 5: Import specific function with an alias
from math import factorial as fact
print(fact(5))


# =========================================================
# CREATING AND IMPORTING YOUR OWN MODULE
# =========================================================

# Step 1: Create a file named mymodule.py with following code:
# def greet(name):
#     return f"Hello, {name}!"

# Step 2: Import and use in another file
# import mymodule
# print(mymodule.greet("Nived"))

# Step 3: Or import specific function
# from mymodule import greet
# print(greet("Krish"))


# =========================================================
# PACKAGES IN PYTHON
# =========================================================
# A package is a collection of modules organized in a directory
# A package must contain a special file __init__.py (can be empty)

# Example Structure:
# mypackage/
# ├── __init__.py
# ├── module1.py
# └── module2.py

# Usage:
# from mypackage import module1
# module1.my_function()

# OR
# from mypackage.module1 import my_function
# my_function()


# =========================================================
# USING BUILT-IN MODULES (Examples)
# =========================================================

import random
print("Random number (1-10):", random.randint(1, 10))

import datetime
today = datetime.date.today()
print("Today's Date:", today)

import os
print("Current Working Directory:", os.getcwd())

import sys
print("Python Version:", sys.version)


# =========================================================
# BEST PRACTICES
# =========================================================
# ✅ Use "import module as alias" for large module names (example: import numpy as np)
# ✅ Prefer "from module import function" when you need only 1-2 functions
# ✅ Avoid "from module import *" (pollutes namespace, may cause conflicts)
# ✅ Organize custom modules into packages for large projects

