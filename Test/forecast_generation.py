import sys
sys.path.append("..")
import random
import numpy as np
import timeit
import time
import subprocess
from Functions.functions import distr_func, abs_dev_func, std_dev_func

# import matplotlib.pyplot as plt 

pos_prob = 0.6
prob_range = [1 - pos_prob, pos_prob]
pos_range = [0.1, 0.5]
neg_range = [-0.1, -0.5]

first_val = 5
events = 300
num_sub = 10000
main_arr = []
sub_arr=[]

def random_func():
    return random.uniform(*pos_range) if random.random() >= random.uniform(*prob_range) else random.uniform(*neg_range)

is_subparted=True
def gen_forecasts():
    for i in range(num_sub*events):
        if np.mod(i, events) == 0  or i == 0:
            main_arr.append(first_val)
            if is_subparted and i != 0 :
                sub_arr.append(main_arr[i-events:i])  
        else:
            main_arr.append(main_arr[-1] + random_func())
        if is_subparted and i == num_sub*events-1:
            sub_arr.append(main_arr[i+1-events:i+1])
    return sub_arr if is_subparted else main_arr

data_distribution = distr_func(np.mean(gen_forecasts()), std_dev_func,gen_forecasts())
print(data_distribution)

run_write=False
if run_write:
    with open('sub_forecast_data.txt', 'r') as file:
        file.write('\n'.join(str(val) for val in gen_forecasts()))







