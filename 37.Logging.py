"""
📌 LOGGING IN PYTHON
Complete Notes with Syntax, Examples, and Real-World Use Cases
"""

import logging

# ✅ Basic Syntax for Logging
"""
SYNTAX:
import logging
logging.basicConfig(level=logging.<LEVEL>,
                    filename='app.log',
                    filemode='w',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

logging.debug("Debug message")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")
"""

# ✅ Example 1: Basic Logging
logging.basicConfig(level=logging.DEBUG)
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

# ✅ Example 2: Logging with File Output
logging.basicConfig(level=logging.DEBUG,
                    filename='app.log',
                    filemode='w',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

logging.debug("File logging started")
logging.info("Writing logs to file")
logging.warning("Potential issue detected")
logging.error("An error occurred")
logging.critical("Critical failure!")

# ✅ Example 3: Logging inside Functions
def add(a, b):
    logging.debug(f"Adding {a} and {b}")
    return a + b

def divide(a, b):
    try:
        result = a / b
        logging.info(f"Division successful: {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logging.error("Division by zero attempted!")
        return None

logging.debug("Calling add function")
print("Addition Result:", add(5, 10))
print("Division Result:", divide(10, 2))
print("Division Result:", divide(10, 0))

# ✅ Example 4: Using Logger Objects
logger = logging.getLogger("MyApp")
logger.setLevel(logging.DEBUG)

# File Handler
file_handler = logging.FileHandler("custom_app.log")
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Log Messages
logger.debug("Custom logger debug message")
logger.info("Custom logger info message")
logger.warning("Custom logger warning")
logger.error("Custom logger error")
logger.critical("Custom logger critical")

# ✅ Practical Example: Logging in a Real-World Scenario
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        logging.info(f"Account created for {owner} with balance {balance}")

    def deposit(self, amount):
        self.balance += amount
        logging.info(f"{self.owner} deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            logging.error(f"{self.owner} attempted to withdraw {amount}, but balance is {self.balance}")
            print("Insufficient funds!")
        else:
            self.balance -= amount
            logging.info(f"{self.owner} withdrew {amount}. New balance: {self.balance}")

# Test the Class
account = BankAccount("Nived", 1000)
account.deposit(500)
account.withdraw(2000)  # Logs error
account.withdraw(300)   # Logs success

"""
📌 KEY TAKEAWAYS:
- logging.basicConfig() is used to configure logging.
- logging levels: DEBUG < INFO < WARNING < ERROR < CRITICAL
- Logs can be directed to console or file.
- Use logger objects for modular logging in large applications.
- Use logging instead of print() for production-ready code.
"""
