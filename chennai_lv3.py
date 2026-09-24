import pandas as pd
import numpy as np
f_path = r'C:\Users\A\Desktop\vk\challenge_dataset_chennai_metro_station_activity.csv'
metro_data = pd.read_csv(f_path)

daily_entries_array = metro_data['daily_entries'].to_numpy() #onverting a Pandas column to a NumPy array
avg =np.mean(daily_entries_array)
maximum = np.max(daily_entries_array)
minimum = min(daily_entries_array)

above_avg = daily_entries_array > avg
count = above_avg.sum()
parking_percentages = metro_data['has_parking'].mean() * 100

print(daily_entries_array)
print(f"average\t: {avg}")
print(f"Minimum\t: {maximum}")
print(f"minimum\t: {minimum}")
print(f"stations count with entries above average: {count}")
print(f" stattions with parking : {round(parking_percentages,2)}%")
