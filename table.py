import pandas as pd

file_paths = r"C:\Users\A\Desktop\vk\challenge_dataset_chennai_metro_station_activity.csv"
metro_data = pd.read_csv(file_paths)
metro_copy = metro_data.copy()

final_table = metro_copy[
    ['station_name',
     'zone',
     'daily_entries',
     'avg_wait_minutes',
     'monthly_complaints',
     'has_parking'

    ]
]
print(final_table)

#identify stations that appear to need the most attention, based on a combination of:

# high daily entries
# high waiting time
# high complaints
#columns have different scales, first rank each one. Higher values get a higher rank:
attention = metro_copy.copy()

attention['entries_rank'] = attention['daily_entries'].rank(
    ascending=True
)
attention['waiting_rank'] = attention['avg_wait_minutes'].rank(
    ascending=True
)
attention['complaints_rank'] = attention['monthly_complaints'].rank(
    ascending=True
)

#combine these ranks
attention['attention_score'] =(
    attention['entries_rank'] +
    attention['waiting_rank'] +
    attention['complaints_rank']
)

most_attention = (
    attention.sort_values('attention_score',ascending=False)
    .head(10)
)
print()
print(
    most_attention[
        [
            'station_name',
            'zone',
            'daily_entries',
            'avg_wait_minutes',
            'monthly_complaints',
            'attention_score'
        ]
    ]
)


# we sorts and ranks each columns then we take the best ranks and sum it all up and get a score
#if the score is high it gets printed 1st

# Original data
#      ↓
# Copy the data
#      ↓
# Rank stations by daily entries
#      ↓
# Rank stations by waiting time
#      ↓
# Rank stations by complaints
#      ↓
# Add the 3 ranks together
#      ↓
# Sort by the combined score
#      ↓
# Take the top 10