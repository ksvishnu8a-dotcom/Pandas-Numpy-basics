import pandas as pd

file_paths = r"C:\Users\A\Desktop\vk\challenge_dataset_chennai_metro_station_activity.csv"
metro_data = pd.read_csv(file_paths)
metro_copy = metro_data.copy()

#Which zone has the highest total daily entries?
most_crowded_zone = metro_copy.groupby('zone')['daily_entries'].sum()

highest_zone = most_crowded_zone.idxmax()
highest_total = most_crowded_zone.max()
print(most_crowded_zone)
print("zone :",highest_zone)
print("total daily entries",highest_total)


#Calculate the average monthly complaints for each station type.
most_complained_stations = metro_copy.groupby('station_type')[ 'monthly_complaints'].mean()
print(most_complained_stations)

#find stations satisfying both:,peak_hour_load_pct > 65 and avg_wait_minutes > 3
result1 = metro_copy.loc[
    (metro_copy['peak_hour_load_pct'] > 65) &
    (metro_copy['avg_wait_minutes'] > 3)
]
#Busy but low waiting time

#Find stations where:daily_entries > 12,000 AND avg_wait_minutes < 3
result2 = metro_copy.loc[
    (metro_copy['daily_entries'] > 12000) &
    (metro_copy['avg_wait_minutes'] < 3)
]

print(result1)
print(result2)

#Calculate the percentage of stations with parking for each zone.
parking_by_zone_percent = metro_copy.groupby('zone')['has_parking'].mean() * 100
print(metro_data.columns)
print(parking_by_zone_percent)

#Rank the stations , where the station with the highest daily_entries gets rank 1.
metro_copy['entry_rank'] = metro_copy['daily_entries'].rank( #Create a new column:
    ascending=False
)
print(metro_copy[['station_name', 'daily_entries', 'entry_rank']])