import pandas as pd 
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

#data cleaning

missing_values = metro_data.loc[metro_data.isnull().any(axis=1)]
metro_copy = metro_data.copy()

average_wait = metro_copy['avg_wait_minutes'].mean()

metro_copy['avg_wait_minutes'] = metro_copy['avg_wait_minutes'].fillna(
    average_wait
)
median_complaints = metro_copy['monthly_complaints'].median()
metro_copy['monthly_complaints'] = metro_copy['monthly_complaints'].fillna( #Only the NaN values are replaced. Existing complaint values stay unchanged.
    median_complaints
)
average_wait_by_zone = metro_copy.groupby('zone')['avg_wait_minutes'].mean()
maximum_daily_entry_by_zone = metro_copy.groupby('zone')['daily_entries'].max()
no_station_by_zone = metro_copy.groupby('zone')['station_name'].count()

zone_stats =(
    metro_copy.groupby('zone')
    .agg( #.agg() lets you calculate multiple statistics at the same time.
        mean_daily_entries = ('daily_entries','mean'), #new_column_name=('existing_column', 'function') inside .agg
        maximum_daily_entries = ('daily_entries','max'),
        minimum_daily_entries = ('daily_entries','min'),
        mean_avg_wait_minutes =('avg_wait_minutes','mean')
    )
    .reset_index()
)
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
print(missing_values)
print(metro_copy)
print(metro_copy[['avg_wait_minutes','monthly_complaints']].isnull().sum()) # checking is there any null values
print("Average waiting time by zone",average_wait_by_zone)
print("Maximum daily entries by zone", maximum_daily_entry_by_zone)
print("Number of stations by zone ", no_station_by_zone)
print(zone_stats)
