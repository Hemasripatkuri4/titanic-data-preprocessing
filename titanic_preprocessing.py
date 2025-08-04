import pandas as pd

# Load data
df = pd.read_csv("Titanic-Dataset.csv")


# View data
print("First 5 rows:")
print(df.head())

# Check structure
print("\nData Info:")
print(df.info())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Handle missing values
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
df.drop(columns=['Cabin'], inplace=True)

# Show after missing value handling
print("\nMissing Values After Handling:")
print(df.isnull().sum())

# ---------------------------
# ✅ Encoding (this part must come AFTER missing values handled)
# ---------------------------
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)

print("\nFinal Columns After Encoding:")
print(df.columns)

print("\nFinal Data Sample:")
print(df.head())

import matplotlib.pyplot as plt
import seaborn as sns

# Step 5: Visualize Outliers
plt.figure(figsize=(12, 5))
sns.boxplot(data=df[['Age', 'Fare']])
plt.title("Boxplot for Age and Fare")
plt.show()

# Remove Outliers using IQR
for col in ['Age', 'Fare']:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    df = df[(df[col] >= lower) & (df[col] <= upper)]

print("\nShape after removing outliers:", df.shape)

from sklearn.preprocessing import StandardScaler

# Step 6: Normalize/Standardize Age and Fare
scaler = StandardScaler()
df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])

print("\nAfter Standardization:")
print(df[['Age', 'Fare']].head())

df.to_csv("processed_titanic.csv", index=False)



