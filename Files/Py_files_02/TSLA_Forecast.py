activate_file = 1

if activate_file:

    import sys
    sys.path.append("..")
    import time    
    import numpy as np
    from Py_files_01.Class_Function import *
    from Py_files_02.TSL_array import tsla_data
    import random
    import matplotlib.pyplot as plt
    import pandas as pd

    start_index = 200
    end_index = 390

    data = tsla_data[start_index:end_index]
    	
    first_val = data[0]
    events = end_index - start_index
    number_sub = 100
    
    pos_change_dist = change_distribution(data,1,1,'distr')[0]
    pos_change_range = [pos_change_dist[0], pos_change_dist[-1]]
    neg_change_range = change_distribution(data,1,-1,'distr')[0]
    neg_change_range = [neg_change_range[0], neg_change_range[-1]]

    data_distribution = distribution_func(data,1,'distr')[0]

    pos_prob = change_prob(data,1)

    print('f The pos change probability from {start_index} to {end_index} is : {pos_prob} \n')
    print(f'The positive change range is: {pos_change_range}')
    print(f'The negative change range is: {neg_change_range}')
    print(f'The distribution of the data is: {data_distribution} \n')


    # region forceast generation
    dynamic_modulator, defualt_pos_prob , = 0.01, 0.5

    is_dynamic, is_default = 0, 0
    if is_dynamic:
        if is_default == False:
            pos_prob_range = (pos_prob - dynamic_modulator, pos_prob + dynamic_modulator) 
        else: pos_change_range = (defualt_pos_prob + dynamic_modulator, defualt_pos_prob + dynamic_modulator)
    else:
        pos_prob_range = (pos_prob, pos_prob) if is_default == False else (defualt_pos_prob, defualt_pos_prob)
    
    def rand_gen():
        return random.uniform(*pos_change_range) if random.random() <= random.uniform(*pos_prob_range) else random.uniform(*neg_change_range)
    # endregion
    

    # region forecasts analysis
    forecasts = pd.DataFrame(gen_forecasts(rand_gen,first_val, events, number_sub, True))
    forecast_func = lambda data: distribution_func(data,1, 'distr')[0]
    applied_forecasts = forecasts.apply(forecast_func, axis=0)
    print(f'The distribution of the forecasts is: {applied_forecasts} \n')

    data_function = lambda data: distribution_func(data,1, 'distr')[0]
    applied_data = forecasts.apply(data_function, axis=0)
    # endregion


    # region plot
    start_x = start_index + 1
    x = np.arange(start_x, start_x + len(data))

    # Plot forecasts
    plt.plot(x,forecasts.T, color = 'grey')
    plt.plot(x,applied_data.T, color = 'blue')

    # Plot data
    plt.plot(np.array(tsla_data), color = 'green')
    for val in data_distribution:
        plt.hlines(y=val, xmin=start_x, xmax=start_x + len(data), color='red')

    # endregion
    plt.show()
