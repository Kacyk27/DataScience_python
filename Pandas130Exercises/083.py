import pandas as pd
import numpy as np


pd.set_option('max_columns', 15)
pd.set_option('display.width', 150)
url = 'https://storage.googleapis.com/esmartdata-courses-files/ds-bootcamp/london_bike.csv'
df = pd.read_csv(url)
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['hour'] = df['timestamp'].dt.hour
df_weekend = df.query("is_weekend == 1.0").copy()

df.to_csv('weekend.txt', index=False)