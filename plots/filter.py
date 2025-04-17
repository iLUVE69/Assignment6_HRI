import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV file with UTF-16 encoding
file_path = r'C:\C++\test\hri\activity6\fourth.csv'
data = pd.read_csv(file_path, encoding='utf-16')

# Print the column names to verify what's available
print("Column names in the dataset:")
print(data.columns.tolist())

# Create a time vector based on 1ms sampling
# Number of samples equals the number of rows in the dataset
time_ms = np.arange(0, len(data)) * 1  # 1ms per sample
time_seconds = time_ms / 1000  # Convert to seconds for plotting

# Set up the figure with two subplots (one for each column)
plt.figure(figsize=(12, 8))

# Assuming the first two numeric columns are what we want to plot
# If you need specific columns, replace this with their actual names
numeric_columns = data.select_dtypes(include=[np.number]).columns

if len(numeric_columns) >= 1:
    # Plot first column
    plt.subplot(2, 1, 1)
    plt.plot(time_seconds, data[numeric_columns[0]], 'b-', linewidth=1)
    plt.title(f'{numeric_columns[0]} vs Time')
    plt.xlabel('Time (seconds)')
    plt.ylabel(numeric_columns[0])
    plt.grid(True)
    
if len(numeric_columns) >= 2:
    # Plot second column
    plt.subplot(2, 1, 2)
    plt.plot(time_seconds, data[numeric_columns[1]], 'r-', linewidth=1)
    plt.title(f'{numeric_columns[1]} vs Time')
    plt.xlabel('Time (seconds)')
    plt.ylabel(numeric_columns[1])
    plt.grid(True)

# If there are no numeric columns or you need to plot specific columns,
# you might need to modify the code above to target those specific columns

plt.tight_layout()
plt.savefig('time_series_plot.png')  # Save the figure
plt.show()  # Display the plot

# Print summary statistics
print("\nSummary statistics:")
print(data.describe())