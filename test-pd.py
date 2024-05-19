import pandas as pd

data = {'calories': [420, 380, 390], 'duration': [50, 40, 45]}

df = pd.DataFrame(data, index=['day1', 'day2', 'day3'])

for i, row in df.iterrows():
    # print(row['calories'], row['duration'])
    print(row.to_dict())
