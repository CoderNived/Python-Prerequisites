"""
=========================
Matplotlib Detailed Notes
=========================
Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.

------------------------
🔑 Installation:
------------------------
pip install matplotlib

------------------------
📌 Import Syntax:
------------------------
import matplotlib.pyplot as plt

------------------------
🎯 Key Features:
------------------------
- Create 2D plots: line, bar, scatter, histogram, pie
- Customize plots with titles, labels, legends
- Supports multiple plots/subplots
- Used for Data Visualization, EDA, ML model evaluation
"""

import matplotlib.pyplot as plt
import numpy as np

# ===================================
# 1️⃣ Basic Line Plot
# ===================================
x = np.linspace(0, 10, 50)
y = np.sin(x)

plt.figure()
plt.plot(x, y, label="Sine Wave")
plt.title("Basic Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid()
plt.show()

# ===================================
# 2️⃣ Bar Plot
# ===================================
categories = ['A', 'B', 'C', 'D']
values = [10, 24, 36, 18]

plt.figure()
plt.bar(categories, values, color='skyblue')
plt.title("Bar Plot Example")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

# Horizontal Bar Plot
plt.barh(categories, values, color='orange')
plt.title("Horizontal Bar Plot")
plt.show()

# ===================================
# 3️⃣ Scatter Plot
# ===================================
x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y, color='red', alpha=0.7)
plt.title("Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# ===================================
# 4️⃣ Histogram
# ===================================
data = np.random.randn(1000)
plt.hist(data, bins=30, color='purple', edgecolor='black', alpha=0.7)
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# ===================================
# 5️⃣ Pie Chart
# ===================================
sizes = [30, 20, 25, 25]
labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
colors = ['red', 'yellow', 'pink', 'brown']

plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90, shadow=True)
plt.title("Pie Chart Example")
plt.show()

# ===================================
# 6️⃣ Subplots
# ===================================
x = np.linspace(0, 10, 50)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(x, y1, 'b', label="Sine")
plt.legend()
plt.title("Sine Function")

plt.subplot(1, 2, 2)
plt.plot(x, y2, 'r', label="Cosine")
plt.legend()
plt.title("Cosine Function")

plt.tight_layout()
plt.show()

# ===================================
# 7️⃣ Customizing Plot Style
# ===================================
plt.style.use('ggplot')
x = np.linspace(0, 5, 50)
y = np.exp(x)

plt.plot(x, y, marker='o', linestyle='--', color='blue')
plt.title("Styled Plot with ggplot")
plt.show()

# Reset style to default
plt.style.use('default')

# ===================================
# 8️⃣ Saving Figures
# ===================================
plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Saving Figure Example")
plt.savefig("plot_example.png", dpi=300)
plt.close()

# ===================================
# 9️⃣ Practical ML/AI Use Cases
# ===================================

# Example 1: Loss Curve
epochs = np.arange(1, 11)
train_loss = np.random.rand(10)
val_loss = np.random.rand(10)

plt.plot(epochs, train_loss, label='Training Loss')
plt.plot(epochs, val_loss, label='Validation Loss', linestyle='--')
plt.title("Training vs Validation Loss")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.legend()
plt.show()

# Example 2: Confusion Matrix (Heatmap)
import seaborn as sns
import pandas as pd

conf_matrix = np.array([[50, 2], [5, 43]])
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
plt.title("Confusion Matrix Heatmap")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# Example 3: Feature Importance (Bar Plot)
features = ["Feature1", "Feature2", "Feature3", "Feature4"]
importance = [0.25, 0.40, 0.15, 0.20]

plt.bar(features, importance, color='green')
plt.title("Feature Importance")
plt.ylabel("Importance Score")
plt.show()

"""
💡 Key ML/AI Use Cases of Matplotlib:
- Plotting training/validation loss curves
- Visualizing confusion matrices
- Showing feature importances
- Visualizing clusters (scatter plot)
- EDA: histograms, boxplots, distributions
"""
