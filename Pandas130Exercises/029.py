import pandas as pd


google = pd.read_csv('google.csv')
google['Date'] = pd.to_datetime(google['Date'])
google['Year'] = google['Date'].dt.year
google['Month'] = google['Date'].dt.month


del google["Year"]
del google['Month']
print(google)

