import random
import yfinance as fin
import numpy as np

run_read = 0

if run_read:
  file_name = 'data.txt'
  with open(file_name, 'r') as file:
    data = [float(line.strip()) for line in file.read().split()]

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

pos_prob = 0.6
neg_prob = 1 - pos_prob

prob = [neg_prob, pos_prob]

pos_distr = [0.5, 1.5]
neg_distr = [-1.5, -0.5]

events = 4
num_forecasts = 3
first_val = 0

def forecast():
  forecast_ , changes = []
  def rand():
    return random.uniform(*pos_distr) if random.random() >= random.uniform(*prob) else random.uniform(*neg_distr)
  for i in range(events):
    changes.append(i)
    forecast_.append(first_val + sum(changes[:i+1]))
  return forecast_

# print(f'forecasts {forecasts}')
# print(forecasts)

# print(sum_changes)
# print(result)
# print(result_2)
# print(len(forecasts))