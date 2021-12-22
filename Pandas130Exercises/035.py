import pandas as pd


url = 'https://ml-repository-krakers.s3-eu-west-1.amazonaws.com/kaggle+/churn_modelling/Telco-Customer-Churn.csv'
df = pd.read_csv(url, index_col=0)
TotalChargesMedian = df['TotalCharges'][df['TotalCharges'] != ' '].median()
df.loc[df['TotalCharges'] == ' ', 'TotalCharges'] = TotalChargesMedian
df['TotalCharges'] = df['TotalCharges'].astype('float')

categorical = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines', 
               'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
               'StreamingTV', 'Contract', 'StreamingMovies', 'PaperlessBilling', 'PaymentMethod', 'Churn'] 

numerical = ['tenure', 'MonthlyCharges']

for col in categorical:
    df[col] = pd.Categorical(df[col]) 

for col in numerical:
    df[col] = df[col].astype(float)

print(df.describe(include='category'))