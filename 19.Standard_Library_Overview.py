"""
===========================================================
📌 PYTHON STANDARD LIBRARY – COMPLETE NOTES
===========================================================

The Python Standard Library is a collection of modules and packages
that are included with every Python installation. It provides ready-to-use
functions and classes for tasks like math, date/time manipulation,
file I/O, networking, concurrency, data persistence, and more.

This makes Python "batteries-included" 🪫🔋 — you can do a lot without installing anything extra.

-----------------------------------------------------------
📌 SYNTAX TO IMPORT MODULES
-----------------------------------------------------------

import module_name
import module_name as alias
from module_name import function_name
from module_name import *  # Not recommended (pollutes namespace)

Example:
import math
print(math.sqrt(16))

from math import sqrt
print(sqrt(16))

"""

# ===========================================================
# 1️⃣ MATH MODULE – MATHEMATICAL OPERATIONS
# ===========================================================
import math

print("📌 Math Module Examples:")
print("Square root:", math.sqrt(25))
print("Ceil:", math.ceil(3.4))
print("Floor:", math.floor(3.4))
print("Factorial:", math.factorial(5))
print("Power:", math.pow(2, 3))
print("Pi constant:", math.pi)

print("-" * 60)

# ===========================================================
# 2️⃣ DATETIME MODULE – DATE AND TIME
# ===========================================================
import datetime

print("📌 Datetime Module Examples:")
today = datetime.date.today()
print("Today's date:", today)
print("Current year:", today.year)
print("Current month:", today.month)
print("Current weekday:", today.weekday())

now = datetime.datetime.now()
print("Current datetime:", now)
future = now + datetime.timedelta(days=10)
print("10 days from now:", future)

print("-" * 60)

# ===========================================================
# 3️⃣ CALENDAR MODULE – WORKING WITH CALENDARS
# ===========================================================
import calendar

print("📌 Calendar Module Examples:")
print(calendar.month(2025, 9))
print("Is 2024 a leap year?", calendar.isleap(2024))
print("Week header:", calendar.weekheader(3))

print("-" * 60)

# ===========================================================
# 4️⃣ RANDOM MODULE – GENERATE RANDOM NUMBERS
# ===========================================================
import random

print("📌 Random Module Examples:")
print("Random number [0,1):", random.random())
print("Random integer [1,10]:", random.randint(1, 10))
print("Random choice from list:", random.choice(['apple', 'banana', 'cherry']))
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print("Shuffled list:", my_list)
print("Random sample:", random.sample(my_list, 3))

print("-" * 60)

# ===========================================================
# 5️⃣ STATISTICS MODULE – BASIC STATS
# ===========================================================
import statistics

data = [10, 20, 30, 40, 50]
print("📌 Statistics Module Examples:")
print("Mean:", statistics.mean(data))
print("Median:", statistics.median(data))
print("Variance:", statistics.variance(data))

print("-" * 60)

# ===========================================================
# 6️⃣ OS MODULE – INTERACT WITH OPERATING SYSTEM
# ===========================================================
import os

print("📌 OS Module Examples:")
print("Current working directory:", os.getcwd())
print("List of files:", os.listdir('.'))
print("Environment variables:", os.environ.get('USERNAME'))

print("-" * 60)

# ===========================================================
# 7️⃣ SYS MODULE – SYSTEM SPECIFIC PARAMETERS
# ===========================================================
import sys

print("📌 Sys Module Examples:")
print("Python Version:", sys.version)
print("Command Line Arguments:", sys.argv)
print("Platform:", sys.platform)

print("-" * 60)

# ===========================================================
# 8️⃣ JSON MODULE – WORKING WITH JSON DATA
# ===========================================================
import json

person = {"name": "Alice", "age": 25, "city": "Paris"}
print("📌 JSON Module Examples:")
json_data = json.dumps(person)
print("Dictionary -> JSON string:", json_data)
dict_data = json.loads(json_data)
print("JSON string -> Dictionary:", dict_data)

print("-" * 60)

# ===========================================================
# 9️⃣ COLLECTIONS MODULE – SPECIALIZED DATA STRUCTURES
# ===========================================================
from collections import Counter, namedtuple, defaultdict

print("📌 Collections Module Examples:")
# Counter
print("Counter:", Counter(['a', 'b', 'a', 'c', 'b', 'a']))

# NamedTuple
Point = namedtuple('Point', ['x', 'y'])
pt = Point(10, 20)
print("NamedTuple:", pt, pt.x, pt.y)

# DefaultDict
d = defaultdict(int)
d['a'] += 1
print("DefaultDict:", dict(d))

print("-" * 60)

# ===========================================================
# 🔟 TIME MODULE – TIME HANDLING
# ===========================================================
import time

print("📌 Time Module Examples:")
print("Current timestamp:", time.time())
print("Local time:", time.ctime())
print("Sleeping for 1 second...")
time.sleep(1)
print("Awake now!")

print("-" * 60)

# ===========================================================
# 1️⃣1️⃣ RE MODULE – REGULAR EXPRESSIONS
# ===========================================================
import re

print("📌 Re Module Examples:")
text = "Contact: test@example.com"
pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
match = re.search(pattern, text)
if match:
    print("Email found:", match.group())

print("-" * 60)

# ===========================================================
# 1️⃣2️⃣ CSV MODULE – WORKING WITH CSV FILES
# ===========================================================
import csv

print("📌 CSV Module Examples:")
with open("sample.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Alice", 25])
    writer.writerow(["Bob", 30])

with open("sample.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

print("-" * 60)

"""
===========================================================
📌 USE CASES OF STANDARD LIBRARY
===========================================================
✅ Data Analysis (json, csv, statistics)
✅ System Utilities (os, sys, shutil)
✅ Web Scraping (re, urllib)
✅ Automation Scripts (os, time, datetime)
✅ AI/ML Preprocessing (random, math, itertools)
✅ File Management & Logging (logging, pathlib, csv)
===========================================================
"""
