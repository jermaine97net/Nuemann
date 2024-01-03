import sys
sys.path.append("..")
import numpy as np
import random
from Functions.functions import *
from Functions.modify_array import *
# import matplotlib.pyplot as plt

# List of all functions:
# - diff_func(a, b, _abs_)
# - sqr_dev_func(val, data)
# - std_dev_func(val, data)
# - abs_dev_func(val, data)
# - cent_tend_func(function, data)
# - abv_bel_func(val, data, type, is_equal)
# - dist_func(val,func_,data)

run_random_write = 0

if run_random_write:
    range_rand = [1, 3]
    random = np.random.uniform(*range_rand, 20)

run_code=0
if run_code==True:
    with open('asset_02.txt', 'w+' if run_random_write else 'r') as file:
        file.write(str(random)) if run_random_write else None
        file.seek(0)
        from_, to_= 0 , None
        data = [float(num) for num in file.read().strip()[from_:to_].split()]

# region
data_2 = mod_array(data, 'rec', 0, len(data), 'group_num', 2)

data_tend=cent_tend_func(abs_dev_func,data)
data_distribution = distr_func(data_tend,abs_dev_func,data)

difference = [diff_func(sub[-1], sub[0]) for sub in data_2]
pos_change_data = abv_bel_func(0, difference, 1, False)
neg_change_data = abv_bel_func(0, difference, -1, False)

pos_prob = len(pos_change_data) / len((abv_bel_func(0, difference, 0, False)))
neg_prob = len(neg_change_data) / len((abv_bel_func(0, difference, 0, False)))

pos_tend = cent_tend_func(abs_dev_func, pos_change_data)
neg_tend = cent_tend_func(abs_dev_func, neg_change_data)

pos_tend_dev = abs_dev_func(pos_tend, pos_change_data)
neg_tend_dev = abs_dev_func(neg_tend, neg_change_data)

pos_distribution = distr_func(pos_tend,abs_dev_func,pos_change_data)
neg_distribution = distr_func(neg_tend,abs_dev_func,neg_change_data)

variables = {'difference': difference, 'pos_change_data': pos_change_data, 'neg_change_data': neg_change_data,
            'data distribution': data_distribution, 'pos_prob': pos_prob, 'neg_prob': neg_prob, 'pos_tend': pos_tend, 'neg_tend': neg_tend,
             'pos_tend_dev': pos_tend_dev, 'neg_tend_dev': neg_tend_dev,
             'pos_distribution': pos_distribution, 'neg_distribution': neg_distribution}

# endregion
for name, value in list(variables.items())[3:]:
    print(f'The {name} is {value}')

# plt.plot(data)
# plt.show()