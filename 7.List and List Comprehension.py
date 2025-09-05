# ==========================================
# LIST BASICS
# ==========================================
print("\n--- Creating Lists ---")
lst = []
print(type(lst))  # <class 'list'>

name = ["Krish", "Jack", "Jacob", 1, 2, 3, 4]  # lists can have mixed data
print(name)

crazy = [1, True, "Krish", 3.15]  # lists can store different data types
print(crazy)

# ==========================================
# ACCESSING LIST ELEMENTS
# ==========================================
print("\n--- Accessing List Elements ---")
fruits = ["apple", "banana", "guava", "cherry", "pineapple"]
print(fruits[2])   # 'guava'
print(fruits[-1])  # 'pineapple'
print(fruits[0])   # 'apple'
print(fruits[4])   # 'pineapple'

print(fruits[1:])   # from index 1 till end
print(fruits[1:3])  # from index 1 to 2
print(fruits[-3:-1])  # using negative indexes (guava, cherry)

# ==========================================
# MODIFYING LIST ELEMENTS
# ==========================================
print("\n--- Modifying List Elements ---")
fruits[1] = "Watermelon"
print(fruits)

# ==========================================
# LIST METHODS
# ==========================================
print("\n--- List Methods ---")
fruits.append("orange")  # add element at end
print(fruits)

fruits.insert(1, "banana")  # insert at position
print(fruits)

fruits.remove("banana")  # removes first occurrence
print(fruits)

# Remove and return last element
popped_fruit = fruits.pop()
print("Popped:", popped_fruit)
print(fruits)

# Indexing
index = fruits.index("cherry")
print("Index of cherry:", index)

# Count occurrences
count_apple = fruits.count("apple")
print("Count of apple:", count_apple)

# Sorting
fruits.sort()
print("Sorted:", fruits)

# Reversing
fruits.reverse()
print("Reversed:", fruits)

# Clearing
fruits.clear()
print("Cleared list:", fruits)

# ==========================================
# SLICING LISTS
# ==========================================
print("\n--- Slicing Lists ---")
numbers = list(range(1, 19))
print(numbers[2:5])   # slice from index 2 to 4
print(numbers[:5])    # slice from start to 4
print(numbers[2:])    # slice from index 2 to end
print(numbers[::5])   # take every 5th element
print(numbers[::-1])  # reverse list

# ==========================================
# ITERATION
# ==========================================
print("\n--- Iteration over List ---")
for number in numbers:
    print(number, end=" ")
print()

print("\nIteration with Index:")
for index, number in enumerate(numbers):
    print(index, number)

# ==========================================
# LIST COMPREHENSIONS
# ==========================================
print("\n--- List Comprehension ---")
lst = [x**2 for x in range(10)]
print("Squares:", lst)

# With Condition
even_num = [num for num in range(20) if num % 2 == 0]
print("Even Numbers:", even_num)

# Nested List Comprehension
lst1 = [1, 2, 3, 4]
lst2 = ['a', 'b', 'c', 'd']
pairs = [[i, j] for i in lst1 for j in lst2]
print("Pairs:", pairs)

# With Function Calls
words = ["hello", "python", "world", "", "code"]
lengths = [len(word) for word in words]
print("Lengths:", lengths)

# ==========================================
# MORE PRACTICAL LIST EXAMPLES
# ==========================================

# 1. Filtering with List Comprehension
print("\nFilter words with length > 4:")
long_words = [word for word in words if len(word) > 4]
print(long_words)

# 2. Converting Strings to Uppercase
print("\nConvert to Uppercase:")
upper_words = [word.upper() for word in words if word]
print(upper_words)

# 3. Removing Duplicates
print("\nRemoving Duplicates:")
nums = [1, 2, 3, 2, 4, 1, 5]
unique_nums = list(set(nums))  # convert to set and back
print(unique_nums)

# 4. Flattening a Nested List
print("\nFlatten a Nested List:")
nested = [[1, 2], [3, 4], [5, 6]]
flat = [item for sublist in nested for item in sublist]
print(flat)

# 5. Sorting by Length
print("\nSort words by length:")
words = ["python", "is", "fun", "amazing", "AI"]
words.sort(key=len)
print(words)

# 6. Find Min and Max
print("\nFind Min and Max:")
print("Min:", min(numbers))
print("Max:", max(numbers))

# 7. Sum of Elements
print("\nSum of Elements:")
print("Sum:", sum(numbers))

# 8. List Copy vs Reference
print("\nCopy vs Reference:")
original = [1, 2, 3]
copy_list = original.copy()  # actual copy
ref_list = original          # reference to same list
original.append(4)
print("Original:", original)
print("Copy:", copy_list)
print("Reference:", ref_list)

# 9. Zipping Two Lists Together
print("\nZip Two Lists:")
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]
zipped = list(zip(names, scores))
print(zipped)

# 10. Using map() with Lists
print("\nUsing map() to Square Numbers:")
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, nums))
print(squares)

# 11. Using any() and all()
print("\nCheck Conditions with any() and all():")
nums = [2, 4, 6, 8]
print("All even?", all(x % 2 == 0 for x in nums))
print("Any greater than 5?", any(x > 5 for x in nums))


