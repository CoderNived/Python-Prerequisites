"""
====================================================================
📌 DATA MANIPULATION USING NUMPY, PANDAS, AND MATPLOTLIB – COMPLETE NOTES
====================================================================

This file covers:
1. NumPy (Data Creation, Indexing, Math, Statistics, Broadcasting)
2. Pandas (Series, DataFrames, Cleaning, Filtering, Grouping)
3. Matplotlib (Data Visualization – Line, Bar, Histogram, Scatter)

Each section has:
✅ Concept explanation
✅ Syntax
✅ Practical examples
✅ Real-world data manipulation use cases
====================================================================
"""

# ================================================================
# 1️⃣ NUMPY – Numerical Python
# ================================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("========== NUMPY ==========")

# --- Creating Arrays ---
arr1 = np.array([1, 2, 3, 4, 5])
print("\nArray:", arr1)
print("Shape:", arr1.shape)
print("Data Type:", arr1.dtype)

# Creating 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:\n", arr2)
print("Shape:", arr2.shape)

# Special arrays
print("\nZeros Array:\n", np.zeros((3, 3)))
print("Ones Array:\n", np.ones((2, 4)))
print("Identity Matrix:\n", np.eye(3))
print("Range Array:\n", np.arange(0, 10, 2))

# --- Array Reshaping & Indexing ---
reshaped = np.arange(12).reshape(3, 4)
print("\nReshaped Array:\n", reshaped)
print("Element at [1, 2]:", reshaped[1, 2])
print("Slice first row:", reshaped[0, :])
print("Last column:", reshaped[:, -1])

# --- Vectorized Operations ---
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])
print("\nAddition:", a + b)
print("Multiplication:", a * b)
print("Square Root:", np.sqrt(b))
print("Exponent:", np.exp(a))

# --- Broadcasting ---
matrix = np.ones((3, 3))
vector = np.array([1, 2, 3])
print("\nBroadcasted Addition:\n", matrix + vector)

# --- Statistical Functions ---
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print("\nMean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))
print("Variance:", np.var(data))

# --- Logical Indexing ---
print("\nElements > 5:", data[data > 5])
print("Even Numbers:", data[data % 2 == 0])

# ================================================================
# 2️⃣ PANDAS – Data Analysis Library
# ================================================================
print("\n========== PANDAS ==========")

# --- Creating Series ---
series = pd.Series([10, 20, 30, 40], index=['A', 'B', 'C', 'D'])
print("\nPandas Series:\n", series)
print("Access Element by Label:", series['B'])
print("Statistical Summary:\n", series.describe())

# --- Creating DataFrame ---
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 75000, 90000]
}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)

# --- DataFrame Operations ---
print("\nColumn Access:\n", df['Name'])
print("\nRow Access using loc:\n", df.loc[1])
print("\nRow Access using iloc:\n", df.iloc[2])
print("\nFilter (Age > 30):\n", df[df['Age'] > 30])

# Adding new column
df['Bonus'] = df['Salary'] * 0.10
print("\nDataFrame with Bonus Column:\n", df)

# --- GroupBy Example ---
grouped = df.groupby('Age')['Salary'].mean()
print("\nGrouped by Age (Salary Mean):\n", grouped)

# --- Handling Missing Values ---
df_missing = pd.DataFrame({'A': [1, np.nan, 3], 'B': [4, 5, np.nan]})
print("\nDataFrame with Missing Values:\n", df_missing)
print("Filled Missing Values:\n", df_missing.fillna(0))
print("Dropped Rows with NaN:\n", df_missing.dropna())

# --- Sorting ---
print("\nSorted by Salary:\n", df.sort_values(by='Salary', ascending=False))

# ================================================================
# 3️⃣ MATPLOTLIB – Data Visualization
# ================================================================
print("\n========== MATPLOTLIB ==========")

# --- Line Plot ---
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.figure(figsize=(6, 4))
plt.plot(x, y, label="sin(x)")
plt.title("Line Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid()
plt.show()

# --- Bar Chart ---
plt.figure(figsize=(6, 4))
plt.bar(df['Name'], df['Salary'], color='skyblue')
plt.title("Employee Salaries")
plt.xlabel("Name")
plt.ylabel("Salary")
plt.show()

# --- Histogram ---
plt.figure(figsize=(6, 4))
plt.hist(np.random.randn(1000), bins=30, color='purple', alpha=0.7)
plt.title("Histogram Example")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# --- Scatter Plot ---
x = np.random.rand(50)
y = np.random.rand(50)
plt.figure(figsize=(6, 4))
plt.scatter(x, y, color='red')
plt.title("Scatter Plot Example")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

"""
====================================================================
📌 SUMMARY
====================================================================
✅ NumPy → Numerical computation, fast array manipulation, broadcasting  
✅ Pandas → Tabular data handling, filtering, grouping, missing data handling  
✅ Matplotlib → Data visualization (line, bar, scatter, histogram)

📌 Real-World Use Case:
1. Load dataset using Pandas
2. Clean / filter / group data
3. Perform numerical operations using NumPy
4. Visualize results using Matplotlib

====================================================================
"""
