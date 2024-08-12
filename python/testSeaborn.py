import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Load data from CSV file
file_path = 'D:/python/product_details.csv'
df = pd.read_csv(file_path)
# Convert DateAdded to datetime format
df['DateAdded'] = pd.to_datetime(df['DateAdded'])

# Sort data by DateAdded
df = df.sort_values(by='DateAdded')
# Set the style
sns.set(style='whitegrid')

# Create the plot
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='DateAdded', y='Price', marker='o', color='b')

# Add title and labels
plt.title('Product Price Over Time')
plt.xlabel('Date Added')
plt.ylabel('Price')

# Display the plot
plt.tight_layout()
plt.show()
