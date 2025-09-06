"""
data_manipulation_master.py
Comprehensive notes + practical implementations for:
- NumPy (arrays, vectorization)
- Pandas (EDA, cleaning, feature engineering, encoding, merging)
- Matplotlib (visualization, EDA plots)
Includes:
- Synthetic dataset creation
- EDA functions and visualizations
- Preprocessing pipeline (imputation, encoding, scaling)
- Simple modeling (uses sklearn if available, otherwise simple linear/logistic demo)
- Time-series resampling & rolling
- Chunked CSV processing example
- Memory optimization tips
Run the file to execute the example pipeline.
"""

# ---------------------------------------------------------------------
# Imports & global settings
# ---------------------------------------------------------------------
import os
import gc
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Optional extras (use if available)
try:
    import seaborn as sns
    _HAS_SEABORN = True
except Exception:
    _HAS_SEABORN = False

try:
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score, classification_report
    _HAS_SKLEARN = True
except Exception:
    _HAS_SKLEARN = False

# reproducibility
RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)

# ---------------------------------------------------------------------
# 1) Synthetic dataset generation (practical starting point)
# ---------------------------------------------------------------------
def create_synthetic_dataset(n_rows=1000):
    """
    Create a synthetic tabular dataset useful for ML demo and manipulation.
    Columns:
      - id: unique id
      - age: numeric (18-70)
      - income: numeric (k)
      - score: numeric (0-1)
      - gender: categorical (M/F)
      - city: categorical (A/B/C)
      - signup_date: datetime
      - target: binary label derived from a linear combination
    """
    ids = np.arange(1, n_rows + 1)
    age = np.random.randint(18, 71, size=n_rows)
    income = np.round(np.random.normal(loc=50_000, scale=15_000, size=n_rows)).astype(int)
    # ensure no negative incomes
    income = np.where(income < 5_000, 5_000, income)
    score = np.random.beta(2, 5, size=n_rows)  # between 0 and 1 (skewed)
    gender = np.random.choice(['M', 'F'], size=n_rows, p=[0.48, 0.52])
    city = np.random.choice(['A', 'B', 'C'], size=n_rows, p=[0.5, 0.3, 0.2])

    # signup dates within last 3 years
    start = pd.Timestamp('2022-01-01').to_pydatetime()
    signup_offsets = np.random.randint(0, 365 * 3, size=n_rows)
    signup_date = [pd.Timestamp(start + pd.Timedelta(days=int(d))) for d in signup_offsets]

    # target = 1 if linear score > threshold (introduce some noise)
    linear_score = (0.03 * age) + (0.00002 * income) + (1.5 * score) + (gender == 'M') * 0.1
    prob = 1 / (1 + np.exp(-linear_score + np.random.normal(0, 0.5, size=n_rows)))  # logistic transform with noise
    target = (prob > 0.5).astype(int)

    df = pd.DataFrame({
        'id': ids,
        'age': age,
        'income': income,
        'score': score,
        'gender': gender,
        'city': city,
        'signup_date': signup_date,
        'target': target
    })

    # Intentionally add some missingness for demo
    mask = np.random.rand(n_rows) < 0.05
    df.loc[mask, 'income'] = np.nan
    mask2 = np.random.rand(n_rows) < 0.03
    df.loc[mask2, 'city'] = None

    return df

# ---------------------------------------------------------------------
# 2) Exploratory Data Analysis (EDA) helpers
# ---------------------------------------------------------------------
def eda_summary(df, max_categories=10):
    """Print quick EDA summary"""
    print("\n------ EDA SUMMARY ------")
    print("Shape:", df.shape)
    print("\nData Types:")
    print(df.dtypes)
    print("\nHead:")
    print(df.head())
    print("\nDescription (numeric):")
    print(df.describe().T)
    print("\nMissing values per column:")
    print(df.isna().sum())
    print("\nUnique values (sample):")
    for col in df.columns:
        if df[col].dtype == 'object' or pd.api.types.is_categorical_dtype(df[col]):
            val_count = df[col].nunique(dropna=False)
            if val_count <= max_categories:
                print(f" - {col}: {val_count} unique -> {df[col].value_counts(dropna=False).to_dict()}")
            else:
                print(f" - {col}: {val_count} unique (too many to show)")

