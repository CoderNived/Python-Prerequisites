
"""
===========================================================
📌 PYTHON CUSTOM EXCEPTIONS – COMPLETE NOTES (MASTER FILE)
===========================================================

✅ What are Custom Exceptions?
Custom Exceptions are user-defined error types that extend Python's built-in Exception class.
They make error handling more meaningful and structured for specific use cases.

✅ When to Use Custom Exceptions?
- When you want to differentiate application-specific errors from generic ones.
- When you want clear, descriptive error messages for debugging or logging.
- When building larger applications where multiple error types may occur.

✅ Syntax:
class MyCustomError(Exception):
    ""Custom Exception class"
    pass

try:
    # Code that may raise custom error
    raise MyCustomError("This is a custom error")
except MyCustomError as e:
    print(f"Caught custom exception: {e}")
"""

# ===========================================================
# 1️⃣ BASIC EXAMPLE – AGE VALIDATION
# ===========================================================
class Error(Exception):
    """Base class for other custom exceptions."""
    pass

class DobException(Error):
    """Raised when age is outside the valid range."""
    pass

try:
    year = int(input("Enter your year of birth: "))
    age = 2025 - year
    if 20 <= age <= 30:
        print("✅ Age is valid. You can apply for the exam.")
    else:
        raise DobException
except DobException:
    print("❌ Sorry, your age must be between 20 and 30.")
except ValueError:
    print("❌ Invalid input. Please enter a number for year of birth.")

print("-" * 60)

# ===========================================================
# 2️⃣ BANKING SYSTEM EXAMPLE – INSUFFICIENT FUNDS
# ===========================================================
class InsufficientFundsError(Exception):
    """Raised when withdrawal exceeds account balance."""
    def __init__(self, balance, amount):
        super().__init__(f"Insufficient Funds! Balance: {balance}, Attempted: {amount}")

class BankAccount:
    """Simple bank account class to demonstrate custom exception use."""
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Deposit money into the account."""
        self.balance += amount
        print(f"✅ Deposited {amount}. New Balance: {self.balance}")

    def withdraw(self, amount):
        """Withdraw money from the account (raises exception if insufficient)."""
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        print(f"✅ Withdrawn {amount}. New Balance: {self.balance}")

try:
    account = BankAccount("Nived", 1000)
    account.deposit(500)
    account.withdraw(200)
    account.withdraw(2000)  # Will raise custom exception
except InsufficientFundsError as e:
    print(f"❌ Exception: {e}")

print("-" * 60)

# ===========================================================
# 3️⃣ FACTORIAL FUNCTION – NEGATIVE NUMBER CHECK
# ===========================================================
class NegativeNumberError(Exception):
    """Raised when a negative number is passed to factorial."""
    pass

def factorial(n):
    """Calculate factorial with custom exception for negative numbers."""
    if n < 0:
        raise NegativeNumberError("Factorial not defined for negative numbers")
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

try:
    num = int(input("Enter a number to calculate factorial: "))
    print(f"Factorial of {num}: {factorial(num)}")
except NegativeNumberError as e:
    print(f"❌ {e}")
except ValueError:
    print("❌ Please enter a valid integer.")

print("-" * 60)

# ===========================================================
# 4️⃣ EMAIL VALIDATION EXAMPLE – CHAINING EXCEPTIONS
# ===========================================================
class InvalidEmailError(Exception):
    """Raised when email format is invalid."""
    pass

def validate_email(email):
    """Simple validation to check if '@' is present in email."""
    if "@" not in email:
        raise InvalidEmailError(f"'{email}' is not a valid email address")

try:
    email = input("Enter your email: ")
    validate_email(email)
    print("✅ Email is valid!")
except InvalidEmailError as e:
    print(f"❌ Custom Exception: {e}")
except Exception as e:
    print(f"❌ Unexpected error: {e}")

print("-" * 60)

"""
===========================================================
📌 BEST PRACTICES FOR CUSTOM EXCEPTIONS
===========================================================

1️⃣ Always inherit from Exception or a subclass (not BaseException directly).
2️⃣ Use meaningful names (e.g., `InvalidAgeError`, `PaymentFailedError`).
3️⃣ Provide descriptive error messages when raising exceptions.
4️⃣ Use a hierarchy of exceptions in complex applications (BaseError -> SpecificError).
5️⃣ Catch exceptions at the right place and handle them gracefully (log, retry, or exit).
6️⃣ Do not use exceptions for normal control flow — reserve them for exceptional cases.
"""



