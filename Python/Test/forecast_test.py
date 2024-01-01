import random
import yfinance as fin
run_read = 0

if run_read:
    file_name = 'data.txt'
    with open(file_name, 'r') as file:
        data = [float(line.strip()) for line in file.read().split()]

data = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
forecasts=[]

events=2
num_forecats=3

pos_prob = 0.6
neg_prob = 1 - pos_prob

prob = [neg_prob, pos_prob]

pos_distr = [0.5, 1.5]
neg_distr = [-1.5, -0.5]

def rand():
  return random.uniform(*pos_distr) if random.random()>= random.uniform(*prob) else random.uniform(*neg_distr)

for val in range(num_forecats):
  forecasts.append([data[0]+sum([rand() for i in range(i)]) for i in range(events)])

print(forecasts)
print(len(forecasts))