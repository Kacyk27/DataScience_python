import pandas as pd


url = 'https://storage.googleapis.com/esmartdata-courses-files/ml-course/insurance.csv'
df = pd.read_csv(url)
x=[]
for col in df.columns:
    if df[col].dtype == 'float64' or df[col].dtype == 'int64':
        x.append(col)
print(x)