"""
===========================
📌 Iterators in Python – Complete Notes
===========================

✅ What is an Iterator?
- An iterator is an object that allows us to traverse (iterate) through a collection (like a list, tuple, string).
- Uses two main methods:
    __iter__() → returns the iterator object itself.
    __next__() → returns the next item, raises StopIteration when no more items are left.

✅ Syntax:
iterable = [1, 2, 3]
iterator = iter(iterable)  # get iterator object
print(next(iterator))      # get next element
print(next(iterator))

✅ Difference Between Iterable & Iterator:
- Iterable: any object that can return an iterator (list, tuple, string, etc.)
- Iterator: the object that performs iteration, keeps track of the current position.
"""

# ---------------------------
# BASIC ITERATOR EXAMPLE
# ---------------------------
my_list = [1, 2, 3, 4, 5, 6]
print("Original List:", my_list)

# Create an iterator
iterator = iter(my_list)
print("Iterator Object Type:", type(iterator))

# Access elements one by one
print("First Element:", next(iterator))
print("Second Element:", next(iterator))

# Iterate using a loop
print("Remaining Elements using Loop:")
for item in iterator:
    print(item)
print("-" * 50)

# ---------------------------
# STRING ITERATOR EXAMPLE
# ---------------------------
my_string = "Hello"
string_iterator = iter(my_string)

print("String Iterator Example:")
try:
    while True:
        print(next(string_iterator))
except StopIteration:
    print("Reached end of string.")
print("-" * 50)

# ---------------------------
# CUSTOM ITERATOR CLASS
# ---------------------------
class CountDown:
    """Custom iterator to count down from a given number."""
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        current = self.start
        self.start -= 1
        return current

print("Custom Iterator Example (Countdown):")
countdown = CountDown(5)
for num in countdown:
    print(num)
print("-" * 50)

# ---------------------------
# ITERATOR OVER DICTIONARY
# ---------------------------
students = {"name": "Nived", "age": 18, "grade": "A"}
print("Iterating Over Dictionary Keys:")
for key in iter(students):
    print(f"{key} -> {students[key]}")
print("-" * 50)

# ---------------------------
# ITERATOR WITH TUPLES
# ---------------------------
my_tuple = (10, 20, 30)
tuple_iterator = iter(my_tuple)
print("Tuple Iterator Example:")
print(next(tuple_iterator))
print(next(tuple_iterator))
print(next(tuple_iterator))
print("-" * 50)

# ---------------------------
# REAL-WORLD USE CASE: ITERATOR FOR PAGINATION
# ---------------------------
class Paginator:
    """Simulates pagination using an iterator."""
    def __init__(self, items, page_size):
        self.items = items
        self.page_size = page_size
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index >= len(self.items):
            raise StopIteration
        page = self.items[self.current_index:self.current_index + self.page_size]
        self.current_index += self.page_size
        return page

print("Pagination Example:")
data = list(range(1, 21))  # data from 1 to 20
paginator = Paginator(data, page_size=5)
for page in paginator:
    print("Page:", page)
print("-" * 50)

# ---------------------------
# MANUAL ITERATION WITH try/except
# ---------------------------
iterator = iter([100, 200, 300])
print("Manual Iteration with try/except:")
while True:
    try:
        print(next(iterator))
    except StopIteration:
        print("End of iterator reached.")
        break
print("-" * 50)

"""
✅ When to Use Iterators:
- When you need memory-efficient access to data (one item at a time).
- When you are working with streams, large datasets, or infinite sequences.
- When you want to implement custom sequence logic (like pagination, countdown, etc.)
"""


