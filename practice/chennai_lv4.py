import pandas as pd 
import numpy as np

file_paths = r'C:\Users\A\Desktop\vk\challenge_dataset_chennai_metro_station_activity.csv'
metro_data = pd.read_csv(file_paths)
south_stations = metro_data[metro_data['zone'] =='South' # all the station in south zone
                            ]

result_and = metro_data.loc[
    (metro_data['daily_entries'] > 10000) &
    (metro_data['peak_hour_load_pct'] > 60),
    ['daily_entries', 'peak_hour_load_pct']
]
result_or = metro_data.loc[
    (metro_data['daily_entries'] >1500 ) |
    (metro_data['monthly_complaints'] > 20),
    ['daily_entries','monthly_complaints']
]
central_zone =metro_data.loc[metro_data['zone'] =='Central', ['station_name', 'zone', 'daily_entries', 'avg_wait_minutes']]
longest_waiting_time = metro_data.loc[metro_data['avg_wait_minutes'].idxmax()]
no_parking = metro_data.loc[metro_data['has_parking']==False, 
                            ['station_name', 'has_parking']
]

parking_count = metro_data['has_parking'].value_counts() 

metro_data['total_weekly_days'] =(
    metro_data['weekday_delays'] + 
    metro_data['weekend_delays']
)
result = metro_data[['station_name', 'total_weekly_days']]

print(parking_count)
print(metro_data.head())
print(south_stations)
print(result_and)
print(result_or)
print(central_zone)
print(longest_waiting_time)
print(no_parking)
print("Stations with parking:", (metro_data['has_parking'] == True).sum())
print("Stations without parking:", (metro_data['has_parking'] == False).sum())
print(parking_count)
print(result)
