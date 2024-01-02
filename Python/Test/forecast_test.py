import sys
sys.path.append("..")
from Functions.functions import central_ten_func, abs_dev_func
import random
import pandas as pd
import time
import matplotlib.pyplot as plt
import IPython.display as display
import pandas as pd
import numpy as np

# Set the option to display all columns/rows
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

run_read = 0

if run_read:
    file_name = 'data.txt'
    with open(file_name, 'r') as file:
        data = [float(line.strip()) for line in file.read().split()]

#region
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

pos_prob = 0.6
neg_prob = 1 - pos_prob

prob = [neg_prob, pos_prob]

pos_distr = [0.5, 1.5]
neg_distr = [-1.5, -0.5]

events = 300
num_forecasts = 30
first_val = 0
#endregion

def forecast_func():
    array = [first_val]
    # Pre-calculate random values
    random_values = [random.uniform(*pos_distr) if random.random() <= random.uniform(*prob) else random.uniform(*neg_distr) for _ in range(events)]
    for rand in random_values:
        array.append(array[-1] + rand)
    return array

def generate_forecasts(num_forecasts):
    return [forecast_func() for _ in range(num_forecasts)]

# print(generate_forecasts(num_forecasts))
forecasts=generate_forecasts(num_forecasts)
forecasts_con=np.concatenate(generate_forecasts(num_forecasts))
# print(forecasts)
tendency_forecasts = central_ten_func(abs_dev_func,forecasts_con)
print(f'tendendancy {tendency_forecasts}')

# for data in forecasts:
#     plt.plot(data)
# plt.show()

get_data_frame=0
if get_data_frame:
    def generate_columns(events):
        return ['From value' if i==0 else f'Event {i}' for i in range(events+1)]
    def generate_rows(num_forecasts):
        return [f'Forecast {i+1}' for i in range(num_forecasts)]
    type_counter={'benchmark': time.perf_counter, 'CPU': time.process_time}
    choice='benchmark'
    Frame_forecasts = pd.DataFrame(generate_forecasts(num_forecasts),columns=generate_columns(events),index=generate_rows(num_forecasts))
    
    # print(Frame_forecasts)
    # tendency_forecasts = central_ten_func(abs_dev_func, Frame_forecasts)
    # print(f'tendendancy {tendency_forecasts}')

