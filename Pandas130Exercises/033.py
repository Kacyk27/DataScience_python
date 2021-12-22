import pandas as pd


url = 'https://ml-repository-krakers.s3-eu-west-1.amazonaws.com/kaggle+/churn_modelling/Telco-Customer-Churn.csv'
df = pd.read_csv(url)

median = df['TotalCharges'][df['TotalCharges']!=' '].median()
df.loc[df['TotalCharges'] == ' ', 'TotalCharges'] = median
df['TotalCharges'] = df['TotalCharges'].astype('float')

print(df['TotalCharges'].value_counts())