import sys
sys.path.append("..")
import numpy as np
import random
from Functions.functions import *
from Functions.modify_array import *

# List of all functions:
# - diff(a, b, _abs_)
# - sqr_dev(val, data)
# - std_dev(val, data)
# - abs_dev(val, data)
# - central_ten(function, data)
# - abv_bel(val, data, type, is_equal)

run_random_write = 0

if run_random_write:
    range_rand = [1, 3]
    random = np.random.uniform(*range_rand, 20)

with open('asset_02.txt', 'w+' if run_random_write else 'r') as file:
    file.write(str(random)) if run_random_write else None
    file.seek(0)
    from_, to_= 0 , None
    data = [float(num) for num in file.read().strip()[from_:to_].split()]

data_2 = mod_array(data, 'rec', 0, len(data), 'group_num', 2)

difference = [diff(sub[-1], sub[0]) for sub in data_2]
pos_change = abv_bel(0, difference, 1, False)
neg_change = abv_bel(0, difference, -1, False)

pos_prob = len(pos_change) / len((abv_bel(0, difference, 0, False)))
neg_prob = len(neg_change) / len((abv_bel(0, difference, 0, False)))

pos_tend = central_ten(abs_dev, pos_change)
neg_tend = central_ten(abs_dev, neg_change)

pos_tend_dev = abs_dev(pos_tend, pos_change)
neg_tend_dev = abs_dev(neg_tend, neg_change)

pos_distribution = [np.diff([pos_tend_dev, pos_tend]), pos_tend, sum([pos_tend, pos_tend_dev])]
neg_distribution = [np.diff([neg_tend_dev, neg_tend]), neg_tend, sum([neg_tend, neg_tend_dev])]

variables = {'difference': difference, 'pos_change': pos_change, 'neg_change': neg_change,
             'pos_prob': pos_prob, 'neg_prob': neg_prob, 'pos_tend': pos_tend, 'neg_tend': neg_tend,
             'pos_tend_dev': pos_tend_dev, 'neg_tend_dev': neg_tend_dev,
             'pos_distribution': pos_distribution, 'neg_distribution': neg_distribution}

for name, value in variables.items():
    print(f'The {name} is {value}')

