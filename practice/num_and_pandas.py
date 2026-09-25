import pandas as pd
import numpy as np

file_paths = r"C:\Users\A\Desktop\vk\challenge_dataset_chennai_metro_station_activity.csv"
metro_data = pd.read_csv(file_paths)
metro_copy = metro_data.copy()

#Convert these columns into a NumPy array:
entries_exits_array = metro_copy[
    ['daily_entries', 'daily_exits']
].to_numpy()

#Calculate entry-exit difference
entries_exit_difference = entries_exits_array[:,0] - entries_exits_array[:,1] #column 0 → daily_entries
#column 1 → daily_exits

# or
entries = metro_copy['daily_entries'].to_numpy()
exits = metro_copy['daily_exits'].to_numpy()

difference = entries - exits

#Find the largest entry-exit difference
max_difference = entries_exit_difference.max()
#identify which station has that difference using
#Use np.argmax() to find the position of the maximum value:
max_index = np.argmax(entries_exit_difference)
#Then use that index with Pandas:
station = metro_copy.loc[
    max_index,
    ['station_name','daily_entries','daily_exits']
]

#overall entry/exit ratio
total_entries = entries.sum()
total_exits = exits.sum()
entries_exit_ratio = total_entries / total_exits

print(entries_exits_array)
print(entries_exits_array.shape)
print(entries_exit_difference)
print("maximum difference",max_difference)
print("Index",max_index)
print(station)
print("Overall entry exit ratio is", entries_exit_ratio)