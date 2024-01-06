import time
import timeit
import numpy as np


data = range(9000)

start_time_2_1 = timeit.default_timer()
arr_3 = np.array([sum(abs(i - j) for i in data) for j in data])
min_indices = np.where(arr_3 == np.min(arr_3))
min_data = [data[i] for i in min_indices[0]]
total_time_1 = timeit.default_timer() - start_time_2_1

start_time_2 = timeit.default_timer()
min_val, min_data = [float('inf')], []
for value in data:
    diff_sum = sum(abs(value-j) for j in data)
    if diff_sum < min_val[-1]:
        min_val = [diff_sum] 
        min_data = [value]
    elif diff_sum == min_val[-1]:
        min_val.append(diff_sum)
        min_data.append(value)
total_time_2 = timeit.default_timer() - start_time_2

print(f'total_time_1: {total_time_1} and total_time_2: {total_time_2}')


(15, 11, 9, 9, 11, 15)        
# print(min_val) 
# print(min_data)