def plot_numeric_distributions(df, numeric_cols=None, bins=30):
    """Plot histograms for numeric columns (matplotlib)"""
    if numeric_cols is None:
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    n = len(numeric_cols)
    cols = 3
    rows = math.ceil(n / cols)
    plt.figure(figsize=(cols * 4, rows * 3))
    for i, col in enumerate(numeric_cols, 1):
        plt.subplot(rows, cols, i)
        plt.hist(df[col].dropna(), bins=bins)
        plt.title(col)
    plt.tight_layout()
    plt.show()

def plot_correlation_heatmap(df, numeric_cols=None):
    """Plot correlation matrix heatmap (uses seaborn if available)"""
    if numeric_cols is None:
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    corr = df[numeric_cols].corr()
    plt.figure(figsize=(8, 6))
    if _HAS_SEABORN:
        sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm')
    else:
        plt.imshow(corr, cmap='coolwarm', interpolation='none')
        plt.colorbar()
        ticks = range(len(numeric_cols))
        plt.xticks(ticks, numeric_cols, rotation=45, ha='right')
        plt.yticks(ticks, numeric_cols)
        for (i, j), val in np.ndenumerate(corr.values):
            plt.text(j, i, f"{val:.2f}", ha='center', va='center', color='k', fontsize=8)
    plt.title("Correlation Matrix")
    plt.tight_layout()
    plt.show()

def plot_category_counts(df, cat_col, top_n=10):
    counts = df[cat_col].value_counts(dropna=False).head(top_n)
    plt.figure(figsize=(6, 4))
    counts.plot(kind='bar')
    plt.title(f"Counts for {cat_col}")
    plt.ylabel("count")
    plt.show()

# ---------------------------------------------------------------------
# 3) Preprocessing pipeline (imputation, encoding, scaling)
# ---------------------------------------------------------------------
def preprocess(df, numeric_impute_strategy='median', drop_cols=None, encode=True, scale=True):
    """
    Preprocess DataFrame:
      - handle missing numeric values (median or mean)
      - handle missing categorical (fill with 'missing')
      - convert categories to 'category' dtype
      - optional: one-hot encode categorical columns (pd.get_dummies)
      - optional: scale numeric columns (StandardScaler if sklearn available else manual z-score)
    Returns: processed_df, metadata
    """
    df = df.copy()
    meta = {}

    if drop_cols:
        df.drop(columns=drop_cols, inplace=True, errors='ignore')

    # Separate types
    num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    cat_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
    meta['num_cols'] = num_cols
    meta['cat_cols'] = cat_cols

    # Impute numeric
    for col in num_cols:
        if df[col].isna().any():
            if numeric_impute_strategy == 'median':
                val = df[col].median()
            else:
                val = df[col].mean()
            df[col].fillna(val, inplace=True)

    # Impute categorical
    for col in cat_cols:
        if df[col].isna().any():
            mode = df[col].mode(dropna=True)
            fill_val = mode[0] if not mode.empty else 'missing'
            df[col].fillna(fill_val, inplace=True)

    # Convert to category dtype for memory & faster operations
    for col in cat_cols:
        df[col] = df[col].astype('category')

    # One-hot encoding (pd.get_dummies)
    if encode and cat_cols:
        df = pd.get_dummies(df, columns=cat_cols, drop_first=True)
        # update numeric columns list
        meta['encoded_columns'] = [c for c in df.columns if c not in meta['num_cols'] and c != 'target']
    else:
        meta['encoded_columns'] = []

    # Scaling numeric columns
    if scale and meta['num_cols']:
        if _HAS_SKLEARN:
            scaler = StandardScaler()
            df[meta['num_cols']] = scaler.fit_transform(df[meta['num_cols']])
            meta['scaler'] = scaler
        else:
            # manual z-score
            for col in meta['num_cols']:
                mean = df[col].mean()
                std = df[col].std(ddof=0) if df[col].std(ddof=0) != 0 else 1.0
                df[col] = (df[col] - mean) / std
            meta['scaler'] = 'manual_zscore'

    return df, meta

