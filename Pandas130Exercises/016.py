import numpy as np
import pandas as pd


np.random.seed(42)
data_dict = {
    'normal': np.random.normal(loc=0, scale=1, size=1000),
    'uniform': np.random.uniform(low=0, high=1, size=1000),
    'binomial': np.random.binomial(n=1, p=0.2, size=1000)
}

df = pd.DataFrame(data=data_dict, index=pd.date_range('2020-01-01', periods=1000))

print(df.head(10))
print()
print(df.tail())