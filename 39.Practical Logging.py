import logging

# ==============================
# Configure Logging Settings
# ==============================
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),     # Logs stored in file
        logging.StreamHandler()              # Logs displayed on console
    ]
)

logger = logging.getLogger("ArithmeticApp")

# ==============================
# Arithmetic Functions
# ==============================
def add(a, b):
    result = a + b
    logger.debug(f"Adding {a} + {b} = {result}")
    return result

def mul(a, b):
    result = a * b
    logger.debug(f"Multiplying {a} * {b} = {result}")
    return result

def sub(a, b):
    result = a - b
    logger.debug(f"Subtracting {a} - {b} = {result}")
    return result

def div(a, b):
    try:
        result = a / b
        logger.debug(f"Dividing {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None

# ==============================
# Function Calls with Logging
# ==============================
logger.info("Arithmetic operations started")

logger.info(f"Result of add(23, 4): {add(23, 4)}")
logger.info(f"Result of sub(23, 4): {sub(23, 4)}")
logger.info(f"Result of mul(23, 5): {mul(23, 5)}")
logger.info(f"Result of div(4, 5): {div(4, 5)}")
logger.info(f"Result of div(4, 0): {div(4, 0)}")  # Triggers error logging

logger.info("Arithmetic operations completed")
