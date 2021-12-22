import pandas as pd


google = pd.read_csv('google.csv', index_col=0)
google = google.reset_index()
google['Date'] = pd.to_datetime(google['Date'])

google['Year'] = google['Date'].dt.year
google['Month'] = google['Date'].dt.month