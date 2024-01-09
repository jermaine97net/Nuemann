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
    

    # region forecasts analysis
    forecasts = gen_forecasts(rand_gen,first_val, events, number_sub, True)

    analysis_type, dev_type, axis_val = 'tend', 1, 0
    is_static_analysis = 1
    conditional_data = np.concatenate(forecasts) if is_static_analysis else pd.DataFrame(forecasts)

    dynamic_func = lambda data_analysis: distribution_func(data_analysis,dev_type, analysis_type)
    static_func = distribution_func(conditional_data,dev_type,analysis_type)

    if is_static_analysis:
        forecast_analysis = static_func[0] if analysis_type == 'distr' else static_func
    else: conditional_data.apply(dynamic_func, axis=axis_val)[0] if analysis_type == 'distr' else conditional_data.apply(dynamic_func, axis=axis_val)

    # endregion


    # region plot
        
    # Plot forecasts
    plot_forecast = 1
    if plot_forecast:
        start_x = forecast_start
        x = np.arange(start_x, start_x + events)
        plt.plot(x,forecasts.T, color = 'lightgrey', linestyle='--', linewidth = 0.5)
        # plt.plot(x, *forecast_moving_distribution, color = 'red', linewidth = 0.5)
        try:
            for val in forecast_distribution:
                plt.hlines(y=val, xmin=start_x, xmax=start_x + events, color='red',linestyle= '--', linewidth = 0.5)
        except ValueError:
                plt.hlines(y=forecast_distribution, xmin=start_x, xmax=start_x + events, color='red',linestyle= '--', linewidth = 0.5)
    
    # Plot data_analysis
    plot_data_analysis = 1
    if plot_data_analysis:
        plt.plot(np.array(tsla_data), color = 'green')
    # for val in data_analysis_distribution:
    #     plt.hlines(y=val, xmin=start_x, xmax=start_x + len(data_analysis), color='red')

    # endregion
   
