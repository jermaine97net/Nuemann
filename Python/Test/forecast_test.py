import random
import yfinance as fin
import numpy as np
run_read = 0

# if run_read:
#     file_name = 'data.txt'
#     with open(file_name, 'r') as file:
#         data = [float(line.strip()) for line in file.read().split()]

# data = [1, 2, 3, 4, 5, 6, 7, 8, 9,]

# events=2
# num_forecats=3

# pos_prob = 0.6
# neg_prob = 1 - pos_prob

# prob = [neg_prob, pos_prob]

# pos_distr = [0.5, 1.5]
# neg_distr = [-1.5, -0.5]

# def rand():
#   return random.uniform(*pos_distr) if random.random()>= random.uniform(*prob) else random.uniform(*neg_distr)

result=[]
sum_arr=[]
events=10

for i in range(events):
    result.append(sum_arr.append(i))
    
result_2=[[1+i for i in range(i+1)] for i in range(events)]

# print(sum_arr)
print(result)
print(result_2)
# print(len(forecasts))