import numpy as np


A = np.array([['PLW CDR 11B TEN', 'AMC LPP'],
              ['CDR PKO KGH', 'CCC QMK']], dtype=np.str)

print(np.char.split(A," "))