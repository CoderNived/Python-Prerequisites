# ==========================================
# DICTIONARIES IN PYTHON
# ==========================================

# Creating an Empty Dictionary
empty_dict = {}
print("\nEmpty Dictionary:", empty_dict)
print("Type:", type(empty_dict))

empty_dict = dict()
print("Another Way:", empty_dict)

# Creating a Dictionary with Data
students = {"name": "Nived", "age": 32, "Grade": 88.2}
print("\nStudents Dictionary:", students)
print("Type:", type(students))

# ==========================================
# ACCESSING DICTIONARY ELEMENTS
# ==========================================
print("\n--- Accessing Dictionary Elements ---")
print("Grade:", students["Grade"])  # Direct access
print("Age:", students["age"])

# Using get() method (avoids KeyError if key is missing)
print("Grade using get():", students.get("Grade"))
print("Name using get():", students.get("Name"))  # Returns None (safe)

# ==========================================
# ADDING & UPDATING ELEMENTS
# ==========================================
print("\n--- Adding & Updating ---")
students["city"] = "Mumbai"  # Add new key-value pair
students["age"] = 33         # Update existing key
print("Updated Dictionary:", students)

# ==========================================
# REMOVING ELEMENTS
# ==========================================
print("\n--- Removing Elements ---")
students.pop("city")   # Removes key-value pair by key
print("After pop:", students)

students.popitem()     # Removes last inserted key-value pair
print("After popitem:", students)

del students["age"]    # Deletes a key
print("After del:", students)

students.clear()       # Clears all items
print("After clear:", students)

# ==========================================
# DICTIONARY METHODS
# ==========================================
print("\n--- Dictionary Methods ---")
person = {"name": "Alice", "age": 25, "city": "Delhi"}
print("Keys:", person.keys())
print("Values:", person.values())
print("Items:", person.items())

# Using update() to merge dictionaries
person.update({"age": 30, "country": "India"})
print("After update:", person)

# Copying dictionary (important to avoid reference issues)
person_copy = person.copy()
person["name"] = "Bob"
print("Original:", person)
print("Copy:", person_copy)

# ==========================================
# LOOPING THROUGH DICTIONARIES
# ==========================================
print("\n--- Looping through Dictionary ---")
for key in person:
    print(key, ":", person[key])

for key, value in person.items():
    print(f"{key} -> {value}")

# ==========================================
# DICTIONARY COMPREHENSIONS
# ==========================================
print("\n--- Dictionary Comprehension ---")
squares = {x: x**2 for x in range(5)}
print("Squares Dictionary:", squares)

# Filter with comprehension
even_squares = {k: v for k, v in squares.items() if v % 2 == 0}
print("Even Squares:", even_squares)

# ==========================================
# PRACTICAL EXAMPLES
# ==========================================

print("\n--- Practical Examples ---")

# 1. Storing Student Records
student_records = {
    "John": {"age": 21, "marks": 85},
    "Alice": {"age": 22, "marks": 92},
    "Bob": {"age": 20, "marks": 75},
}
print("Student Records:", student_records)
print("Alice's Marks:", student_records["Alice"]["marks"])

# 2. Counting Word Frequency
sentence = "python is easy and python is fun"
word_counts = {}
for word in sentence.split():
    word_counts[word] = word_counts.get(word, 0) + 1
print("\nWord Frequency:", word_counts)

# 3. Converting Two Lists into a Dictionary
keys = ["name", "age", "city"]
values = ["Charlie", 28, "Bangalore"]
person = dict(zip(keys, values))
print("\nDictionary from Lists:", person)

# 4. Searching in a Dictionary
if "age" in person:
    print("Age Found:", person["age"])

# 5. Using Dictionary for a Simple Phonebook
phonebook = {
    "Alice": "9876543210",
    "Bob": "9123456789",
    "Charlie": "9988776655"
}
name = "Bob"
print(f"\n{name}'s Number:", phonebook.get(name, "Not Found"))

# 6. Grouping Data by Category
employees = [
    {"name": "Raj", "dept": "IT"},
    {"name": "Neha", "dept": "HR"},
    {"name": "Karan", "dept": "IT"},
    {"name": "Pooja", "dept": "Finance"},
]
grouped = {}
for emp in employees:
    dept = emp["dept"]
    grouped.setdefault(dept, []).append(emp["name"])
print("\nGrouped Employees:", grouped)

# 7. Sorting Dictionary by Values
scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
sorted_scores = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))
print("\nSorted Scores (Descending):", sorted_scores)

# 8. Merging Multiple Dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = {**dict1, **dict2}  # dict2 overrides dict1
print("\nMerged Dictionary:", merged)

# 9. Default Values with fromkeys()
default_dict = dict.fromkeys(["a", "b", "c"], 0)
print("\nDictionary with Default Values:", default_dict)

# 10. Creating Nested Dictionaries Dynamically
nested = {}
for i in range(1, 4):
    nested[i] = {"square": i**2, "cube": i**3}
print("\nNested Dictionary:", nested)
