# ==========================================
# PRACTICAL LIST EXAMPLES & REAL-WORLD USE CASES
# ==========================================

print("\n--- Practical Examples with Lists ---")

# 1. Storing Student Names & Printing Them
students = ["Alice", "Bob", "Charlie", "David"]
print("Class Students:", students)
for student in students:
    print("Welcome", student)

# 2. Calculating Average Marks
marks = [85, 90, 78, 92, 88]
average = sum(marks) / len(marks)
print("\nAverage Marks:", average)

# 3. Finding Highest & Lowest Marks
print("Highest Mark:", max(marks))
print("Lowest Mark:", min(marks))

# 4. Filtering Passing Students
passing_marks = [mark for mark in marks if mark >= 40]
print("\nStudents who passed:", passing_marks)

# 5. Creating a Shopping Cart
shopping_cart = []
shopping_cart.append("Milk")
shopping_cart.append("Bread")
shopping_cart.append("Eggs")
print("\nShopping Cart:", shopping_cart)

shopping_cart.remove("Bread")  # removing an item
print("Updated Cart:", shopping_cart)

# 6. Counting Occurrences (Real-world: Votes, Likes)
votes = ["Yes", "No", "Yes", "Yes", "No", "Yes"]
yes_count = votes.count("Yes")
no_count = votes.count("No")
print("\nVotes Count: Yes =", yes_count, ", No =", no_count)

# 7. Working with Sensor Readings (IoT Example)
temperatures = [30.5, 32.0, 31.2, 33.8, 29.5, 35.0]
print("\nMaximum Temperature:", max(temperatures))
print("Minimum Temperature:", min(temperatures))

# Find all temperatures above 32 (high temperature alert)
high_temps = [t for t in temperatures if t > 32]
print("High Temperatures:", high_temps)

# 8. Removing Duplicates from a List (Useful in Data Cleaning)
emails = ["a@gmail.com", "b@gmail.com", "a@gmail.com", "c@gmail.com"]
unique_emails = list(set(emails))
print("\nUnique Emails:", unique_emails)

# 9. Sorting Names Alphabetically
names = ["Steve", "Alice", "Bob", "Eve"]
names.sort()
print("\nSorted Names:", names)

# 10. Joining Lists (Merging Data)
list1 = ["Apples", "Bananas"]
list2 = ["Mangoes", "Oranges"]
fruits = list1 + list2
print("\nCombined Fruits List:", fruits)

# 11. Simple To-Do List (Mini Project)
todo_list = []
todo_list.append("Study Python")
todo_list.append("Complete Assignment")
todo_list.append("Go to Gym")
print("\nToday's Tasks:", todo_list)

done_task = todo_list.pop(0)  # mark first task as done
print("Completed Task:", done_task)
print("Remaining Tasks:", todo_list)

# 12. Extracting Even & Odd Numbers from a List
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = [n for n in numbers if n % 2 == 0]
odd = [n for n in numbers if n % 2 != 0]
print("\nEven Numbers:", even)
print("Odd Numbers:", odd)

# 13. Simple Search in a List
cities = ["Mumbai", "Delhi", "Bangalore", "Chennai"]
search = "Delhi"
if search in cities:
    print("\n", search, "found in list!")
else:
    print(search, "not found in list!")

# 14. Splitting a Sentence into Words (Useful for NLP)
sentence = "Python is a powerful language"
words = sentence.split()  # convert string to list of words
print("\nWords in sentence:", words)

# 15. Finding Duplicates in a List
nums = [1, 2, 3, 2, 4, 5, 1, 6]
duplicates = [n for n in set(nums) if nums.count(n) > 1]
print("\nDuplicates in List:", duplicates)

# 16. Flattening a Nested List (Useful in Data Processing)
nested_list = [[1, 2], [3, 4], [5, 6]]
flattened = [item for sublist in nested_list for item in sublist]
print("\nFlattened List:", flattened)

# 17. Parallel Iteration (Using zip)
products = ["Laptop", "Phone", "Tablet"]
prices = [50000, 20000, 15000]
for product, price in zip(products, prices):
    print(f"{product} costs ₹{price}")

# 18. Rotating a List (Useful for Shifting Data)
numbers = [1, 2, 3, 4, 5]
k = 2  # rotate by 2 positions
rotated = numbers[k:] + numbers[:k]
print("\nRotated List:", rotated)

# 19. Using any() and all() to Check Conditions
ages = [18, 21, 25, 17, 30]
print("\nAll adults?", all(age >= 18 for age in ages))
print("Any minor?", any(age < 18 for age in ages))

# 20. Building a Matrix (List of Lists)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("\nMatrix:")
for row in matrix:
    print(row)

# Accessing matrix elements
print("Element at row 1, col 2:", matrix[0][1])
