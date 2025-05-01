import pandas as pd
import matplotlib.pyplot as plt

# Load values from CSV
df = pd.read_csv('values.csv')  # Make sure your CSV file has a 'Values' column

# Define bins and labels
bins = [0, 25, 50, 75, 100]
labels = ['Low', 'Medium', 'High', 'Very High']

# Categorize values
df['Categories'] = pd.cut(df['Values'], bins=bins, labels=labels)

# Display DataFrame with categories
print("\nData with Categories:")
print(df)

# Print data types
print("\nData Types:")
print(df.dtypes)

# Plot Histogram
plt.hist(df['Values'], bins=bins, color='blue', edgecolor='black')
plt.title('Value Distribution')
plt.xlabel('Range')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
plt.show()
