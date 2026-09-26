import pandas as pd

file_paths = r"C:\Users\A\Desktop\vk\challenge_dataset_chennai_metro_station_activity.csv"
metro_data = pd.read_csv(file_paths)
metro_copy = metro_data.copy()

#Find the top 10 stations based on daily entries.
busiest_stations = metro_copy.sort_values('daily_entries',
    ascending=False
).head(10)

print(busiest_stations[['station_name', 'daily_entries']])
print(metro_copy.columns)

#Identify problem stations
problem_stations = metro_copy.loc[(metro_copy['monthly_complaints'] >20 ) & (metro_copy['avg_wait_minutes']> 3),
                          'station_name']
print(problem_stations)

zone_summary =(
    metro_copy.groupby('zone')
    .agg(
        number_of_stations = ('station_name','count'),
        average_entries = ('daily_entries','mean'),
        average_exits  = ( 'daily_exits','mean'),
        average_waiting_time = ('avg_wait_minutes','mean'),
        total_complaints = ('monthly_complaints','sum')

    )
)
print(zone_summary)