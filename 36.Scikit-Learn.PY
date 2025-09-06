"""
===============================
📌 SCIKIT-LEARN COMPLETE NOTES
===============================

Scikit-learn is a machine learning library in Python that provides:
- Simple and efficient tools for data mining and analysis
- Built on NumPy, SciPy, and Matplotlib
- Focused on machine learning algorithms (classification, regression, clustering)

📦 INSTALLATION:
----------------
pip install scikit-learn

IMPORTING:
----------
import sklearn
from sklearn import datasets, model_selection, metrics, preprocessing

"""

# ===================================================
# 1️⃣ BASIC WORKFLOW
# ===================================================
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split data (train 80%, test 20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))

# ===================================================
# 2️⃣ CLASSIFICATION EXAMPLE (KNN)
# ===================================================
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
knn_pred = knn.predict(X_test)
print("KNN Accuracy:", accuracy_score(y_test, knn_pred))

# ===================================================
# 3️⃣ REGRESSION EXAMPLE (Linear Regression)
# ===================================================
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Example dataset
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])  # y = 2x

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)
y_pred = lin_reg.predict(X_test)

print("Linear Regression Coeff:", lin_reg.coef_)
print("MSE:", mean_squared_error(y_test, y_pred))

# ===================================================
# 4️⃣ DATA PREPROCESSING
# ===================================================
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Standardization (mean=0, std=1)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(iris.data)
print("Scaled Features (first row):", X_scaled[0])

# ===================================================
# 5️⃣ PIPELINE EXAMPLE
# ===================================================
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression(max_iter=200))
])
pipeline.fit(X_train, y_train)
pipeline_pred = pipeline.predict(X_test)
print("Pipeline Accuracy:", accuracy_score(y_test, pipeline_pred))

# ===================================================
# 6️⃣ MODEL SELECTION (Cross Validation & Hyperparameter Tuning)
# ===================================================
from sklearn.model_selection import cross_val_score, GridSearchCV

# Cross validation
cv_scores = cross_val_score(LogisticRegression(max_iter=200), X, y, cv=5)
print("Cross Validation Scores:", cv_scores)

# Hyperparameter tuning using GridSearch
param_grid = {"n_neighbors": [3, 5, 7]}
grid_search = GridSearchCV(KNeighborsClassifier(), param_grid, cv=3)
grid_search.fit(X, y)
print("Best K for KNN:", grid_search.best_params_)

# ===================================================
# 7️⃣ CLUSTERING (UNSUPERVISED LEARNING)
# ===================================================
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans.fit(X)
print("Cluster Centers:\n", kmeans.cluster_centers_)

# ===================================================
# 8️⃣ DIMENSIONALITY REDUCTION (PCA)
# ===================================================
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
print("PCA Reduced Shape:", X_pca.shape)

# ===================================================
# 9️⃣ MODEL METRICS
# ===================================================
from sklearn.metrics import classification_report, confusion_matrix

print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# ===================================================
# 🔟 SAVING & LOADING MODELS
# ===================================================
import joblib

joblib.dump(model, "logistic_model.pkl")  # Save model
loaded_model = joblib.load("logistic_model.pkl")  # Load model
print("Loaded Model Accuracy:", accuracy_score(y_test, loaded_model.predict(X_test)))

"""
====================================================
📌 SUMMARY OF IMPORTANT MODULES IN SCIKIT-LEARN
====================================================

🔹 sklearn.datasets → Built-in datasets (iris, digits, wine, breast_cancer)
🔹 sklearn.model_selection → train_test_split, cross_val_score, GridSearchCV
🔹 sklearn.metrics → accuracy_score, confusion_matrix, classification_report
🔹 sklearn.preprocessing → StandardScaler, MinMaxScaler, OneHotEncoder
🔹 sklearn.pipeline → Pipeline for chaining steps
🔹 sklearn.linear_model → LinearRegression, LogisticRegression
🔹 sklearn.tree → DecisionTreeClassifier, DecisionTreeRegressor
🔹 sklearn.ensemble → RandomForestClassifier, GradientBoostingClassifier
🔹 sklearn.svm → Support Vector Machines
🔹 sklearn.cluster → KMeans, DBSCAN
🔹 sklearn.decomposition → PCA (Dimensionality Reduction)
🔹 joblib → Save/Load trained models

====================================================
💡 REAL-WORLD USE CASES:
====================================================
✅ Predicting customer churn (classification)
✅ House price prediction (regression)
✅ Image classification using SVM/RandomForest
✅ Sentiment analysis (text classification)
✅ Clustering customers into groups
✅ Feature reduction using PCA
✅ Building ML pipelines for production

"""
