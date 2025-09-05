# =========================================================
# FILTER() FUNCTION IN PYTHON
# =========================================================
# Syntax: filter(function, iterable)
# filter() constructs an iterator from elements of an iterable 
# for which the function returns True.
# It is generally used to filter out unwanted elements from a sequence.

# Example 1: Using a Normal Function
def even(num):
    if num % 2 == 0:
        return True

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 132, 421]
even_numbers = list(filter(even, lst))
print("Even Numbers:", even_numbers)

# Example 2: Filter with Lambda Function
numbers = [1, 2, 3, 4, 5, 6, 78, 9]
greater_than_five = list(filter(lambda x: x > 5, numbers))
print("Numbers > 5:", greater_than_five)

# Example 3: Filter with Multiple Conditions
greater_than_five_and_even = list(filter(lambda x: x > 5 and x % 2 == 0, numbers))
print("Numbers > 5 and Even:", greater_than_five_and_even)

# Example 4: Filter with Dictionary (Real World)
people = [
    {"name": "Nived", "age": 15},
    {"name": "Krish", "age": 18},
    {"name": "Satyanarayan", "age": 45},
    {"name": "Ramesh", "age": 32}
]

def age_greater_than_25(person):
    return person['age'] > 25

adults = list(filter(age_greater_than_25, people))
print("People with Age > 25:", adults)

# Example 5: Filter with Lambda + Dictionary
adults_lambda = list(filter(lambda p: p['age'] > 25, people))
print("People with Age > 25 (Lambda):", adults_lambda)

# Example 6: Filtering Out Empty Strings
words = ["apple", "", "banana", "", "grape"]
non_empty_words = list(filter(None, words))  # None removes "Falsey" values
print("Non-empty Words:", non_empty_words)

# Example 7: Filter with Custom Function for Prime Numbers
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

numbers = list(range(1, 30))
prime_numbers = list(filter(is_prime, numbers))
print("Prime Numbers (1-30):", prime_numbers)

# Example 8: Filter Odd Numbers using Lambda
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print("Odd Numbers:", odd_numbers)

# Example 9: Filter with Strings (Names starting with "K")
names = ["Krish", "Nived", "Kiran", "John"]
names_starting_with_k = list(filter(lambda name: name.startswith("K"), names))
print("Names starting with K:", names_starting_with_k)

# Example 10: Filter Numbers That Are Multiples of 3
multiples_of_3 = list(filter(lambda x: x % 3 == 0, numbers))
print("Multiples of 3:", multiples_of_3)

# Example 11: Filter with Booleans (Remove False Values)
bool_list = [True, False, True, False, True]
true_values = list(filter(lambda x: x, bool_list))
print("Only True Values:", true_values)

# Example 12: Combining filter() with map() (Advanced)
# First filter even numbers, then square them
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_squares = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print("Squares of Even Numbers:", even_squares)
