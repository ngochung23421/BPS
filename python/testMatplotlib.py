import pandas as pd
import matplotlib.pyplot as plt
# Load data from CSV file
file_path = 'D:/python/product_details.csv'
df = pd.read_csv(file_path)
# Convert DateAdded to datetime format
df['DateAdded'] = pd.to_datetime(df['DateAdded'])

# Sort data by DateAdded
df = df.sort_values(by='DateAdded')
# Set the figure size
plt.figure(figsize=(12, 6))

# Plot the data
plt.plot(df['DateAdded'], df['Price'], marker='o', linestyle='-', color='b', label='Price')

# Add title and labels
plt.title('Product Price Over Time')
plt.xlabel('Date Added')
plt.ylabel('Price')
plt.legend()

# Display the plot
plt.grid(True)
plt.tight_layout()
plt.show()
