import pandas as pd


url = 'https://ml-repository-krakers.s3-eu-west-1.amazonaws.com/kaggle+/churn_modelling/Telco-Customer-Churn.csv'
df = pd.read_csv(url, index_col=0)

df['Churn'] = df['Churn'].map({'Yes':1, 'No':0})
print(df['Churn'].head())
