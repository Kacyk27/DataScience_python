import pandas as pd


url = 'https://storage.googleapis.com/esmartdata-courses-files/ml-course/insurance.csv'
df = pd.read_csv(url)
for col in list(df.select_dtypes(include=['object']).columns):
    df[col] = df[col].astype('category')
df_num = df.select_dtypes(include=['float', 'int']).copy()

print(df_num.describe())