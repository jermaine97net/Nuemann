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

    start_index = 0
    end_index = 250

    data_analysis = tsla_data[start_index:end_index]
    	
    pos_change_dist = change_distribution(data_analysis,1,1,'distr')[0]
    pos_change_range = [pos_change_dist[0], pos_change_dist[-1]]
    neg_change_range = change_distribution(data_analysis,1,-1,'distr')[0]
    neg_change_range = [neg_change_range[0], neg_change_range[-1]]

    data_analysis_distribution = distribution_func(data_analysis,1,'distr')[0]

    pos_prob = change_prob(data_analysis,1)

    print(f' The pos change probability of data_analysis({start_index},{end_index}) is : {pos_prob}')
    print(f'The positive change range is: {pos_change_range}')
    print(f'The negative change range is: {neg_change_range}')
    print(f'The distribution of data_analysis({start_index},{end_index}) is: {data_analysis_distribution} \n')


    # region forceast generation
    forecast_start = end_index
    first_val = tsla_data[end_index]

    events = len(tsla_data) - forecast_start
    number_sub = 100
  
    dynamic_modulator, defualt_pos_prob , = 0.1, 0.5
    is_dynamic, is_default = 0, 1

    if is_dynamic:
        if is_default == False:
            pos_prob_range = (pos_prob - dynamic_modulator, pos_prob + dynamic_modulator) 
        else: pos_prob_range = (defualt_pos_prob + dynamic_modulator, defualt_pos_prob + dynamic_modulator)
    else:
        pos_prob_range = (pos_prob, pos_prob) if is_default == False else (defualt_pos_prob, defualt_pos_prob)
    
    def rand_gen():
        return random.uniform(*pos_change_range) if random.random() <= random.uniform(*pos_prob_range) else random.uniform(*neg_change_range)
    # endregion
    

   
