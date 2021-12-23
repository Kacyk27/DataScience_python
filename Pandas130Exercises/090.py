import pandas as pd


url = 'https://storage.googleapis.com/esmartdata-courses-files/ml-course/insurance.csv'
df = pd.read_csv(url)
for col in list(df.select_dtypes(include=['object']).columns):
    df[col] = df[col].astype('category')
    
df_cat = df[df.select_dtypes(include=['category']).columns].copy()
df_num = df[df.select_dtypes(include=['float','int']).columns].copy()
print(df_cat.head())
print(df_num.head())