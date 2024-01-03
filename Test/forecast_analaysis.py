import sys
sys.path.append("..")
from Functions.functions import distr_func, abs_dev_func
import IPython.display as display
import pandas as pd
import numpy as np
pd.set_option('display.max_rows', None)
pd.reset_option('display.max_rows')

file = open('forecast_data.txt','r')

data = list(map(lambda x: float(x),file.readlines()))

# pd.set_option('display.max_rows', None)
# display.display(data)
# pd.reset_option('display.max_rows')

data_distr = distr_func(np.mean(data),abs_dev_func, data)
print(data_distr)