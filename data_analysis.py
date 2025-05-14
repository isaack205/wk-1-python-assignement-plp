# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris(as_frame=True)
df = iris.frame

# Display the first few rows of the dataset
print("First 5 rows of the dataset:")
print(df.head())
print("\n" + "="*50 + "\n")

# Explore the structure of the dataset
print("Dataset information:")
df.info()
print("\n" + "="*50 + "\n")

# Check for missing values
print("Missing values in the dataset:")
print(df.isnull().sum())
print("\n" + "="*50 + "\n")

# Clean the dataset (in this case, there are no missing values, so no action is needed)
if df.isnull().sum().any():
    print("Handling missing values (filling with mean):")
    for col in df.columns:
        if df[col].isnull().any():
            if pd.api.types.is_numeric_dtype(df[col]):
                df[col].fillna(df[col].mean(), inplace=True)
            else:
                df[col].fillna(df[col].mode()[0], inplace=True)
    print("Missing values after handling:")
    print(df.isnull().sum())
    print("\n" + "="*50 + "\n")
else:
    print("No missing values found in the dataset.")
    print("\n" + "="*50 + "\n")

# Compute basic statistics of numerical columns
print("Basic statistics of numerical columns:")
print(df.describe())
print("\n" + "="*50 + "\n")

# Perform groupings on the 'target' column (species) and compute the mean of numerical columns
print("Mean of numerical columns per species:")
mean_per_species = df.groupby('target').mean()
print(mean_per_species)
print("\n" + "="*50 + "\n")

# Identify patterns or interesting findings
print("Patterns and Interesting Findings:")
print("- The 'setosa' species generally has smaller sepal length, sepal width, petal length, and petal width compared to 'versicolor' and 'virginica'.")
print("- 'virginica' tends to have the largest petal length and petal width among the three species.")
print("- There is a noticeable difference in the mean values of the features across the different Iris species, suggesting that these features are good indicators for distinguishing between the species.")


# Set a visually appealing style for the plots using seaborn
sns.set(style="whitegrid")

# 1. Line chart showing trends (not directly applicable to the Iris dataset in its current form)
# We'll create a placeholder or a conceptually similar line plot

plt.figure(figsize=(8, 6))
for column in df.columns[:-1]:
    sns.lineplot(x=df.index, y=df[column], label=column)
plt.title('Feature Values Across Data Points (Conceptual Trend)')
plt.xlabel('Data Point Index')
plt.ylabel('Feature Value (cm)')
plt.legend()
plt.show()
print("\n" + "="*50 + "\n")

# 2. Bar chart showing the comparison of a numerical value across categories (average petal length per species)
plt.figure(figsize=(8, 6))
sns.barplot(x=mean_per_species.index, y='petal length (cm)', data=mean_per_species, palette='viridis')
plt.title('Average Petal Length per Iris Species')
plt.xlabel('Iris Species (0: Setosa, 1: Versicolor, 2: Virginica)')
plt.ylabel('Average Petal Length (cm)')
plt.xticks(ticks=[0, 1, 2], labels=['Setosa', 'Versicolor', 'Virginica'])
plt.show()
print("\n" + "="*50 + "\n")

# 3. Histogram of a numerical column to understand its distribution (Sepal Width)
plt.figure(figsize=(8, 6))
sns.histplot(df['sepal width (cm)'], kde=True, color='skyblue')
plt.title('Distribution of Sepal Width')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.show()
print("\n" + "="*50 + "\n")

# 4. Scatter plot to visualize the relationship between two numerical columns (Sepal Length vs. Petal Length)
plt.figure(figsize=(8, 6))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='target', data=df, palette='Set2')
plt.title('Relationship between Sepal Length and Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species', labels=['Setosa', 'Versicolor', 'Virginica'])
plt.show()
print("\n" + "="*50 + "\n")