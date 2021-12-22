import numpy as np
import pandas as pd


url = 'https://storage.googleapis.com/esmartdata-courses-files/dash-course/data.csv'
df = pd.read_csv(url, index_col=0)
df.columns = [col.lower() for col in df.columns]
df['power'] = np.where(df['power'] == 'null bhp', np.nan, df['power'])
print(df['power'].value_counts()[:5])
