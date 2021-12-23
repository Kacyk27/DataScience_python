import pandas as pd


url = 'https://storage.googleapis.com/esmartdata-courses-files/ml-course/insurance.csv'

df = pd.read_csv(url)
print(df.head())