# ---------------------------------------------------------------------
# 4) Train simple model (classification) - uses sklearn if available
# ---------------------------------------------------------------------
def simple_classification_pipeline(df, target_col='target', test_size=0.2, random_state=RANDOM_SEED):
    """
    Example classification pipeline:
      - split
      - train LogisticRegression if sklearn available
      - otherwise uses thresholding on a linear score
    Returns: trained_model_or_info, metrics_dict
    """
    df = df.copy()
    if target_col not in df.columns:
        raise ValueError("target_col not found in DataFrame")

    X = df.drop(columns=[target_col])
    y = df[target_col]

    # simple train-test split
    if _HAS_SKLEARN:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, stratify=y, random_state=random_state)
    else:
        # manual shuffle split
        idx = np.arange(len(df))
        np.random.shuffle(idx)
        split = int(len(df) * (1 - test_size))
        train_idx = idx[:split]; test_idx = idx[split:]
        X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
        y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]

    # model training
    if _HAS_SKLEARN:
        model = LogisticRegression(max_iter=200)
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        proba = model.predict_proba(X_test)[:, 1]
        acc = accuracy_score(y_test, preds)
        cm = confusion_matrix(y_test, preds)
        try:
            auc = roc_auc_score(y_test, proba)
        except Exception:
            auc = None
        metrics = {'accuracy': acc, 'confusion_matrix': cm, 'roc_auc': auc}
        return model, metrics
    else:
        # fallback: build a linear score from coefficients by linear regression (pseudo-inverse)
        X_mat = np.c_[np.ones(len(X_train)), X_train.values]
        y_vec = y_train.values
        # compute beta via least squares: beta = (X^T X)^-1 X^T y
        beta = np.linalg.pinv(X_mat.T.dot(X_mat)).dot(X_mat.T).dot(y_vec)
        def linear_score(X_df):
            X_local = np.c_[np.ones(len(X_df)), X_df.values]
            return X_local.dot(beta)
        scores = linear_score(X_test)
        preds = (scores > np.median(scores)).astype(int)
        acc = (preds == y_test.values).mean()
        cm = np.array([[int(((preds==0)&(y_test.values==0)).sum()), int(((preds==1)&(y_test.values==0)).sum())],
                       [int(((preds==0)&(y_test.values==1)).sum()), int(((preds==1)&(y_test.values==1)).sum())]])
        metrics = {'accuracy': acc, 'confusion_matrix': cm}
        return {'beta': beta}, metrics

# ---------------------------------------------------------------------
# 5) Time-series examples: resampling & rolling
# ---------------------------------------------------------------------
def time_series_examples():
    # create daily sales data for 2 years
    idx = pd.date_range(start='2023-01-01', periods=365*2, freq='D')
    sales = 100 + 10 * np.sin(np.linspace(0, 20, len(idx))) + np.random.normal(0, 5, len(idx))
    ts = pd.Series(sales, index=idx, name='sales')

    # Resample monthly
    monthly = ts.resample('M').sum()
    # Rolling mean (30-day)
    rolling_30 = ts.rolling(window=30, min_periods=1).mean()

    # Plot
    plt.figure(figsize=(10, 4))
    plt.plot(ts.index, ts.values, alpha=0.4, label='daily')
    plt.plot(rolling_30.index, rolling_30.values, color='red', label='30-day rolling mean')
    plt.title("Daily Sales and 30-day Rolling Mean")
    plt.legend()
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(8, 3))
    monthly.plot(kind='bar')
    plt.title("Monthly Sales (sum)")
    plt.tight_layout()
    plt.show()

# ---------------------------------------------------------------------
# 6) Chunked CSV processing (memory-efficient aggregation)
# ---------------------------------------------------------------------
def chunked_csv_aggregation(csv_path, chunk_size=1000):
    """
    Example: read a very large CSV in chunks and compute aggregated metrics
    (mean income per city) without loading whole file in memory.
    """
    agg = {}
    count = {}
    for chunk in pd.read_csv(csv_path, chunksize=chunk_size):
        for city, group in chunk.groupby('city'):
            if pd.isna(city):
                city = 'missing'
            agg.setdefault(city, 0.0)
            count.setdefault(city, 0)
            agg[city] += group['income'].sum(skipna=True)
            count[city] += group['income'].count()
    # compute means
    means = {city: (agg[city] / count[city]) if count[city] > 0 else np.nan for city in agg}
    return means

