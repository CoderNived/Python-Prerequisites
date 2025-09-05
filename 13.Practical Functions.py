# =========================================================
# PRACTICAL FUNCTION EXAMPLES
# =========================================================

# 1️⃣ SIMPLE CALCULATOR FUNCTION
def calculator(a, b, operator):
    """Performs basic arithmetic operations"""
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b if b != 0 else "Division by zero not allowed"
    else:
        return "Invalid operator"

print("Calculator Result:", calculator(10, 5, "+"))


# 2️⃣ FIND MAXIMUM OF THREE NUMBERS
def find_max(a, b, c):
    """Returns the largest of three numbers"""
    return max(a, b, c)

print("Max Number:", find_max(10, 25, 15))


# 3️⃣ COUNT VOWELS IN A STRING
def count_vowels(text):
    """Counts number of vowels in the given text"""
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

print("Vowel Count:", count_vowels("Hello World"))


# 4️⃣ PALINDROME CHECKER
def is_palindrome(word):
    """Checks if the given word is a palindrome"""
    return word.lower() == word.lower()[::-1]

print("Is 'madam' a palindrome?", is_palindrome("madam"))


# 5️⃣ FACTORIAL (ITERATIVE APPROACH)
def factorial_iterative(n):
    """Calculates factorial using loop"""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("Factorial of 6:", factorial_iterative(6))


# 6️⃣ FIBONACCI SERIES
def fibonacci(n):
    """Returns first n Fibonacci numbers"""
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq

print("First 10 Fibonacci numbers:", fibonacci(10))


# 7️⃣ CHECK IF A NUMBER IS PRIME
def is_prime(num):
    """Returns True if num is prime"""
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print("Is 29 prime?", is_prime(29))


# 8️⃣ TEMPERATURE CONVERTER
def convert_temperature(value, to_unit):
    """
    Converts temperature between Celsius and Fahrenheit.
    to_unit = 'C' or 'F'
    """
    if to_unit.upper() == "F":
        return (value * 9/5) + 32
    elif to_unit.upper() == "C":
        return (value - 32) * 5/9
    else:
        return "Invalid unit"

print("100°C in Fahrenheit:", convert_temperature(100, "F"))


# 9️⃣ CHECK PASSWORD STRENGTH
def check_password_strength(password):
    """
    Checks password strength based on:
    length >= 8, contains numbers, uppercase and special characters
    """
    has_number = any(ch.isdigit() for ch in password)
    has_upper = any(ch.isupper() for ch in password)
    has_special = any(ch in "!@#$%^&*()" for ch in password)
    if len(password) >= 8 and has_number and has_upper and has_special:
        return "Strong Password ✅"
    else:
        return "Weak Password ❌"

print(check_password_strength("Hello123!"))


# 🔟 GRADE CALCULATOR
def calculate_grade(marks):
    """Returns grade based on marks"""
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "Fail"

print("Grade for 82:", calculate_grade(82))


# 1️⃣1️⃣ AREA CALCULATOR
def area_of_shapes(shape, **kwargs):
    """
    Calculates area of different shapes.
    Example:
        area_of_shapes("circle", radius=5)
        area_of_shapes("rectangle", length=10, width=5)
    """
    if shape == "circle":
        return 3.14 * (kwargs['radius'] ** 2)
    elif shape == "rectangle":
        return kwargs['length'] * kwargs['width']
    elif shape == "triangle":
        return 0.5 * kwargs['base'] * kwargs['height']
    else:
        return "Shape not supported"

print("Area of Circle:", area_of_shapes("circle", radius=5))
print("Area of Rectangle:", area_of_shapes("rectangle", length=10, width=5))


# 1️⃣2️⃣ EMAIL GENERATOR
def generate_email(name, domain="example.com"):
    """Generates email address with optional domain"""
    return f"{name.lower()}@{domain}"

print("Generated Email:", generate_email("Nived", "gmail.com"))


# 1️⃣3️⃣ CALCULATE DISCOUNT
def calculate_discount(price, discount=10):
    """Returns price after discount (default = 10%)"""
    return price - (price * discount / 100)

print("Price after 15% discount:", calculate_discount(1000, 15))


# 1️⃣4️⃣ LIST CLEANER FUNCTION
def clean_list(data):
    """Removes duplicates and sorts the list"""
    return sorted(set(data))

print("Cleaned List:", clean_list([3, 1, 3, 2, 5, 2, 1]))


# 1️⃣5️⃣ WORD COUNTER
def word_count(sentence):
    """Returns a dictionary with word counts"""
    words = sentence.split()
    count_dict = {}
    for word in words:
        count_dict[word] = count_dict.get(word, 0) + 1
    return count_dict

print("Word Count:", word_count("hello world hello python world"))
