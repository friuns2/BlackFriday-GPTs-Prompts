# 🧠 Data Science

## Introduction

This document serves as a comprehensive and detailed guide for users aiming to harness the power of GPT-based AI assistants for **data science workflows** including data cleaning, exploratory data analysis (EDA), machine learning, statistical testing, visualization, automation, and even prompt engineering to optimize AI-driven data science.

Each section presents:

* A detailed explanation of the task
* Best practices and considerations
* Example prompt templates to use with GPT
* Python code snippets using common libraries (pandas, numpy, sklearn, matplotlib, seaborn)
* Suggestions for example datasets you can use to practice
* Tips on how to attach or structure your data when querying GPT

---

## 📊 1. Data Cleaning

### What it is:

Data cleaning prepares raw data by correcting or removing inaccurate, incomplete, or inconsistent records. It’s a foundational step in any data science pipeline because model accuracy, analysis validity, and insights all depend on high-quality data.

### Common problems:

* Missing values (NaNs)
* Mixed data types in columns
* Outliers or anomalies
* Duplicates
* Inconsistent formatting (dates, strings, units)
* Erroneous or invalid entries

### Best practice cleaning pipeline with pandas:

1. **Load and inspect data** — check data types, null counts, duplicates.
2. **Handle missing values** — impute with mean/median/mode or drop.
3. **Convert data types** — force numeric, datetime, categorical as needed.
4. **Remove duplicates** — based on subset of columns.
5. **Standardize formatting** — trimming whitespace, lowercasing, fixing date formats.
6. **Detect and treat outliers** — using statistical thresholds or domain rules.
7. **Validate value ranges and categories** — e.g., age between 0 and 120.
8. **Document transformations** — keep logs or comments.

### Example prompt for GPT:

> "You’re a data cleaning expert. I have a CSV file with missing values, mixed data types (e.g., numeric columns stored as strings), and inconsistent formatting (date columns with different formats). Provide me a detailed step-by-step pandas cleaning pipeline, including code snippets, explanations for each step, and advice on handling common pitfalls. Assume the dataset has \~50,000 rows and 15 columns, including dates, categories, and numeric fields."

### Example code snippet:

```python
import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv('sample_dataset.csv')

# Step 1: Inspect data
print(df.info())
print(df.head())
print(df.isnull().sum())

# Step 2: Handle missing values
# Example: Fill numeric columns with median, categorical with mode
for col in df.select_dtypes(include=['float64', 'int64']).columns:
    median = df[col].median()
    df[col].fillna(median, inplace=True)
for col in df.select_dtypes(include=['object']).columns:
    mode = df[col].mode()[0]
    df[col].fillna(mode, inplace=True)

# Step 3: Convert data types
df['date_column'] = pd.to_datetime(df['date_column'], errors='coerce')

# Step 4: Remove duplicates
df.drop_duplicates(inplace=True)

# Step 5: Standardize formatting
df['category_column'] = df['category_column'].str.strip().str.lower()

# Step 6: Detect outliers (example using z-score)
from scipy.stats import zscore
numeric_cols = df.select_dtypes(include=[np.number]).columns
df['zscore'] = zscore(df['numeric_column'])
df = df[df['zscore'].abs() < 3]  # Remove outliers > 3 std dev

# Step 7: Validate values (e.g., age range)
df = df[(df['age'] >= 0) & (df['age'] <= 120)]

# Drop helper column
df.drop('zscore', axis=1, inplace=True)
```

### Example dataset to attach or use:

* **Titanic dataset**: Contains mixed data types, missing values, and categories — perfect for cleaning.
* **Kaggle’s Credit Card Fraud Detection dataset** — great for handling imbalanced and messy financial data.
* Or any CSV with 50k rows and mixed data types (you can attach this when querying GPT or upload to a file-sharing service).

---

## 📈 2. Exploratory Data Analysis (EDA)

### What it is:

EDA is the practice of summarizing main dataset characteristics, often visually, to gain understanding and insights before modeling. It reveals patterns, anomalies, relationships, and guides feature engineering.

### Key statistics to compute:

* Summary statistics: mean, median, mode, std, min, max, quantiles
* Missing value percentages
* Distribution of each feature (histograms, boxplots)
* Relationships: correlations, scatterplots, pairplots
* Categorical value counts
* Time series trends (if applicable)

### Suggested visualizations:

* Histogram / KDE for distributions
* Boxplots for outliers
* Scatterplots for relationships
* Heatmap for correlations
* Bar charts for categorical counts
* Line plots for time series

### Example prompt for GPT:

> "Perform an exploratory data analysis (EDA) on a dataset with 100,000 rows and 20 columns containing numeric, categorical, and datetime data. Suggest a thorough EDA workflow including what summary statistics to calculate, what plots to create, how to analyze correlations, and how to detect anomalies. Provide Python code snippets using pandas, matplotlib, and seaborn."

### Example code snippet:

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('large_dataset.csv')

