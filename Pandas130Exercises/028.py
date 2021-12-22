import pandas as pd


google = pd.read_csv('google.csv')

google = google.set_index('Date')

