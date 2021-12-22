import pandas as pd


google = pd.read_csv('google.csv')
print(google.info())
print()
print(google.describe())