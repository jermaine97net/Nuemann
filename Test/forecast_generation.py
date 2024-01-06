activate_file = 0

if activate_file:

    import sys
    sys.path.append("..")

    import time    
    import numpy as np
    from Functions.functions import*
    import random

    start_time = time.perf_counter() 
    # region code
    pos_prob = 0.6
    prob_range = [1 - pos_prob, pos_prob]
    pos_range = [0.1, 0.5]
    neg_range = [-0.1, -0.5]

    first_val = 5
    events = 150
    num_sub = 100
    main_arr = []
    sub_arr=[]
    # endregion code

    #region code
    def random_func():
        return random.uniform(*pos_range) if random.random() >= random.uniform(*prob_range) else random.uniform(*neg_range)

    is_subparted=False
    def gen_forecasts():
        for i in range(num_sub*events):
            if np.mod(i, events) == 0  or i == 0:
                main_arr.append(first_val)
                if is_subparted and i != 0 :
                    sub_arr.append(main_arr[i-events:i])  
            else:
                main_arr.append(main_arr[-1] + random_func())
            if is_subparted and i == num_sub*events-1:
                sub_arr.append(main_arr[i+1-events:i+1])
        return sub_arr if is_subparted else main_arr
    
    tendenancy = cent_tend_func(gen_forecasts())
    print(f' Central tendency is {tendenancy}')

    run_write = False
    if run_write:
        with open('sub_forecast_data.txt', 'w') as file:
            file.write('\n'.join(str(val) for val in gen_forecasts()))
    #endregion code            
    total_time = time.perf_counter() - start_time

    print(f'Total process of {events*num_sub} iterations is: {total_time:0.4f} seconds')

else:
    print('The file is not activated for running.')



