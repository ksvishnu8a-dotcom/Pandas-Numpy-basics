import pandas as pd

f_path = r"C:\Users\A\Desktop\vk\challenge_dataset_chennai_metro_station_activity.csv"
metro_data = pd.read_csv(f_path)

fst5_row = metro_data.head()
num_rows_cols = metro_data.shape
cols_names = metro_data.columns
data_typ = metro_data.dtypes
msng_val = metro_data.isnull().sum()
bsc_stati = metro_data.describe()

highest_entry = metro_data.loc[
    metro_data['daily_entries'].idxmax()], ['station_name', 'daily_entries']
lowest_entry = metro_data.loc[
    metro_data['daily_entries'].idxmin()], ['station_name','daily_entries']
avg_entry = metro_data['daily_entries'].mean()
avg_etry_zone = metro_data.groupby('zone')['daily_entries'].mean()
stan_count = metro_data['station_type'].value_counts()
peak_load = metro_data.loc[
    metro_data['peak_hour_load_pct'] > 70,
    ['station_name','peak_hour_load_pct']
]
sort_station = metro_data.sort_values(
    'daily_entries',
    ascending=False) [['station_name','daily_entries']]
mst_cmplnts = metro_data.sort_values(
    'monthly_complaints',
    ascending=False) [['station_name','monthly_complaints']].head(5)

print(fst5_row)
print(num_rows_cols)
print(cols_names)
print(data_typ)
print(msng_val)
print(bsc_stati)
print(highest_entry)
print(lowest_entry)
print(f"average entry \t :{avg_entry}")
print(avg_etry_zone)
print(stan_count)
print(peak_load)
print(sort_station)
print(mst_cmplnts)