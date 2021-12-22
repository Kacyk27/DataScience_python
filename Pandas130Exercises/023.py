import pandas as pd


google = pd.read_csv('google.csv', index_col=0)
print(google.reset_index())


