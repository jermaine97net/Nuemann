activate_file = 0

if activate_file:  
    import sys
    sys.path.append("..")

    from Functions.functions import cent_tend_func
    import pandas as pd
    import time

    start_time = time.perf_counter()
    #region code
    pd.set_option('display.max_rows', None)
    pd.reset_option('display.max_rows')

    file = open('sub_forecast_data.txt','r')
    data = list(map(lambda x: float(x),file.readlines()))

    # pd.set_option('display.max_rows', None)
    # display.display(data)
    # pd.reset_option('display.max_rows')

    tend = cent_tend_func(data)
    print(tend)
    #endregion code
    total_time = time.perf_counter() - start_time

    print(f'Total process of {len(data)} file read iterations is: {total_time} seconds')