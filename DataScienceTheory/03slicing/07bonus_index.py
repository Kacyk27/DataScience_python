import pandas as pd
import numpy as np

#%%
idx = pd.Index(['8638','0643','0953','3246'])

df = pd.DataFrame(np.random.randn(4,5), index=idx, columns=list('abcde'))