# ---------------------------------------------------------------------
# 7) Memory optimization tips (dtypes and downcasting)
# ---------------------------------------------------------------------
def optimize_dataframe_memory(df):
    """
    Downcast numeric types and convert object columns with low cardinality to category
    Returns optimized df and summary of memory reduction
    """
    start_mem = df.memory_usage(deep=True).sum() / 1024**2
    df_opt = df.copy()
    for col in df_opt.select_dtypes(include=['int64', 'int32']).columns:
        df_opt[col] = pd.to_numeric(df_opt[col], downcast='integer')
    for col in df_opt.select_dtypes(include=['float64']).columns:
        df_opt[col] = pd.to_numeric(df_opt[col], downcast='float')
    for col in df_opt.select_dtypes(include=['object']).columns:
        num_unique = df_opt[col].nunique()
        num_total = len(df_opt[col])
        if num_unique / num_total < 0.5:
            df_opt[col] = df_opt[col].astype('category')
    end_mem = df_opt.memory_usage(deep=True).sum() / 1024**2
    return df_opt, start_mem, end_mem

# ---------------------------------------------------------------------
# 8) Practical end-to-end demo that uses the above pieces
# ---------------------------------------------------------------------
def demo_pipeline():
    print("\n=== Creating synthetic dataset ===")
    df = create_synthetic_dataset(2000)
    # quick save to CSV for chunk demo
    csv_path = "demo_synthetic.csv"
    df.to_csv(csv_path, index=False)

    # EDA
    eda_summary(df)
    plot_numeric_distributions(df, numeric_cols=['age', 'income', 'score'])
    plot_category_counts(df, 'gender')
    if _HAS_SEABORN:
        plot_correlation_heatmap(df, numeric_cols=['age', 'income', 'score'])

    # Preprocessing
    print("\n=== Preprocessing ===")
    df_proc, meta = preprocess(df, numeric_impute_strategy='median', encode=True, scale=True)
    print("Processed shape:", df_proc.shape)
    print("Meta keys:", list(meta.keys()))

    # Save cleaned data
    cleaned_csv = "cleaned_demo.csv"
    df_proc.to_csv(cleaned_csv, index=False)
    print("Saved cleaned data to", cleaned_csv)

    # Simple model
    print("\n=== Modeling ===")
    try:
        model, metrics = simple_classification_pipeline(df_proc, target_col='target')
        print("Model metrics:", metrics)
        if _HAS_SKLEARN and hasattr(model, 'coef_'):
            print("Coefficients:", model.coef_)
            print("Intercept:", model.intercept_)
    except Exception as e:
        print("Modeling failed:", e)

    # Time-series demo
    print("\n=== Time-series demo ===")
    time_series_examples()

    # Chunk processing example (uses the earlier saved CSV)
    print("\n=== Chunked CSV Aggregation ===")
    city_income_means = chunked_csv_aggregation(csv_path, chunk_size=500)
    print("Mean income per city (from chunks):", city_income_means)

    # Memory optimization
    print("\n=== Memory optimization ===")
    df_opt, mem_before, mem_after = optimize_dataframe_memory(df)
    print(f"Memory before: {mem_before:.2f} MB, after: {mem_after:.2f} MB")

    # cleanup
    try:
        os.remove(csv_path)
        os.remove(cleaned_csv)
    except Exception:
        pass
    gc.collect()
    print("\nDemo pipeline completed.")

# ---------------------------------------------------------------------
# 9) Practical Tips & Checklist (printed at end)
# ---------------------------------------------------------------------
PRACTICAL_TIPS = """
PRACTICAL TIPS & CHECKLIST
- Always inspect df.info() and df.describe() after loading data.
- Prefer vectorized ops (numpy/pandas) over Python loops for speed.
- Use pd.read_csv(..., dtype=...) or converters to reduce memory.
- Convert string columns with low cardinality to 'category' dtype.
- Impute carefully (median is robust to outliers).
- For ML: split data before target leakage-prone feature engineering.
- Use StandardScaler (or RobustScaler) for numeric features when required.
- Use chunked reading for very large files -> process/aggregate then discard chunk.
- Log random seeds for reproducibility.
- Save intermediate cleaned data to disk (csv/parquet) for reproducibility.
"""

# ---------------------------------------------------------------------
# If executed as script, run demo pipeline
# ---------------------------------------------------------------------
if __name__ == "__main__":
    print("Data Manipulation Master File — starting demo pipeline.")
    demo_pipeline()
    print(PRACTICAL_TIPS)
