import numpy as np
import pandas as pd


np.random.seed(42)
df = pd.DataFrame(np.random.rand(10, 4), columns=list('ABCD'))

print(df[df['C']>0.8])


