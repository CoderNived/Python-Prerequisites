# ==========================================
# TUPLES IN PYTHON
# ==========================================

# Creating Tuples
empty_tuple = ()
print("Empty Tuple:", empty_tuple, "Type:", type(empty_tuple))

tpl = tuple()
print("Empty Tuple using tuple():", tpl)

numbers = (1, 2, 3, 4, 5)
numbers2 = tuple([1, 2, 3, 4, 5])  # Creating tuple from list

mixed_tuple = (1, "name", True, 3.14)
print("Mixed Tuple:", mixed_tuple)

# Single element tuple - NOTE: must have a comma!
single = (5,)
print("Single Element Tuple:", single, "Type:", type(single))

# ==========================================
# ACCESSING ELEMENTS
# ==========================================
print("\n--- Accessing Elements ---")
print(numbers[0])      # First element
print(numbers[-1])     # Last element
print(numbers[1:3])    # Slicing
print(numbers[::-1])   # Reverse tuple

# ==========================================
# TUPLE OPERATIONS
# ==========================================
print("\n--- Tuple Operations ---")
a = numbers + mixed_tuple   # Concatenation
print("Concatenated:", a)

b = numbers * 3             # Repetition
print("Repeated:", b)

print("Is 3 in numbers?", 3 in numbers)  # Membership

# ==========================================
# IMMUTABILITY
# ==========================================
# numbers[0] = 100  # ❌ This will throw error (Tuples are immutable)

# ==========================================
# TUPLE METHODS
# ==========================================
print("\n--- Tuple Methods ---")
print("Count of 1:", numbers.count(1))
print("Index of 4:", numbers.index(4))

# ==========================================
# PACKING & UNPACKING
# ==========================================
print("\n--- Packing & Unpacking ---")
packed_tuple = 1, "hello", 3.14  # Packing
print("Packed Tuple:", packed_tuple)

a, b, c = packed_tuple  # Unpacking
print(a, b, c)

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
first, *middle, last = numbers  # Unpacking with *
print("First:", first)
print("Middle:", middle)
print("Last:", last)

# ==========================================
# NESTED TUPLES
# ==========================================
print("\n--- Nested Tuples ---")
nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print("Nested Tuple:", nested_tuple)
print("Second Subtuple:", nested_tuple[1])
print("Element 8:", nested_tuple[2][1])

# Iterating over Nested Tuples
for sub_tuple in nested_tuple:
    for item in sub_tuple:
        print(item, end=" ")
    print()

# ==========================================
# PRACTICAL EXAMPLES
# ==========================================

print("\n--- Practical Examples ---")

# 1. Returning Multiple Values from a Function
def min_max(nums):
    return (min(nums), max(nums))

result = min_max([5, 1, 9, 3, 7])
print("Min & Max:", result)

# 2. Using Tuple as Dictionary Keys (Immutable)
locations = {
    ("New York", "USA"): 8_000_000,
    ("Mumbai", "India"): 20_000_000,
}
print("Population of Mumbai:", locations[("Mumbai", "India")])

# 3. Storing Coordinates
point = (12.5, 45.8)
print("Latitude:", point[0], "Longitude:", point[1])

# 4. Swapping Variables
x, y = 10, 20
x, y = y, x
print("After Swapping -> x:", x, "y:", y)

# 5. Enumerating with Tuple
for idx, value in enumerate(("a", "b", "c")):
    print(f"Index {idx} -> Value {value}")

# 6. Tuple for Immutable Config
CONFIG = ("localhost", 8080, True)  # host, port, debug_mode
print("Server Config:", CONFIG)

# 7. Zipping into Tuple
names = ["Alice", "Bob", "Charlie"]
marks = [85, 92, 78]
students = list(zip(names, marks))
print("Students with Marks:", students)

# 8. Tuple Unpacking in Loops
for name, mark in students:
    print(f"{name} scored {mark}")

