import pandas as pd


metro_file_path =r'C:\Users\A\Desktop\vk\challenge_dataset_chennai_metro_station_activity.csv'
metro_data = pd.read_csv(metro_file_path)

highest_daily_value = metro_data['daily_entries'].idxmax() #Pandas finds the largest value and returns the index of that row.
highest_daily_entry = metro_data['daily_entries'].max() # just only find the maximum value in the daily entries 
slct_row = metro_data.loc[0] #gives row whose index label is 1
highest_station = metro_data.loc[metro_data['daily_entries'].idxmax() ] #gives the entire row belonging to that maximum.
lowest_station = metro_data.loc[metro_data['daily_entries'].idxmin()]  #gives the entire row belonging to that minimum.
avg_entry = metro_data['daily_entries'].mean() #gives the average entry
avg_entry_by_zone = metro_data.groupby('zone')['daily_entries'].mean() #groups all rows belonging to the same zone. and calculates the average entries within each group.
stan_types = metro_data['station_type'].value_counts() #counts how many times each unique value appears,. Count how many stations belong to each station type.
peak_load = metro_data.loc[
    metro_data['peak_hour_load_pct'] > 70, #stations where peak-hour load is above 70%,
    ['station_name', 'zone','peak_hour_load_pct']    #colums we want to display with condition
]

sorted_stations = metro_data.sort_values(  #sorting values
    'daily_entries',
    ascending=False
)   [['station_name','daily_entries']]

top5_complaints =metro_data.sort_values(
    'monthly_complaints',
    ascending=False
)[['station_name', 'monthly_complaints']].head(5)                           
print(f"\nstation with highest daily entry:\n {highest_station}")
print(f"\nstation with lowest daily entry: \n {lowest_station}")
print(f"avg daily entry:\t {avg_entry}")
print(avg_entry_by_zone)
print(metro_data.columns)
print(metro_data.head())
print(stan_types)
print(peak_load)
print(f"""\nsortded stations:\n
      {sorted_stations}""")
print(top5_complaints)



# print(highest_daily_value)
# print(slct_row)
# print(highest_daily_entry)
