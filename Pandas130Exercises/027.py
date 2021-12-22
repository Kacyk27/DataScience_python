import pandas as pd


google = pd.read_csv('google.csv', index_col=0)
google = google.reset_index()

google = google.iloc[:,[0,1,4,5]]

print(google)