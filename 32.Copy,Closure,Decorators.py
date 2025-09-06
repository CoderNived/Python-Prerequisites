"""
===========================================================
📌 COPY, CLOSURE, AND DECORATORS – COMPLETE NOTES
===========================================================

This file covers three important Python concepts:
1. Copy (Shallow Copy vs Deep Copy)
2. Closures
3. Decorators

Each section includes:
✅ Concept Explanation  
✅ Syntax  
✅ Examples  
✅ Real-World Use Cases  
===========================================================
"""

# ===========================================================
# 1️⃣ COPY IN PYTHON (Shallow Copy vs Deep Copy)
# ===========================================================
import copy

print("========== COPY IN PYTHON ==========")

# Original List
original_list = [[1, 2, 3], [4, 5, 6]]
print("Original List:", original_list)

# Assignment (Not a copy! Just another reference)
assigned_list = original_list
assigned_list[0][0] = 99
print("\nAssigned List (changes original):", assigned_list)
print("Original List After Assignment:", original_list)

# Shallow Copy (copies outer object but not inner objects)
original_list = [[1, 2, 3], [4, 5, 6]]
shallow_copy = copy.copy(original_list)
shallow_copy[0][0] = 100
print("\nShallow Copy:", shallow_copy)
print("Original List After Shallow Copy (inner lists affected):", original_list)

# Deep Copy (full independent copy)
original_list = [[1, 2, 3], [4, 5, 6]]
deep_copy = copy.deepcopy(original_list)
deep_copy[0][0] = 500
print("\nDeep Copy:", deep_copy)
print("Original List After Deep Copy (no change):", original_list)

"""
📌 Summary:
- Assignment → Same reference (changes reflect in both)
- Shallow Copy → Copies outer object, inner objects shared
- Deep Copy → Complete independent copy (safe)
"""

# ===========================================================
# 2️⃣ CLOSURES IN PYTHON
# ===========================================================
print("\n========== CLOSURES ==========")

def outer_function(msg):
    """Outer function that returns inner function (closure)"""
    def inner_function():
        print(f"Message from closure: {msg}")
    return inner_function  # returning function object

# Create closures
closure_hello = outer_function("Hello")
closure_world = outer_function("World")

# Call closures
closure_hello()
closure_world()

"""
📌 Concept:
- A closure is a function that remembers values from its enclosing scope
  even after the outer function has finished executing.

📌 Syntax:
def outer():
    var = "some value"
    def inner():
        print(var)
    return inner

closure = outer()
closure()
"""

# Example: Counter using Closure
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

counter1 = make_counter()
print("\nCounter Example using Closure:")
print(counter1())
print(counter1())
print(counter1())

# ===========================================================
# 3️⃣ DECORATORS IN PYTHON
# ===========================================================
print("\n========== DECORATORS ==========")

"""
📌 Concept:
Decorators allow you to "wrap" a function with another function
to add functionality without modifying the original function code.

📌 Syntax:
def decorator(func):
    def wrapper(*args, **kwargs):
        # Add functionality before/after function call
        result = func(*args, **kwargs)
        return result
    return wrapper
"""

# Simple Decorator Example
def my_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Decorator with Arguments
def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} called with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned {result}")
        return result
    return wrapper

@logging_decorator
def add(a, b):
    return a + b

print("\nAdd Function with Logging Decorator:")
add(10, 20)

# Multiple Decorators Example
def uppercase_decorator(func):
    def wrapper():
        return func().upper()
    return wrapper

def exclamation_decorator(func):
    def wrapper():
        return func() + "!!!"
    return wrapper

@uppercase_decorator
@exclamation_decorator
def greet():
    return "hello"

print("\nMultiple Decorators Result:", greet())

# ===========================================================
# 4️⃣ REAL-WORLD USE CASES
# ===========================================================

# ✅ Use Case 1: Timing function execution
import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} executed in {end - start:.5f}s")
        return result
    return wrapper

@timer_decorator
def slow_function():
    time.sleep(1)
    return "Done"

print("\nTiming Decorator Example:")
print(slow_function())

# ✅ Use Case 2: Access control decorator
def require_authentication(func):
    def wrapper(user_authenticated, *args, **kwargs):
        if not user_authenticated:
            print("Access Denied! User not authenticated.")
            return None
        return func(*args, **kwargs)
    return wrapper

@require_authentication
def view_dashboard():
    print("Welcome to the dashboard!")

print("\nAuthentication Decorator Example:")
view_dashboard(False)  # Not authenticated
view_dashboard(True)   # Authenticated

"""
===========================================================
📌 SUMMARY
===========================================================
✅ COPY
- Assignment → Same reference
- Shallow Copy → Only top-level copied
- Deep Copy → Completely independent object

✅ CLOSURE
- Function that remembers enclosing scope variables
- Useful for maintaining state across calls (like counters)

✅ DECORATORS
- Functions that modify behavior of other functions
- Use @decorator_name syntax
- Real-world use cases: logging, authentication, caching, timing

===========================================================
"""
