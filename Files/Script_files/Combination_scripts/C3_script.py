import time
import numpy as np
import timeit

iterable = 10000
data = range(iterable)
data_2 =range(iterable -1)
results = []

start_time = time.time()  # Start timing
for i in data:
    result = tuple((i+j) for j in data if j > i)
    results.append(result)
end_time = time.time()  # End timing

elapsed_time = end_time - start_time  # Calculate elapsed time
print(f"The process took {elapsed_time} seconds.")
