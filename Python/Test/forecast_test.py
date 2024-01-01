import random

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
num_forecasts = 10
first_val = 0

def forecast():
    forecast_ = [first_val]
    rand = lambda: random.uniform(*pos_distr) if random.random() <= random.uniform(*prob) else random.uniform(*neg_distr)
    for _ in range(events):
        forecast_.append(forecast_[-1] + rand())
    return forecast_

from multiprocessing import Pool

def generate_forecasts(num_forecasts):
    with Pool() as p:
        forecasts = p.map(forecast, range(num_forecasts))
    return forecasts

forecasts = generate_forecasts(num_forecasts)

# print(f'forecasts {forecasts}')
# print(forecasts)

# print(sum_changes)
# print(result)
# print(result_2)
# print(len(forecasts))