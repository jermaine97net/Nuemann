activate_file = 1

if activate_file:

    import sys
    sys.path.append("..")

    import time    
    import numpy as np
    from Functions.functions import*
    import random
    import matplotlib.pyplot as plt
    import pandas as pd

    start_time = time.perf_counter() 
    # region code
    tsla_distr = [191.94791279328174, 192.35000610351562, 192.7520994137495]
    pos_prob = 0.4631578947368421
    is_static = 1
    static_val = 0.5
    prob_range =  [static_val,static_val] if is_static else [1 - pos_prob, pos_prob]
    pos_range = [0.011086203835227272, 0.06890036843039773]
    neg_range = [-0.06947049907609529, -0.010516073189529719]

    first_val = 194.32000732421875
    events = 300
    num_sub = 10
    main_arr = []
    sub_arr=[]
    # endregion code

    #region code
    def random_func():
        return random.uniform(*pos_range) if random.random() <= random.uniform(*prob_range) else random.uniform(*neg_range)

    is_subparted = True
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
    
    run_code = 0
    if run_code:
        tendenancy = cent_tend_func(gen_forecasts())
        print(f' Central tendency is {tendenancy}')

    read_write = 1
    with open('asset_02.txt', 'r' if read_write == 1 else ' w') as file:
        read_to_data = list(map(lambda x: float(x),file.readlines()))
        write_to_file = file.write('\n'.join(str(val) for val in gen_forecasts()))
        read_to_data if read_write ==1 else write_to_file if read_write == 0 else None
        file.close()

    tsla_data = pd.DataFrame(read_to_data).T if read_write == 1 else print('File is not read.')
    tsla_cast = pd.DataFrame(gen_forecasts()).T

    for _ in range(3):
        plt.axhline(y=tsla_distr[_], color='green',label='TSLA Distribution') 
    plt.axhline(y=first_val, color='blue',label='First Value')

    plt.plot(pd.DataFrame(tsla_data).T, color='blue')
    plt.plot(pd.DataFrame(tsla_cast).T, color='grey')

    plt.legend()
    plt.show()

    # endregion code            
    
    total_time = time.perf_counter() - start_time

    print(f'Total process of {events*num_sub} iterations is: {total_time:0.4f} seconds')

else:
    print('The file is not activated for running.')



