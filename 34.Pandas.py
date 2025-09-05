import pandas as pd
"""
=========================
Pandas Detailed Notes
=========================
Pandas is a fast, powerful, flexible open-source data analysis and manipulation library.
It is built on top of NumPy and is widely used in Data Science, ML, and AI.

------------------------
🔑 Installation:
------------------------
pip install pandas

------------------------
📌 Import Syntax:
------------------------
import pandas as pd

------------------------
🎯 Key Features:
------------------------
- Two main data structures: Series (1D) and DataFrame (2D)
- Easy reading/writing of CSV, Excel, JSON, SQL, etc.
- Powerful indexing, filtering, groupby operations
- Missing data handling
- Widely used for data cleaning, preprocessing, and analysis
"""

import pandas as pd
import numpy as np

# ===================================
# 1️⃣ Creating Series (1D Data)
# ===================================
print("\n=== Creating Series ===")
s1 = pd.Series([10, 20, 30, 40, 50])
print(s1)

# Custom index
s2 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print("\nSeries with custom index:\n", s2)

# From dictionary
data_dict = {"math": 80, "science": 90, "english": 85}
s3 = pd.Series(data_dict)
print("\nSeries from dictionary:\n", s3)

# ===================================
# 2️⃣ Creating DataFrames (2D Data)
# ===================================
print("\n=== Creating DataFrame ===")
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [24, 27, 22, 32],
    "City": ["New York", "London", "Paris", "Tokyo"]
}
df = pd.DataFrame(data)
print(df)

# ===================================
# 3️⃣ Reading & Writing Data
# ===================================
# CSV, Excel, JSON (For demonstration - not actually writing to disk here)
# df.to_csv("people.csv", index=False)
# df_read = pd.read_csv("people.csv")

# ===================================
# 4️⃣ Inspecting Data
# ===================================
print("\nHead:\n", df.head())
print("\nTail:\n", df.tail())
print("\nInfo:\n")
print(df.info())
print("\nDescribe:\n", df.describe())

# ===================================
# 5️⃣ Selecting & Indexing
# ===================================
print("\nSingle column:\n", df["Name"])
print("\nMultiple columns:\n", df[["Name", "City"]])

print("\nRow selection with loc:\n", df.loc[1])  # By label
print("\nRow selection with iloc:\n", df.iloc[2])  # By position

# ===================================
# 6️⃣ Filtering Data
# ===================================
print("\nFilter Age > 25:\n", df[df["Age"] > 25])
print("\nFilter City == 'London':\n", df[df["City"] == "London"])

# ===================================
# 7️⃣ Adding / Modifying Columns
# ===================================
df["Salary"] = [50000, 60000, 45000, 70000]
df["Age+5"] = df["Age"] + 5
print("\nDataFrame with new columns:\n", df)

# ===================================
# 8️⃣ Handling Missing Data
# ===================================
df2 = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", None],
    "Age": [24, None, 22, 32],
    "City": ["New York", "London", None, "Tokyo"]
})
print("\nDataFrame with missing values:\n", df2)

print("\nDrop missing rows:\n", df2.dropna())
print("\nFill missing values:\n", df2.fillna({"Name": "Unknown", "Age": df2["Age"].mean(), "City": "Unknown"}))

# ===================================
# 9️⃣ GroupBy & Aggregations
# ===================================
df_group = pd.DataFrame({
    "Department": ["HR", "IT", "IT", "HR", "Finance"],
    "Employee": ["A", "B", "C", "D", "E"],
    "Salary": [40000, 50000, 55000, 42000, 60000]
})

print("\nGroup by Department:\n", df_group.groupby("Department")["Salary"].mean())

# Multiple aggregations
print("\nGroup by with multiple aggregations:\n", df_group.groupby("Department")["Salary"].agg(["mean", "max", "min"]))

# ===================================
# 🔟 Merging & Joining
# ===================================
dept = pd.DataFrame({"EmpID": [1, 2, 3], "Department": ["HR", "IT", "Finance"]})
salary = pd.DataFrame({"EmpID": [1, 2, 3], "Salary": [40000, 50000, 60000]})

merged = pd.merge(dept, salary, on="EmpID")
print("\nMerged DataFrame:\n", merged)

# ===================================
# 1️⃣1️⃣ Sorting
# ===================================
print("\nSorted by Salary:\n", df.sort_values(by="Salary", ascending=False))

# ===================================
# 1️⃣2️⃣ Descriptive Statistics
# ===================================
print("\nMean Age:", df["Age"].mean())
print("Median Age:", df["Age"].median())
print("Standard Deviation:", df["Age"].std())

# ===================================
# 1️⃣3️⃣ Practical ML/AI Use Cases
# ===================================

# Example 1: Handling Dataset for ML
dataset = pd.DataFrame({
    "Feature1": [1, 2, np.nan, 4, 5],
    "Feature2": ["A", "B", "B", np.nan, "A"],
    "Target": [0, 1, 1, 0, 1]
})
print("\nRaw Dataset:\n", dataset)

# Handle Missing Values
dataset["Feature1"].fillna(dataset["Feature1"].mean(), inplace=True)
dataset["Feature2"].fillna(dataset["Feature2"].mode()[0], inplace=True)
print("\nAfter Filling Missing Values:\n", dataset)

# One-Hot Encoding (for ML)
dataset_encoded = pd.get_dummies(dataset, columns=["Feature2"])
print("\nOne-Hot Encoded Dataset:\n", dataset_encoded)

# Feature Scaling
dataset_encoded["Feature1_scaled"] = (dataset_encoded["Feature1"] - dataset_encoded["Feature1"].mean()) / dataset_encoded["Feature1"].std()
print("\nScaled Dataset:\n", dataset_encoded)

"""
💡 Key ML/AI Use Cases of Pandas:
- Loading datasets (CSV, Excel, SQL)
- Cleaning & Preprocessing (handling NaN, duplicates)
- Feature Engineering (One-Hot Encoding, Binning)
- Exploratory Data Analysis (EDA)
- Input preparation for Scikit-learn, TensorFlow, PyTorch
"""
