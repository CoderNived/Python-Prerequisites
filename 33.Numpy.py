"""
=========================
NumPy Detailed Notes
=========================
NumPy (Numerical Python) is a fundamental library for numerical and scientific computing.
It provides powerful n-dimensional arrays, mathematical functions, and tools for data analysis.

------------------------
🔑 Installation:
------------------------
pip install numpy

------------------------
📌 Import Syntax:
------------------------
import numpy as np

------------------------
🎯 Key Features:
------------------------
- Fast, memory-efficient multi-dimensional arrays
- Mathematical operations on entire arrays (vectorization)
- Broadcasting support
- Linear algebra, Fourier transform, random number generation
- Used in ML, AI, Data Science, Scientific Computing
"""

import numpy as np

# ===================================
# 1️⃣ Creating Arrays
# ===================================

# From Python list
arr1 = np.array([1, 2, 3])
print("Array from list:", arr1)

# Multi-dimensional array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:\n", arr2)

# Special arrays
zeros = np.zeros((3, 3))       # 3x3 matrix filled with zeros
ones = np.ones((2, 4))         # 2x4 matrix filled with ones
identity = np.eye(3)           # Identity matrix
range_array = np.arange(0, 10, 2)  # Start=0, Stop=10, Step=2
linspace_array = np.linspace(0, 1, 5) # 5 values between 0 & 1

print("\nZeros:\n", zeros)
print("\nIdentity:\n", identity)
print("\nRange Array:", range_array)
print("\nLinspace Array:", linspace_array)

# ===================================
# 2️⃣ Array Attributes
# ===================================
print("\nShape:", arr2.shape)
print("Dimensions:", arr2.ndim)
print("Size:", arr2.size)
print("Data Type:", arr2.dtype)
print("Item Size (bytes):", arr2.itemsize)

# ===================================
# 3️⃣ Reshaping and Flattening
# ===================================
reshaped = np.arange(12).reshape(3, 4)
print("\nReshaped 3x4:\n", reshaped)

flattened = reshaped.flatten()
print("\nFlattened Array:", flattened)

# ===================================
# 4️⃣ Vectorized Operations
# ===================================
a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

print("\nAddition:", a + b)
print("Subtraction:", b - a)
print("Multiplication:", a * b)
print("Division:", b / a)

# Broadcasting Example
print("\nBroadcasting Example:\n", a + 5)

# ===================================
# 5️⃣ Universal Functions (ufuncs)
# ===================================
print("\nSquare Root:", np.sqrt(a))
print("Exponential:", np.exp(a))
print("Sine:", np.sin(a))
print("Log:", np.log(a))

# ===================================
# 6️⃣ Indexing & Slicing
# ===================================
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print("\nElement at (0,0):", matrix[0, 0])
print("Second Row:", matrix[1])
print("Last Column:", matrix[:, 2])
print("Submatrix:\n", matrix[0:2, 1:])

# Modify elements
matrix[0, 0] = 100
matrix[:, 1] = 200
print("\nModified Matrix:\n", matrix)

# ===================================
# 7️⃣ Statistical Functions
# ===================================
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
mean = np.mean(data)
median = np.median(data)
std_dev = np.std(data)
variance = np.var(data)

print("\nMean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)
print("Variance:", variance)

# Normalize data
normalized_data = (data - mean) / std_dev
print("\nNormalized Data:", normalized_data)

# Logical Operations
print("\nElements > 5:", data[data > 5])
print("Elements between 3 and 7:", data[(data >= 3) & (data <= 7)])

# ===================================
# 8️⃣ Random Module (Important for ML)
# ===================================
random_arr = np.random.rand(3, 3)      # Random floats [0, 1)
randn_arr = np.random.randn(3, 3)      # Normally distributed random numbers
randint_arr = np.random.randint(1, 10, size=(3, 3)) # Random integers

print("\nRandom Array:\n", random_arr)
print("\nNormal Distribution Array:\n", randn_arr)
print("\nRandom Integers:\n", randint_arr)

# ===================================
# 9️⃣ Practical Use Cases in ML/AI
# ===================================

# Example 1: Feature Scaling
features = np.array([10, 20, 30, 40, 50])
scaled = (features - np.min(features)) / (np.max(features) - np.min(features))
print("\nMin-Max Scaled Features:", scaled)

# Example 2: Mean Squared Error (MSE)
y_true = np.array([3.0, -0.5, 2.0, 7.0])
y_pred = np.array([2.5, 0.0, 2.1, 7.8])
mse = np.mean((y_true - y_pred) ** 2)
print("\nMean Squared Error:", mse)

# Example 3: Creating Dummy Dataset for ML
X = np.random.rand(100, 3)  # 100 samples, 3 features
y = (X[:, 0] + X[:, 1] * 0.5 > 0.7).astype(int)  # Binary classification labels
print("\nDummy Features Shape:", X.shape)
print("Dummy Labels Shape:", y.shape)
print("First 5 Labels:", y[:5])

"""
💡 Key ML/AI Use Cases of NumPy:
- Data Preprocessing (Scaling, Normalization)
- Vectorized Cost Functions & Gradients
- Handling Datasets Efficiently
- Generating Random Numbers for Model Initialization
- Used internally by Pandas, TensorFlow, Scikit-learn
"""

