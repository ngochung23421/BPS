import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Load the data from the CSV file
file_path = r'D:\python\product_details.csv'
df = pd.read_csv(file_path)

# Extract features and target variable
X = df[['Price']].values  # Feature: Price
y = df['StockQuantity'].values  # Target: Stock Quantity

# Train a linear regression model
model = LinearRegression()
model.fit(X, y)

# Predict values for plotting the regression line
X_fit = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
y_fit = model.predict(X_fit)

# Plot the data and the regression line
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', label='Actual Stock Quantity')
plt.plot(X_fit, y_fit, color='red', linewidth=2, label='Regression Line')
plt.xlabel('Price')
plt.ylabel('Stock Quantity')
plt.title('Product Growth: Price vs Stock Quantity')
plt.legend()
plt.grid(True)
plt.show()

