import pandas as pd

metro_file_path =r'C:\Users\A\Desktop\vk\challenge_dataset_chennai_metro_station_activity.csv'
metro_data = pd.read_csv(metro_file_path)
print(metro_data.head()) # for printing 5 rows .head(3) gives 3 rows
print(metro_data.count()) #count non null values in eah column
print(metro_data.columns)
print(metro_data.dtypes)

print(metro_data.shape) # gives number rows, cols
print(metro_data.isnull().sum()) #find missing values per rows
print(f"total missing values {metro_data.isnull().sum().sum()}")
print(metro_data.describe()) # Generate basic statistics
