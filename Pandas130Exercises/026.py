import pandas as pd


google = pd.read_csv('google.csv', index_col=0)
google = google.reset_index()

idx_min = google['Close'].argmin()
print(google.iloc[[idx_min]])