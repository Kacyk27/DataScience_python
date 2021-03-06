import numpy as np
import pandas as pd


np.random.seed(42)
s1 = pd.Series(np.random.rand(20))
s2 = pd.Series(np.random.randn(20))

df = pd.concat([s1, s2], axis=1)
df.columns = ['col1', 'col2']

df['col3'] = df['col2'].map(lambda x: -1 if x< 0 else 1)
print(df)