# =========================================================
# MAP() FUNCTION IN PYTHON
# =========================================================
# Syntax: map(function, iterable, ...)
# map() applies a given function to all items in an iterable (list, tuple, etc.)
# It returns a map object, which can be converted to list, tuple, or set.

# Example 1: Using normal function
def square(x):
    return x ** 2
print("Square of 10:", square(10))

# Lambda Function with map()
numbers = [1, 2, 3, 45, 6, 7]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Squared Numbers:", squared_numbers)


# Example 2: Map with Multiple Iterables
numbers1 = [1, 2, 3, 4, 5, 6, 7, 8]
numbers2 = [1, 2, 3, 3, 5, 6, 7]
addition = list(map(lambda x, y: x + y, numbers1, numbers2))
print("Addition of Two Lists:", addition)


# Example 3: Map with Built-in Functions
words = ["apple", "banana", "cherry"]
upper_words = list(map(str.upper, words))   # Using str.upper directly
print("Uppercase Words:", upper_words)

lower_words = list(map(str.lower, words))
print("Lowercase Words:", lower_words)

lengths = list(map(len, words))
print("Length of Words:", lengths)


# Example 4: Map with Custom Function
def get_name(person):
    return person["name"]

people = [
    {"name": "Nived", "age": 15},
    {"name": "Krish", "age": 18},
    {"name": "Satyanarayan", "age": 45}
]

names = list(map(get_name, people))
print("Extracted Names:", names)


# Example 5: Converting Strings to Integers
str_numbers = ['1', '2', '3', '4', '5', '6']
int_numbers = list(map(int, str_numbers))
print("Converted Integers:", int_numbers)


# Example 6: Map with Conditional Logic
# Convert numbers: if even -> square, if odd -> cube
numbers = [1, 2, 3, 4, 5]
transformed = list(map(lambda x: x ** 2 if x % 2 == 0 else x ** 3, numbers))
print("Even->Square, Odd->Cube:", transformed)


# Example 7: Map with Multiple Functions
# Apply different functions on the same list
def square(x): return x ** 2
def cube(x): return x ** 3

funcs = [square, cube]
for f in funcs:
    print(list(map(f, [1, 2, 3, 4, 5])))


# Example 8: Map with Nested List
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flatten = list(map(lambda sublist: [x * 2 for x in sublist], nested_list))
print("Doubled Nested List:", flatten)


# Example 9: Map + str Methods
emails = ["user1@gmail.com", "user2@yahoo.com", "user3@outlook.com"]
domains = list(map(lambda email: email.split("@")[1], emails))
print("Extracted Domains:", domains)


# Example 10: Map with Tuples
students = [("Nived", 18), ("Krish", 20), ("Jack", 22)]
only_names = list(map(lambda x: x[0], students))
only_ages = list(map(lambda x: x[1], students))
print("Student Names:", only_names)
print("Student Ages:", only_ages)


