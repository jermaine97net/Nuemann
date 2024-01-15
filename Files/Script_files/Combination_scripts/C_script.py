import itertools
import time
import numpy as np

iterable = 10000
data = range(iterable)

start_time = time.time()  # Start timing
comb_2 = itertools.combinations(data, 2)
result = tuple(comb[0]+comb[-1] for comb in comb_2)
end_time = time.time()  # End timing

elapsed_time = end_time - start_time  # Calculate elapsed time
print(f"The process took {elapsed_time} seconds.")

