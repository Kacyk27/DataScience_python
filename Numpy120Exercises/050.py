import numpy as np


image = np.random.randint(low=0, high=256, size=(10, 10, 3), dtype=np.uint8)

result = image[:5,:5,:3]
