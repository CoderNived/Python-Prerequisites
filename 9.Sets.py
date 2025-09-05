# ==========================================
# SETS IN PYTHON
# ==========================================

# Creating a Set
my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print("\nSet Example:", my_set)
print("Type:", type(my_set))

# Creating an Empty Set
my_empty_set = set()
print("\nEmpty Set Type:", type(my_empty_set))

# Creating a Set from a List
my_set = set([1, 2, 3, 4, 5, 6, 7])
print("\nSet from List:", my_set)

# ==========================================
# BASIC SET OPERATIONS
# ==========================================
print("\n--- Basic Set Operations ---")
my_set.add(12)  # Adds an element
print("After Adding 12:", my_set)

my_set.remove(3)  # Removes element (throws error if element not present)
print("After Removing 3:", my_set)

my_set.discard(11)  # Removes element (no error if element not present)
print("After Discarding 11 (No Error):", my_set)

popped_value = my_set.pop()  # Removes a random element
print("Popped Element:", popped_value)
print("Set After Pop:", my_set)

my_set.clear()  # Clears all elements
print("After Clearing:", my_set)

# ==========================================
# MATHEMATICAL SET OPERATIONS
# ==========================================
print("\n--- Mathematical Set Operations ---")
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Union
print("Union:", set_a | set_b)
print("Union using method:", set_a.union(set_b))

# Intersection
print("Intersection:", set_a & set_b)
print("Intersection using method:", set_a.intersection(set_b))

# Difference
print("Difference (A - B):", set_a - set_b)
print("Difference using method:", set_a.difference(set_b))

# Symmetric Difference (Elements in A or B but not both)
print("Symmetric Difference:", set_a ^ set_b)
print("Symmetric Difference using method:", set_a.symmetric_difference(set_b))

# ==========================================
# SET MEMBERSHIP & RELATIONSHIP CHECKS
# ==========================================
print("\n--- Membership & Relationship Checks ---")
print("Is 3 in set_a?", 3 in set_a)
print("Is 10 not in set_b?", 10 not in set_b)

set_c = {1, 2}
set_d = {1, 2, 3, 4}
print("Is set_c a subset of set_d?", set_c.issubset(set_d))
print("Is set_d a superset of set_c?", set_d.issuperset(set_c))
print("Are set_a and set_b disjoint?", set_a.isdisjoint(set_b))

# ==========================================
# SET COMPREHENSIONS
# ==========================================
print("\n--- Set Comprehensions ---")
squared_set = {x**2 for x in range(1, 6)}
print("Squared Numbers Set:", squared_set)

even_set = {x for x in range(1, 11) if x % 2 == 0}
print("Even Numbers Set:", even_set)

# ==========================================
# PRACTICAL EXAMPLES
# ==========================================

print("\n--- Practical Examples ---")

# 1. Removing Duplicates from a List
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print("Unique Numbers from List:", unique_numbers)

# 2. Finding Common Elements in Two Lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = set(list1) & set(list2)
print("Common Elements:", common)

# 3. Finding Unique Words in a Sentence
sentence = "python is easy and python is powerful"
words = set(sentence.split())
print("Unique Words:", words)

# 4. Detecting Duplicate Emails
emails = ["a@gmail.com", "b@gmail.com", "a@gmail.com", "c@gmail.com"]
if len(emails) != len(set(emails)):
    print("Duplicate Emails Found!")

# 5. Fast Membership Test (Faster than List)
large_set = set(range(1, 100000))
print("Is 99999 in large_set?", 99999 in large_set)

# 6. Set Operations in Real Life (Students Example)
cricket_players = {"Alice", "Bob", "Charlie", "David"}
football_players = {"Bob", "David", "Eve", "Frank"}

print("\nStudents who play both Cricket & Football:",
      cricket_players & football_players)
print("Students who play only Cricket:",
      cricket_players - football_players)
print("Students who play either Cricket or Football:",
      cricket_players | football_players)

# 7. Creating a Frozen Set (Immutable Set)
frozen = frozenset([1, 2, 3, 4])
print("\nFrozen Set:", frozen)

# frozen.add(5)  # This will throw an error (frozen set cannot be changed)

# 8. Set Filtering with Comprehension
random_numbers = {5, 10, 15, 20, 25}
greater_than_12 = {x for x in random_numbers if x > 12}
print("Numbers > 12:", greater_than_12)
