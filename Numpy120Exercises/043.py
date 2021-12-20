import numpy as np


image = np.random.randint(low=0, high=256, size=(200, 300, 3), dtype=np.uint8)

image_extended = np.expand_dims(image,axis=0)

