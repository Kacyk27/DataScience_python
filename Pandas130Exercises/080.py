import pandas as pd


pd.set_option('max_columns', 15)
pd.set_option('display.width', 150)
url = 'https://storage.googleapis.com/esmartdata-courses-files/ds-bootcamp/london_bike.csv'
df = pd.read_csv(url)
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['hour'] = df['timestamp'].dt.hour

cnt_by_weekend_hour = df.groupby(['is_weekend','hour'])['cnt'].mean().reset_index()

print(cnt_by_weekend_hour)