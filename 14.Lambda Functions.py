# =========================================================
# LAMBDA FUNCTIONS IN PYTHON
# =========================================================

# Syntax: lambda arguments: expression
# A lambda function is an anonymous function (no name) that can have any number of arguments, 
# but only one expression.

# Example 1: Basic Addition
def addition(a, b):
    return a + b

# Using lambda
addition = lambda a, b: a + b
print("Lambda Addition:", addition(5, 6))


# Example 2: Even Check
def even(num):
    if num % 2 == 0:
        return True
    return False

# Lambda version
even1 = lambda num: num % 2 == 0
print("Even Check (12):", even1(12))
print("Even Check (15):", even1(15))


# Example 3: Multiple Arguments
def addition(x, y, z):
    return x + y + z

# Lambda version
addition = lambda x, y, z: x + y + z
print("Sum of 12, 13, 14:", addition(12, 13, 14))


# =========================================================
# LAMBDA WITH BUILT-IN FUNCTIONS
# =========================================================

numbers = [1, 2, 3, 4, 5, 6, 7]

# 1️⃣ map() - Apply a function to all items in an iterable
# Example: Square all numbers
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Squares:", squared_numbers)

# Example: Convert Celsius to Fahrenheit
temps_celsius = [0, 20, 30, 40]
temps_fahrenheit = list(map(lambda c: (c * 9/5) + 32, temps_celsius))
print("Temperatures in Fahrenheit:", temps_fahrenheit)


# 2️⃣ filter() - Filter items based on a condition
# Example: Get even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", even_numbers)

# Example: Get numbers greater than 3
greater_than_three = list(filter(lambda x: x > 3, numbers))
print("Numbers > 3:", greater_than_three)


# 3️⃣ reduce() - Cumulative computation (needs functools)
from functools import reduce

# Example: Sum of numbers
sum_of_numbers = reduce(lambda a, b: a + b, numbers)
print("Sum of Numbers:", sum_of_numbers)

# Example: Product of numbers
product_of_numbers = reduce(lambda a, b: a * b, numbers)
print("Product of Numbers:", product_of_numbers)


# 4️⃣ sorted() with key
# Example: Sort words by length
words = ["apple", "kiwi", "banana", "grape"]
sorted_words = sorted(words, key=lambda word: len(word))
print("Words sorted by length:", sorted_words)

# Example: Sort dictionary by value
my_dict = {"a": 3, "b": 1, "c": 2}
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Dictionary sorted by value:", sorted_dict)


# 5️⃣ Custom Key Functions with max() / min()
students = [
    {"name": "Alice", "marks": 88},
    {"name": "Bob", "marks": 92},
    {"name": "Charlie", "marks": 79},
]

# Get student with highest marks
top_student = max(students, key=lambda x: x['marks'])
print("Top Student:", top_student)

# Get student with lowest marks
lowest_student = min(students, key=lambda x: x['marks'])
print("Lowest Student:", lowest_student)


# 6️⃣ Using Lambda for Inline Conditional Expressions
check_age = lambda age: "Adult" if age >= 18 else "Minor"
print("Age 20:", check_age(20))
print("Age 15:", check_age(15))


# 7️⃣ Lambda inside List Comprehension
double_odd_numbers = [(lambda x: x * 2)(x) for x in numbers if x % 2 != 0]
print("Doubled Odd Numbers:", double_odd_numbers)


# 8️⃣ Combining map() + filter() + lambda
# Example: Get squares of only even numbers
even_squares = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print("Squares of Even Numbers:", even_squares)
