"""
=========================
Python Logging – Detailed Notes
=========================
Logging is a built-in Python module used to record messages, debug information, warnings, errors, and critical events.

------------------------
🔑 Why Logging?
------------------------
- Helps in debugging instead of using print()
- Records important events and errors
- Can log to console, files, or even external systems
- Allows filtering messages based on severity level

------------------------
📌 Syntax:
------------------------
import logging

# Configure Logging
logging.basicConfig(
    level=logging.DEBUG,                    # Minimum log level to capture
    filename='app.log',                     # Optional: save logs to a file
    filemode='w',                           # 'w' → overwrite, 'a' → append
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Example Usage
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

------------------------
🎯 Log Levels (Lowest → Highest)
------------------------
DEBUG      – Detailed information, for developers
INFO       – General information about program execution
WARNING    – Something unexpected happened, program still works
ERROR      – Serious issue, program might fail
CRITICAL   – Very serious error, program cannot continue
"""

import logging

# ===================================
# 1️⃣ Basic Logging Setup
# ===================================
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logging.debug("Debugging message example")
logging.info("Info message example")
logging.warning("Warning message example")
logging.error("Error message example")
logging.critical("Critical message example")

# ===================================
# 2️⃣ Multiple Loggers
# ===================================
logger1 = logging.getLogger("module1")
logger1.setLevel(logging.DEBUG)

logger2 = logging.getLogger("module2")
logger2.setLevel(logging.WARNING)

logger1.debug("This is a debug message from module1")
logger1.info("Module1 info message")
logger2.warning("Module2 warning message")
logger2.error("Module2 error message")

# ===================================
# 3️⃣ Logging to File
# ===================================
file_logger = logging.getLogger("fileLogger")
file_handler = logging.FileHandler("logs.txt", mode='w')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
file_logger.addHandler(file_handler)
file_logger.setLevel(logging.INFO)

file_logger.info("This message is written to logs.txt")
file_logger.error("This error is also stored in logs.txt")

# ===================================
# 4️⃣ Custom Handlers (Console + File)
# ===================================
custom_logger = logging.getLogger("customLogger")
custom_logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter('%(name)s - %(levelname)s - %(message)s'))

file_handler2 = logging.FileHandler("combined_logs.txt")
file_handler2.setFormatter(formatter)

custom_logger.addHandler(console_handler)
custom_logger.addHandler(file_handler2)

custom_logger.debug("Debug log (seen in console and file)")
custom_logger.info("Info log (both console + file)")

# ===================================
# 5️⃣ Practical Example: Function Logging
# ===================================
def add(a, b):
    logging.debug(f"Adding {a} + {b}")
    result = a + b
    logging.info(f"Result: {result}")
    return result

add(10, 5)

# ===================================
# 6️⃣ Exception Handling with Logging
# ===================================
try:
    x = 10 / 0
except ZeroDivisionError as e:
    logging.exception("Exception occurred!")  # Automatically includes traceback

# ===================================
# 7️⃣ Advanced Concept: Rotating Log Files
# ===================================
from logging.handlers import RotatingFileHandler

rot_logger = logging.getLogger("rotatingLogger")
rot_logger.setLevel(logging.DEBUG)

rot_handler = RotatingFileHandler("rotating.log", maxBytes=200, backupCount=3)
rot_handler.setFormatter(formatter)

rot_logger.addHandler(rot_handler)

for i in range(20):
    rot_logger.info(f"Logging event {i}")

# ===================================
# 8️⃣ Use Case in ML/AI Pipeline
# ===================================
def train_model():
    logging.info("Training model started")
    for epoch in range(1, 6):
        loss = 1 / epoch
        logging.debug(f"Epoch {epoch} - Loss: {loss}")
    logging.info("Training completed successfully!")

train_model()

"""
💡 Key Tips:
- Use logging instead of print() in production code
- Different modules can use different loggers
- Use logging.exception() inside except blocks to capture traceback
- Use RotatingFileHandler to avoid very large log files
- Log training progress, API calls, and errors in ML projects
"""
