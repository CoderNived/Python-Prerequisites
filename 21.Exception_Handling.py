""" 
📌 EXCEPTION HANDLING IN PYTHON
Complete Notes with Syntax, Examples, and Concepts
"""

# ✅ Basic Exception Handling
try:
    a = int(input("Enter a number: "))
    print("You entered:", a)
except ValueError:
    print("Invalid input! Please enter a number.")

# ✅ Catching Multiple Exceptions
try:
    x = int(input("Enter numerator: "))
    y = int(input("Enter denominator: "))
    result = x / y
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input! Please enter numbers only.")

# ✅ Using else with try-except
try:
    x = int(input("Enter a number: "))
except ValueError:
    print("Invalid input!")
else:
    print(f"{x} is a valid number.")  # Runs only if no exception occurs

# ✅ Using finally for Cleanup
try:
    file = open("example.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found!")
finally:
    print("Closing file (if open).")
    try:
        file.close()
    except:
        pass

# ✅ Catching All Exceptions
try:
    x = int("abc")  # This will raise ValueError
except Exception as e:
    print(f"An error occurred: {e}")

# ✅ Raising Your Own Exceptions
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds!")
    return balance - amount

try:
    new_balance = withdraw(1000, 1500)
    print("New Balance:", new_balance)
except ValueError as e:
    print("Error:", e)

# ✅ Custom Exceptions
class NegativeNumberError(Exception):
    pass

def square_root(x):
    if x < 0:
        raise NegativeNumberError("Cannot take square root of a negative number!")
    return x ** 0.5

try:
    print(square_root(-9))
except NegativeNumberError as e:
    print("Custom Exception:", e)

# ✅ Practical Example: Safe Calculator
def safe_division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return None
    except TypeError:
        print("Inputs must be numbers!")
        return None
    else:
        print("Division successful.")
    finally:
        print("Division operation completed.")

print(safe_division(10, 2))
print(safe_division(10, 0))
print(safe_division(10, "five"))

# ✅ Common Python Exceptions Table (for reference)
"""
ValueError       - Raised when wrong value is passed to a function.
ZeroDivisionError- Raised when dividing by zero.
TypeError        - Raised when operation is applied to wrong type.
IndexError       - Raised when invalid index is accessed.
KeyError         - Raised when key not found in dictionary.
FileNotFoundError- Raised when file does not exist.
ImportError      - Raised when module import fails.
AttributeError   - Raised when attribute is missing.
"""
