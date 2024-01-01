import random
import yfinance as fin
import numpy as np
run_read = 0

if run_read:
    file_name = 'data.txt'
    with open(file_name, 'r') as file:
        data = [float(line.strip()) for line in file.read().split()]

data = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
first_val=0
events=4
num_forecats=3

pos_prob = 0.6
neg_prob = 1 - pos_prob

prob = [neg_prob, pos_prob]

pos_distr = [0.5, 1.5]
neg_distr = [-1.5, -0.5]

def rand():
  return random.uniform(*pos_distr) if random.random()>= random.uniform(*prob) else random.uniform(*neg_distr)

arr = []
val_2=[]
first_val=0
for i in range(events):
    arr.append(rand())
    val_2.append(first_val+sum(arr[:i+1]))
    print(f'## arr {arr}')
    print(val_2)
# print(f'val_2 {val_2}')
# print(forecasts)

# print(sum_arr)
# print(result)
# print(result_2)
# print(len(forecasts))