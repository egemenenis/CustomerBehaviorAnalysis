# -*- coding: utf-8 -*-
"""customer_behavior_analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VZ0c6kcchfSwgfW7tDlB_EwS4Wh6kMW6
"""

# Load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import drive
drive.mount('/content/drive')

# Specify the file path
file_path = '/content/drive/MyDrive/my_data/customer_data.csv'

# Load data
df = pd.read_csv(file_path)

from google.colab import files
uploaded = files.upload()

import io
df = pd.read_csv(io.BytesIO(uploaded['customer_data.csv']))

# Display first 5 lines
print(df.head())

# Check data types
print(df.info())

# Check for missing values
print(df.isnull().sum())

# Remove or fill in missing values
df = df.dropna()  # You can remove missing data
# or df.fillna(value) you can fill in missing data with a value

import pandas as pd

# Specify the correct separator when rereading the data
df = pd.read_csv('customer_data.csv', sep=';')

# Check columns
print(df.columns)

# General statistics
print(df.describe())

# Average and median values ​​for metrics like Age, Spending and Purchase Frequency
print("Average Age:", df['Age'].mean())
print("Average Spending:", df['Total_Spent'].mean())
print("Average Purchase Frequency:", df['Purchase_Frequency'].mean())

# Age segmentation
bins = [0, 25, 35, 45, 100]
labels = ['18-25', '26-35', '36-45', '46+']
df['Age_Segment'] = pd.cut(df['Age'], bins=bins, labels=labels)

# Number of customers in each age segment
print(df['Age_Segment'].value_counts())

# Spending analysis by product categories
category_spending = df.groupby('Product_Category')['Total_Spent'].mean()
print(category_spending)

# Comparison of product categories and purchasing frequency
category_frequency = df.groupby('Product_Category')['Purchase_Frequency'].mean()
print(category_frequency)

# Convert 'Date' column to datetime type
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Check the conversion process
print(df['Date'].head())

# Total monthly spending
df['Month'] = df['Date'].dt.to_period('M')
monthly_spending = df.groupby('Month')['Total_Spent'].sum()
print(monthly_spending)

# Monthly purchasing frequency
monthly_frequency = df.groupby('Month')['Purchase_Frequency'].sum()
print(monthly_frequency)

# Separate repeat buyers and non-purchasers using the Purchased_Next column
repeat_buyers = df[df['Purchased_Next'] == 1]
non_repeat_buyers = df[df['Purchased_Next'] == 0]

# Difference in spending between repeat shoppers and non-repurchasers
print("Average Expenditure of Repeat Customers:", repeat_buyers['Total_Spent'].mean())
print("Average Expenditure of Customers Who Do Not Shop Again:", non_repeat_buyers['Total_Spent'].mean())

# Spending distribution by product categories
plt.figure(figsize=(10, 6))
sns.barplot(x=category_spending.index, y=category_spending.values)
plt.title('Average Spending by Product Categories')
plt.xticks(rotation=45)
plt.show()

# Average spend by age segment
plt.figure(figsize=(8, 5))
sns.boxplot(x='Age_Segment', y='Total_Spent', data=df)
plt.title('Expenditure Distribution by Age Segments')
plt.show()

# Save CLV and segment information to a new CSV file
df.to_csv('customer_analysis_results.csv', index=False)