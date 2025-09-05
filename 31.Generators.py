"""
===========================
📌 Generators in Python – Complete Notes
===========================

✅ What is a Generator?
- A generator is a special type of function that returns an iterator object.
- Instead of using `return`, it uses `yield` to produce values one by one.
- Execution state is saved between calls, so it resumes where it left off.
- Very memory efficient (does not store all values at once).

✅ Syntax:
def generator_name(parameters):
    # Some code
    yield value1
    yield value2
    ...

✅ Usage:
gen = generator_name()
next(gen)       # Get next value manually
for val in gen: # Iterate through all values
    print(val)

"""

# ---------------------------
# BASIC GENERATOR EXAMPLE
# ---------------------------
def count_upto(n):
    """Generator that yields numbers from 0 to n."""
    for i in range(n + 1):
        yield i

print("Basic Generator Example:")
gen = count_upto(5)
print(next(gen))  # 0
print(next(gen))  # 1
for num in gen:
    print(num)    # Prints 2,3,4,5
print("-" * 50)

# ---------------------------
# DIFFERENCE BETWEEN RETURN AND YIELD
# ---------------------------
def normal_func():
    return 1
    return 2  # Never executed

print("Normal Function:", normal_func())  # 1

def generator_func():
    yield 1
    yield 2

print("Generator Example:")
gen = generator_func()
print(next(gen))  # 1
print(next(gen))  # 2
print("-" * 50)

# ---------------------------
# GENERATOR: SQUARE NUMBERS
# ---------------------------
def generate_squares(n):
    """Yields squares of numbers from 0 to n-1"""
    for i in range(n):
        yield i ** 2

print("Squares Generator:")
for sq in generate_squares(5):
    print(sq)
print("-" * 50)

# ---------------------------
# GENERATOR: FIBONACCI SERIES
# ---------------------------
def fibonacci(limit):
    """Generator for Fibonacci sequence up to a limit."""
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

print("Fibonacci Series:")
for num in fibonacci(50):
    print(num, end=" ")
print("\n" + "-" * 50)

# ---------------------------
# GENERATOR: EVEN NUMBERS
# ---------------------------
def even_numbers(n):
    """Yields even numbers up to n."""
    for i in range(0, n + 1, 2):
        yield i

print("Even Numbers:")
for even in even_numbers(10):
    print(even)
print("-" * 50)

# ---------------------------
# GENERATOR: LAZY FILE READER
# ---------------------------
def read_file_line_by_line(filename):
    """Reads a file line by line lazily using a generator."""
    with open(filename, "r") as file:
        for line in file:
            yield line.strip()

# (Create a file for demo)
with open("sample.txt", "w") as f:
    f.write("Line 1\nLine 2\nLine 3\n")

print("Lazy File Reading Example:")
for line in read_file_line_by_line("sample.txt"):
    print(line)
print("-" * 50)

# ---------------------------
# GENERATOR EXPRESSIONS (One-Liners)
# ---------------------------
print("Generator Expression Example:")
gen_exp = (x ** 2 for x in range(5))
for val in gen_exp:
    print(val)
print("-" * 50)

# ---------------------------
# REAL-WORLD USE CASE: MEMORY EFFICIENT DATA STREAM
# ---------------------------
def data_stream():
    """Simulates a data stream (infinite generator)."""
    n = 0
    while True:
        yield n
        n += 1

print("Streaming Data (First 5 values):")
stream = data_stream()
for _ in range(5):
    print(next(stream))
print("-" * 50)
