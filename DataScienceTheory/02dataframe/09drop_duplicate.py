import pandas as pd
import numpy as np

#%%
df = pd.DataFrame(np.random.randint(0,10,100))

df.drop_duplicates(inplace=True)
