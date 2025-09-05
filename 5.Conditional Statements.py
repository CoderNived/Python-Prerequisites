age = 20

# ==============================
# Simple If Statement
# ==============================
if age >= 20:
    print("You have reached the legal drinking age.")  # ✅ Spelling fixed

# ==============================
# If-Else Statement
# ==============================
if age < 18:
    print("You are not eligible.")  # ✅ Fixed spelling
else:
    print("You are eligible.")

# ==============================
# If-Elif-Else Statement
# ==============================
if age < 13:
    print("You are a child.")
elif age < 18:
    print("You are a teenager.")
else:
    print("You are an adult.")

# ==============================
# Nested If Example
# ==============================
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
    if num % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
else:
    print("The number is negative.")

# ==============================
# Practical Example 1: Leap Year Check
# ==============================
year = int(input("Enter a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a leap year.")
        else:
            print(year, "is not a leap year.")
    else:
        print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

# ==============================
# Practical Example 2: Simple Calculator
# ==============================
print("\n--- Simple Calculator ---")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    print("Result:", num1 + num2)
elif operation == "-":
    print("Result:", num1 - num2)
elif operation == "*":
    print("Result:", num1 * num2)
elif operation == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation.")

# ==============================
# Practical Example 3: Ticket Pricing
# ==============================
age = int(input("\nEnter your age: "))
student = input("Are you a student? (yes/no): ").lower()

if age < 12:
    price = 50
elif age < 18:
    price = 100
elif student == "yes":
    price = 120
else:
    price = 200

print("Your ticket price is:", price)

# ==============================
# MORE IF-ELSE EXAMPLES
# ==============================

# Example 4: Grading System
marks = int(input("\nEnter your marks (0-100): "))
if marks >= 90:
    print("Grade: A+")
elif marks >= 75:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
elif marks >= 40:
    print("Grade: C")
else:
    print("Grade: F (Fail)")

# Example 5: Password Check
password = input("\nEnter your password: ")
if password == "admin123":
    print("Access granted!")
else:
    print("Access denied!")

# Example 6: Weather Check
temperature = float(input("\nEnter temperature in °C: "))
if temperature > 35:
    print("It's very hot! Stay hydrated.")
elif temperature > 25:
    print("It's warm outside.")
elif temperature > 15:
    print("It's a pleasant day.")
elif temperature > 5:
    print("It's a bit cold, wear a jacket.")
else:
    print("It's freezing! Stay warm.")

# Example 7: Odd/Even with Short Syntax
num = int(input("\nEnter a number to check odd/even: "))
print("Even number!" if num % 2 == 0 else "Odd number!")  # ✅ Inline if-else

