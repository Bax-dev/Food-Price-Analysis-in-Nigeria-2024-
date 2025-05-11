import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression

data = pd.read_csv('food_prices.csv')

data['Inflation_Rate'] = ((data['Current_Price'] - data['Past_Price']) / data['Past_Price']) * 100

print("Descriptive Statistics of Food Prices:\n", data.describe())

#  Missing Value Check
print("\nMissing Values in the Data:\n", data.isnull().sum())

#  Correlation Heatmap (Selecting numerical columns for correlation)
plt.figure(figsize=(10, 8))
sns.heatmap(data[['Current_Price', 'Past_Price', 'Inflation_Rate']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix of Food Prices')
plt.show()

# 5. Distribution of Current Prices
plt.figure(figsize=(10, 6))
sns.histplot(data['Current_Price'], kde=True)
plt.title('Distribution of Current Prices')
plt.xlabel('Current Price (Naira)')
plt.ylabel('Frequency')
plt.show()

# 6. Boxplot to Detect Outliers by Item
plt.figure(figsize=(12, 6))
sns.boxplot(x='Item', y='Current_Price', data=data)
plt.title('Boxplot of Current Prices by Item')
plt.xticks(rotation=45)
plt.show()

# 7. Time Series Analysis for Lagos Region
lagos_data = data[data['Region'] == 'Lagos']
plt.figure(figsize=(10, 6))
sns.lineplot(x='Month', y='Current_Price', hue='Item', data=lagos_data)
plt.title('Price Trends Over Time in Lagos')
plt.xlabel('Month')
plt.ylabel('Price (Naira)')
plt.tight_layout()
plt.show()

#  Predictive Modeling for Price Forecasting
# Preparing the data for Linear Regression Model
year_data = data.groupby('Year')['Current_Price'].mean().reset_index()
X = year_data['Year'].values.reshape(-1, 1)
y = year_data['Current_Price'].values

# Linear regression model
model = LinearRegression()
model.fit(X, y)

# Forecasting next year's average price
next_year = np.array([[2025]])
predicted_price = model.predict(next_year)
print(f"\nPredicted average price for 2025: {predicted_price[0]:.2f} Naira")

# 9. Policy Suggestions based on Inflation Rate
item_inflation = data.groupby(['Item', 'Region'])['Inflation_Rate'].mean().reset_index()
high_inflation_items = item_inflation[item_inflation['Inflation_Rate'] > 10]  # Arbitrary threshold
print("\nSuggested policy: Consider subsidizing the following items to improve food security:")
print(high_inflation_items)

# Save visualizations and reports
plt.figure(figsize=(10, 6))
sns.barplot(x='Item', y='Inflation_Rate', data=item_inflation, hue='Region')
plt.title('Inflation Rate per Food Item by Region')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('inflation_rate_report.png')  # Save the chart as PNG
plt.show()

