# ==============================
# FOR LOOP BASICS
# ==============================

print("\n--- Basic For Loops ---")
for i in range(5):  # range(5) → 0 to 4
    print(i)

print("\nRange with start and end:")
for i in range(1, 6):  # range(start, end) → end is excluded
    print(i)

print("\nRange with step value:")
for i in range(1, 40, 10):  # range(start, end, step)
    print(i)

# Loop through a string
print("\nLooping through a string:")
str_val = "Nived Shenoy"
for char in str_val:
    print(char)

# ==============================
# WHILE LOOPS
# ==============================
print("\n--- While Loop Example ---")
count = 0
while count < 5:
    print(count)
    count += 1  # Increment to avoid infinite loop

print("\nExample with condition:")
count = 0
while count % 2 == 0:  # Will run only once because count=0 is even
    print("Count was even, incrementing it.")
    count += 1

# ==============================
# LOOP CONTROL STATEMENTS
# ==============================

# Break: exits loop permanently
print("\n--- Break Example ---")
for i in range(10):
    if i == 5:
        break  # loop stops when i = 5
    print(i)

# Continue: skips current iteration
print("\n--- Continue Example (Print only odd numbers) ---")
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)

# Pass: does nothing (used as a placeholder)
print("\n--- Pass Example ---")
for i in range(5):
    if i == 3:
        pass  # Nothing happens, loop continues
    print(i)

# Nested Loops: Loop inside a loop
print("\n--- Nested Loops Example ---")
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

# ==============================
# PRACTICAL EXAMPLES
# ==============================

# 1. Sum of first n natural numbers (while loop)
print("\n--- Sum of First 10 Numbers (While Loop) ---")
n = 10
total = 0
count = 1
while count <= n:
    total += count
    count += 1
print("Sum of first 10 natural numbers:", total)

# 2. Sum of first n natural numbers (for loop)
print("\n--- Sum of First 10 Numbers (For Loop) ---")
total = 0
for i in range(1, 11):
    total += i
print(total)

# 3. Print prime numbers between 1 to 100
print("\n--- Prime Numbers from 1 to 100 ---")
for num in range(1, 101):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, end=" ")
print()

# ==============================
# MORE PRACTICAL LOOP EXAMPLES
# ==============================

# 4. Multiplication Table
print("\n--- Multiplication Table of 5 ---")
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

# 5. Factorial of a Number
print("\n--- Factorial of a Number ---")
num = 5
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"Factorial of {num} is {factorial}")

# 6. Reverse a String
print("\n--- Reverse a String ---")
text = "Python"
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text
print("Reversed String:", reversed_text)

# 7. Count Vowels in a String
print("\n--- Count Vowels in a String ---")
text = "Programming is fun"
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count += 1
print(f"Number of vowels in '{text}':", count)

# 8. Find Sum of Even and Odd Numbers Separately
print("\n--- Sum of Even and Odd Numbers from 1 to 20 ---")
even_sum = 0
odd_sum = 0
for i in range(1, 21):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print("Even Sum:", even_sum)
print("Odd Sum:", odd_sum)

# 9. Guess the Number Game (Fun Example)
print("\n--- Guess the Number Game ---")
secret_number = 7
attempts = 0
while True:
    guess = int(input("Guess a number between 1 and 10: "))
    attempts += 1
    if guess == secret_number:
        print(f"🎉 Correct! You guessed it in {attempts} tries.")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
