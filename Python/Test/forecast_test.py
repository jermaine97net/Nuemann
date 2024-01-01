import random

run_read = 0

if run_read:
    file_name = 'data.txt'
    with open(file_name, 'r') as file:
        data = [float(line.strip()) for line in file.read().split()]

data = [1, 2, 3, 4, 5, 6, 7, 8, 9,]

events=20

forecast_ = data[0]
pos_prob = 0.6
neg_prob = 1 - pos_prob

prob = [neg_prob, pos_prob]

pos_distr = [0.5, 1.5]
neg_distr = [-1.5, -0.5]

\
  rand = lambda : random.uniform(*pos_distr) if random.random()>= random.uniform(*prob) else random.uniform(*neg_distr)
print(rand)
[rand() for i in range(events)]