# Summary stats
print(df.describe(include='all'))

# Missing values
print(df.isnull().mean())

# Distribution plots for numeric features
num_cols = df.select_dtypes(include=['float64', 'int64']).columns
for col in num_cols:
    plt.figure(figsize=(8,4))
    sns.histplot(df[col].dropna(), kde=True)
    plt.title(f'Distribution of {col}')
    plt.show()

# Boxplots to spot outliers
for col in num_cols:
    plt.figure(figsize=(8,4))
    sns.boxplot(x=df[col])
    plt.title(f'Boxplot of {col}')
    plt.show()

# Correlation heatmap
plt.figure(figsize=(12,10))
sns.heatmap(df[num_cols].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation matrix')
plt.show()

# Categorical value counts bar plots
cat_cols = df.select_dtypes(include=['object']).columns
for col in cat_cols:
    plt.figure(figsize=(8,4))
    df[col].value_counts().plot(kind='bar')
    plt.title(f'Value counts of {col}')
    plt.show()
```

### Dataset suggestion:

* **Airbnb listings dataset** — contains numeric, categorical, and datetime columns.
* **NYC Taxi Trip data** — large dataset with mixed types and temporal data.

---

## 🤖 3. Machine Learning

### What it is:

Machine learning trains algorithms to identify patterns and make predictions or classifications. Common workflows include data preparation, model training, evaluation, and tuning.

### Example task:

Train a logistic regression classifier to predict customer churn.

### Key points to cover:

* Data splitting into train/test
* Feature encoding (categorical to numeric)
* Model training with Scikit-Learn
* Evaluation metrics (accuracy, precision, recall, ROC-AUC)
* Model assumptions and limitations

### Example prompt for GPT:

> "Train a logistic regression classifier using Scikit-Learn to predict customer churn based on a customer dataset with numeric and categorical features. Provide detailed code for data preprocessing, train-test split, feature encoding, model training, evaluation using accuracy, precision, recall, and ROC-AUC, and explanation of logistic regression assumptions."

### Example code snippet:

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_auc_score, classification_report

# Load data
df = pd.read_csv('customer_data.csv')

# Features and target
X = df.drop('churn', axis=1)
y = df['churn']

# Encode categorical variables
cat_cols = X.select_dtypes(include=['object']).columns
X_encoded = pd.get_dummies(X, columns=cat_cols, drop_first=True)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Train logistic regression
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:,1]

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("ROC AUC:", roc_auc_score(y_test, y_prob))
print("\nClassification Report:\n", classification\_report(y\_test, y\_pred))
```

### Dataset suggestion:

- **Telco Customer Churn Dataset** (available on Kaggle) — classic for churn prediction.
- **Bank Marketing dataset** for binary classification tasks.

---

## 🧪 4. Statistical Hypothesis Testing

### What it is:

Used to test assumptions or claims about populations, based on sample data.

### Common tests:

- t-test (compare means)
- Chi-square (categorical associations)
- ANOVA (compare multiple groups)
- Two-proportion z-test (e.g., A/B testing)

### Example prompt for GPT:

> "Explain how to perform a two-proportion z-test to compare conversion rates between two user groups in an A/B test, including hypotheses, test statistic calculation, p-value interpretation, and Python code example using `statsmodels`."

### Example code snippet:

```python
import statsmodels.api as sm
import numpy as np

# Sample data
convert_A = 200
n_A = 1000
convert_B = 240
n_B = 1200

count = np.array([convert_A, convert_B])
nobs = np.array([n_A, n_B])

# Two-proportion z-test
stat, pval = sm.stats.proportions_ztest(count, nobs)
print(f"Z-test statistic: {stat:.4f}")
print(f"P-value: {pval:.4f}")

if pval < 0.05:
    print("Reject null hypothesis: Significant difference in conversion rates")
else:
    print("Fail to reject null hypothesis: No significant difference")
````

---

## 📊 5. Visualization Best Practices

* Use clear titles and axis labels
* Use legends where multiple plots overlap
* Choose colorblind-friendly palettes
* Avoid clutter; keep charts simple
* Annotate important points or stats

---

## 📎 6. Automation & Reporting

Use Python libraries like `matplotlib`, `pandas`, `pdfkit` or `reportlab` to generate reports, and `smtplib` for email automation. Schedule via cron jobs (Linux/macOS) or Task Scheduler (Windows).

---

## 🔑 How to Attach or Provide Data for GPT

* Provide a small sample of your dataset (20-50 rows) in CSV format pasted inline or via file upload
* Share column names and data types if dataset is large or confidential
* Describe your problem context clearly: goals, dataset size, features, challenges
* Provide example rows to clarify data quirks

---

## Conclusion

This guide gives you a detailed framework to interact with GPT-based assistants in data science. You can copy-paste the prompts, attach sample data, and ask for code, explanations, or suggestions tailored to your dataset and goals.

---
