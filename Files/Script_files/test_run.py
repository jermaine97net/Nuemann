import pandas as pd
import random
import numpy as np

data = ((5,6,7,8),(3,4))
dif = np.diff(data, n=1)

arr = [[val[0],val[-1]] for val in data]
print(arr)
