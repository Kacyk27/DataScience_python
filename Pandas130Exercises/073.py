import pandas as pd


url = 'https://storage.googleapis.com/esmartdata-courses-files/ds-bootcamp/london_bike.csv'

df = pd.read_csv(url, index_col=0)
df.info()