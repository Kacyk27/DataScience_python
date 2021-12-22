import pandas as pd


google = pd.read_csv('google.csv', index_col=0)

google.columns = ["O",'H','L','C','V']
print(google)