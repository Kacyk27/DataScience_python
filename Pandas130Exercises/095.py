import pandas as pd


pd.set_option('max_columns', 15)
pd.set_option('display.width', 150)
url = 'https://storage.googleapis.com/esmartdata-courses-files/ml-course/insurance.csv'
df = pd.read_csv(url)
for col in list(df.select_dtypes(include=['object']).columns):
    df[col] = df[col].astype('category')
    
df_dummies = pd.get_dummies(df, drop_first=True)
print(df_dummies.head())