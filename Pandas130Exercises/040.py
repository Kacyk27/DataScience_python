import pandas as pd
import numpy as np


np.random.seed(42)

url = 'https://ml-repository-krakers.s3-eu-west-1.amazonaws.com/kaggle+/churn_modelling/Telco-Customer-Churn.csv'
df = pd.read_csv(url, index_col=0)

x = df.sample(n=10)
x.to_csv('sample_10.csv')