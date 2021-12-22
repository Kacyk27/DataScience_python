import numpy as np
import pandas as pd


np.random.seed(42)
df = pd.DataFrame(np.random.rand(10, 4), columns=list('ABCD'))
df['B'].iloc[3] = np.nan
df.loc[8,"D"] = np.nan
print(df)