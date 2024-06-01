# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np
#
# # Load the dataset
# file_path = 'uber-raw-data-sep14.csv'
# data = pd.read_csv(file_path)
#
# # Convert the Date/Time column to datetime
# data['Date/Time'] = pd.to_datetime(data['Date/Time'], format='%m/%d/%Y %H:%M:%S')
#
# # Sort the data by base and Date/Time
# data = data.sort_values(by=['Base', 'Date/Time'])
#
# # Calculate the time difference between consecutive pickups
# data['Time_Diff'] = data.groupby('Base')['Date/Time'].diff().dt.total_seconds().dropna()
#
# # Set the style
# sns.set(style="whitegrid")
#
# # Plot the distribution of time differences (proxy for ride durations)
# plt.figure(figsize=(12, 6))
# sns.histplot(data['Time_Diff'], bins=np.arange(0, 3600, 60), kde=False, color='blue', alpha=0.7)
# plt.title('Distribution of Time Differences Between Consecutive Pickups', fontsize=16)
# plt.xlabel('Time Difference (seconds)', fontsize=14)
# plt.ylabel('Frequency', fontsize=14)
# plt.grid(True, which='both', linestyle='--', linewidth=0.5)
# plt.tight_layout()
# plt.show()


#Uaing Histogram plot
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np
#
# # Load the dataset
# file_path = 'uber-raw-data-sep14.csv'
# data = pd.read_csv(file_path)
#
# # Convert the Date/Time column to datetime
# data['Date/Time'] = pd.to_datetime(data['Date/Time'], format='%m/%d/%Y %H:%M:%S')
#
# # Sort the data by base and Date/Time
# data = data.sort_values(by=['Base', 'Date/Time'])
#
# # Calculate the time difference between consecutive pickups
# data['Time_Diff'] = data.groupby('Base')['Date/Time'].diff().dt.total_seconds().dropna()
#
# # Filter out extremely large time differences to focus on more common intervals
# data = data[data['Time_Diff'] < 3600]  # Only consider differences less than an hour
#
# # Set the style
# sns.set(style="whitegrid")
#
# # Plot the distribution of time differences
# plt.figure(figsize=(12, 6))
# sns.histplot(data['Time_Diff'], bins=np.arange(0, 3600, 60), kde=True, color='blue', alpha=0.7)
# plt.yscale('log')
# plt.title('Distribution of Time Differences Between Consecutive Pickups', fontsize=16)
# plt.xlabel('Time Difference (seconds)', fontsize=14)
# plt.ylabel('Frequency (log scale)', fontsize=14)
#
# # Add annotations
# median_time_diff = data['Time_Diff'].median()
# mean_time_diff = data['Time_Diff'].mean()
# plt.axvline(median_time_diff, color='red', linestyle='--', label=f'Median: {median_time_diff:.1f} s')
# plt.axvline(mean_time_diff, color='green', linestyle='-', label=f'Mean: {mean_time_diff:.1f} s')
#
# # Add legend
# plt.legend()
#
# # Add grid
# plt.grid(True, which='both', linestyle='--', linewidth=0.5)
#
# # Add a tight layout
# plt.tight_layout()
#
# # Show plot
# plt.show()



#Using Barplot
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# # Load the dataset
# file_path = 'uber-raw-data-sep14.csv'
# data = pd.read_csv(file_path)
#
# # Convert the Date/Time column to datetime
# data['Date/Time'] = pd.to_datetime(data['Date/Time'], format='%m/%d/%Y %H:%M:%S')
#
# # Sort the data by base and Date/Time
# data = data.sort_values(by=['Base', 'Date/Time'])
#
# # Calculate the time difference between consecutive pickups
# data['Time_Diff'] = data.groupby('Base')['Date/Time'].diff().dt.total_seconds().dropna()
#
# # Filter out extremely large time differences to focus on more common intervals
# data = data[data['Time_Diff'] < 3600]  # Only consider differences less than an hour
#
# # Calculate the mean time difference for each base
# mean_time_diff = data.groupby('Base')['Time_Diff'].mean()
#
# # Set the style
# sns.set(style="whitegrid")
#
# # Create a bar plot
# plt.figure(figsize=(12, 8))
# sns.barplot(x=mean_time_diff.index, y=mean_time_diff.values, palette='muted')
#
# # Add titles and labels
# plt.title('Mean Time Difference Between Consecutive Pickups by Base', fontsize=16)
# plt.xlabel('Base', fontsize=14)
# plt.ylabel('Mean Time Difference (seconds)', fontsize=14)
#
# # Add grid
# plt.grid(True, which='both', linestyle='--', linewidth=0.5)
#
# # Rotate x-axis labels for better readability
# plt.xticks(rotation=45)
#
# # Add a tight layout
# plt.tight_layout()
#
# # Show plot
# plt.show()


#Using Scatter plot
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'uber-raw-data-sep14.csv'
data = pd.read_csv(file_path)

# Convert the Date/Time column to datetime
data['Date/Time'] = pd.to_datetime(data['Date/Time'], format='%m/%d/%Y %H:%M:%S')

# Sort the data by base and Date/Time
data = data.sort_values(by=['Base', 'Date/Time'])

# Calculate the time difference between consecutive pickups
data['Time_Diff'] = data.groupby('Base')['Date/Time'].diff().dt.total_seconds().dropna()

# Filter out extremely large time differences to focus on more common intervals
data = data[data['Time_Diff'] < 3600]  # Only consider differences less than an hour

# Set the style
sns.set(style="whitegrid")

# Plot the distribution of time differences using a scatter plot
plt.figure(figsize=(12, 6))
sns.scatterplot(x=data.index, y='Time_Diff', data=data, color='blue', alpha=0.5)
plt.title('Distribution of Time Differences Between Consecutive Pickups', fontsize=16)
plt.xlabel('Index', fontsize=14)
plt.ylabel('Time Difference (seconds)', fontsize=14)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Add informative text annotations
plt.text(0.5, 0.95, 'Time Differences less than 1 hour', horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes, fontsize=12, bbox=dict(facecolor='white', alpha=0.5))

plt.tight_layout()
plt.show()
