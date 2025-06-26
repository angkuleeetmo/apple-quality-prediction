# -----------------------------------------------
# Apple Quality Dataset Analysis
# BSCS42 | MP2
# -----------------------------------------------

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# -------------------------------------------------
# Dataset Overview
# -------------------------------------------------
"""
This dataset contains information about various attributes of apples,
including size, weight, sweetness, crunchiness, juiciness, ripeness, acidity, 
and a quality label (good/bad). The goal is to explore how these characteristics 
influence the perceived quality of apples.
"""

# Load the dataset
df = pd.read_csv('Apple_Quality_Dataset.csv')

# -------------------------------------------------
# Data Cleaning
# -------------------------------------------------
"""
We begin by identifying and handling missing values, duplicate entries, 
and potential outliers that may affect the accuracy of analysis.
"""

# Check and display missing values
print("Missing values per column:")
print(df.isnull().sum())

# Drop rows with missing values (assuming minimal missing data)
df.dropna(inplace=True)

# Check and remove duplicates
duplicates = df.duplicated()
print(f"\nDuplicate rows found: {duplicates.sum()}")
df.drop_duplicates(inplace=True)

# -------------------------------------------------
# Descriptive Statistics
# -------------------------------------------------
"""
Here we examine basic descriptive statistics and distribution properties 
(mean, median, mode, skewness, kurtosis) of the numerical features.
"""

# Define numerical and categorical features
numerical_features = ['Size', 'Weight', 'Sweetness', 'Crunchiness', 'Juiciness', 'Ripeness', 'Acidity']

# Display summary statistics
print("\nSummary Statistics:")
print(df[numerical_features].describe())

# Display mode
print("\nMode for each numerical feature:")
print(df[numerical_features].mode().iloc[0])

# Display skewness and kurtosis
print("\nSkewness of numerical features:")
print(df[numerical_features].skew())

print("\nKurtosis of numerical features:")
print(df[numerical_features].kurt())

# Frequency table for the categorical feature
print("\nFrequency table for Quality:")
print(df['Quality'].value_counts())

# -------------------------------------------------
# Data Visualization
# -------------------------------------------------
"""
We use plots to better understand the distribution and relationships 
between the features and the quality classification.
"""

# -- Univariate Analysis --

# Histograms for numerical features
df[numerical_features].hist(bins=30, figsize=(15, 10))
plt.suptitle("Histograms of Numerical Features")
plt.tight_layout()
plt.show()

# Boxplots grouped by quality
for feature in numerical_features:
    plt.figure(figsize=(6, 4))
    sns.boxplot(x='Quality', y=feature, data=df)
    plt.title(f'{feature} by Apple Quality')
    plt.tight_layout()
    plt.show()

# Bar plot for Quality
plt.figure(figsize=(5, 4))
sns.countplot(x='Quality', data=df)
plt.title("Distribution of Apple Quality")
plt.show()

# -- Bivariate Analysis --

# Correlation heatmap
plt.figure(figsize=(10, 8))
correlation_matrix = df[numerical_features].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', square=True)
plt.title('Correlation Heatmap of Numerical Features')
plt.show()

# Scatter plots for selected pairs
feature_pairs = [('Sweetness', 'Juiciness'), ('Ripeness', 'Acidity'), ('Size', 'Weight')]

for x_feat, y_feat in feature_pairs:
    plt.figure(figsize=(6, 4))
    sns.scatterplot(x=x_feat, y=y_feat, hue='Quality', data=df)
    plt.title(f'{y_feat} vs. {x_feat} (colored by Quality)')
    plt.tight_layout()
    plt.show()

# -------------------------------------------------
# Insights and Hypothesis Formulation
# -------------------------------------------------
"""
Observations:
1. Apples labeled "good" tend to have higher sweetness and juiciness.
2. Size and weight show strong positive correlation — larger apples weigh more.
3. Acidity and ripeness are inversely related — riper apples are less acidic.

Hypothesis:
"Apples with higher sweetness and juiciness are more likely to be classified as good quality."

This can be tested with statistical analysis or machine learning classification techniques.
"""

input("Press Enter to close...")
