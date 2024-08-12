import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('D:\python\customers.csv')

# List of major cities to include
major_cities = ['New York', 'Los Angeles', 'Wilsonton', 'Morganside', 'New Alvin']

# Filter the data to include only rows from the major cities
filtered_df = df[df['City'].isin(major_cities)]

# Count the number of customers in each major city
city_counts = filtered_df['City'].value_counts()

# Calculate the total number of customers in the major cities
total_customers = city_counts.sum()

# Calculate percentages
city_percentages = (city_counts / total_customers) * 100

# Plot the pie chart
plt.figure(figsize=(10, 7))
plt.pie(city_percentages, labels=city_percentages.index, autopct='%1.1f%%', startangle=140)
plt.title('Customer Segmentation Address')
plt.show()
