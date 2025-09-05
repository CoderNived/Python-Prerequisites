# =========================================================
# FUNCTIONS IN PYTHON
# =========================================================
# Function: A block of code that performs a specific task.
# Functions make code organized, reusable, and improve readability.

# ---------------------------------------------------------
# 1. DEFINING AND CALLING A FUNCTION
# ---------------------------------------------------------

# SYNTAX:
# def function_name(parameters):
#     """docstring (optional)"""
#     # function body
#     return value (optional)

def even_or_odd(num):
    """This function determines if a number is even or odd"""
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

# Calling the function
even_or_odd(24)
even_or_odd(17)

# ---------------------------------------------------------
# 2. FUNCTION WITH RETURN VALUE
# ---------------------------------------------------------

# SYNTAX:
# def function_name(parameters):
#     return expression

def add(a, b):
    """Returns the sum of two numbers"""
    return a + b

result = add(5, 10)
print("Sum is:", result)

# ---------------------------------------------------------
# 3. DEFAULT PARAMETERS
# ---------------------------------------------------------

# SYNTAX:
# def function_name(parameter=default_value):
#     function body

def greet(name="Guest"):
    """Greets a user, default name is 'Guest'"""
    print(f"Hello {name}!")

greet("Nived")
greet()  # Uses default value

# ---------------------------------------------------------
# 4. POSITIONAL AND KEYWORD ARGUMENTS
# ---------------------------------------------------------

# SYNTAX:
# def function_name(param1, param2, ...):
#     function body
# function_name(value1, value2, ...)             # positional args
# function_name(param1=value1, param2=value2)    # keyword args

def describe_person(name, age, country):
    """Prints details about a person"""
    print(f"Name: {name}, Age: {age}, Country: {country}")

describe_person("Alice", 22, "India")
describe_person(age=30, name="Bob", country="USA")  # Keyword args (order can change)

# ---------------------------------------------------------
# 5. VARIABLE LENGTH ARGUMENTS (*args, **kwargs)
# ---------------------------------------------------------

# SYNTAX:
# def function_name(*args):      # accepts variable positional arguments
# def function_name(**kwargs):   # accepts variable keyword arguments

def print_numbers(*args):
    """Prints all numbers passed to it"""
    for num in args:
        print(num, end=" ")
    print()

print_numbers(1, 2, 3, 4, 5)

def print_details(**kwargs):
    """Prints all keyword arguments"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Nived", age=18, country="India")

# Both together
def mix_args(*args, **kwargs):
    """Accepts both positional and keyword arguments"""
    print("Positional Arguments:", args)
    print("Keyword Arguments:", kwargs)

mix_args(1, 2, 3, name="John", city="Paris")

# ---------------------------------------------------------
# 6. RETURNING MULTIPLE VALUES
# ---------------------------------------------------------

# SYNTAX:
# def function_name(parameters):
#     return value1, value2, value3 ...

def multiply_and_divide(a, b):
    """Returns multiplication and division of a & b"""
    return a * b, a / b

product, division = multiply_and_divide(10, 2)
print("Product:", product, "| Division:", division)

# ---------------------------------------------------------
# 7. LAMBDA FUNCTIONS (Anonymous Functions)
# ---------------------------------------------------------

# SYNTAX:
# lambda arguments : expression

square = lambda x: x**2
print("Square of 6:", square(6))

# Using lambda with map()
nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, nums))
print("Squared List:", squared)

# ---------------------------------------------------------
# 8. RECURSIVE FUNCTION
# ---------------------------------------------------------

# SYNTAX:
# def function_name(parameters):
#     if base_condition:
#         return value
#     else:
#         return function_name(modified_parameters)

def factorial(n):
    """Calculates factorial of n using recursion"""
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))

# ---------------------------------------------------------
# 9. HIGHER ORDER FUNCTION (Function as Argument)
# ---------------------------------------------------------

# SYNTAX:
# def function_name(func, value):
#     return func(value)

def apply_function(func, value):
    return func(value)

result = apply_function(lambda x: x**3, 3)
print("Cube of 3:", result)

# ---------------------------------------------------------
# 10. FUNCTION RETURNING FUNCTION (CLOSURES)
# ---------------------------------------------------------

# SYNTAX:
# def outer_function():
#     def inner_function():
#         return something
#     return inner_function

def make_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

double = make_multiplier(2)
print("Double of 10:", double(10))

# ---------------------------------------------------------
# 11. PRACTICAL EXAMPLES
# ---------------------------------------------------------

# Example 1: Prime Number Checker
def is_prime(num):
    """Returns True if num is prime"""
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print("Is 13 prime?", is_prime(13))
print("Is 20 prime?", is_prime(20))

# Example 2: Temperature Conversion
def celsius_to_fahrenheit(c):
    """Converts Celsius to Fahrenheit"""
    return (c * 9/5) + 32

print("30°C =", celsius_to_fahrenheit(30), "°F")

# Example 3: Student Grade Function
def get_grade(score):
    """Returns grade based on score"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "Fail"

print("Grade for 85:", get_grade(85))
