import pandas as pd
import random
import numpy as np
import itertools
import random

number = 28
data = np.array(range(10))
indices = np.concatenate(np.where((data > 5) & (data < 9)))
print(indices)
indices = itertools.filterfalse(lambda x: x + number > len(data) - 1, indices)
print(list(indices))


# for val in indices:
#     if val == len(data) - 1:  # Check if val is the last index
#         continue
#     print((data[val],data[val+number]))

# data_2  = ((1,2),(3,4),(5,6),(7,8))

# mapped = itertools.starmap(lambda x,y: x + y, data_2)
# # map_2 = map(lambda x,y: x+y, data_2)

# print(list(mapped))
# # print(list(map_2))