import numpy as np


votes = np.array(['yes', 'no', 'yes', 'no', np.nan, 'yes', 'yes'])

print(np.unique(votes,return_counts=True))