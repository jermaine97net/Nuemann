import numpy as np

# List of all functions:
# - diff_func(a, b, _abs_)
# - sqr_dev_func(val, data)
# - std_dev_func(val, data)
# - abs_dev_func(val, data)
# - cent_tend_func(function, data)
# - abv_bel_func(val, data, type, is_equal)
# - dist_func(val,func_,data)

def find_file(filename):
    import subprocess
    command = f"find / -name {filename}"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()

    if process.returncode != 0:
        print(f"Error occurred: {error.decode().strip()}")
    else:
        print(f"Output: {output.decode().strip()}")
        
    return output.decode().strip()

def diff_func(a, b):
    """
    Get the difference between two values.
    Parameters:
    - a (int): First value.
    - b (int): Second value.
    """   
    return a - b

def sqr_dev_func(val, data):
    """
    Get the mean square deviation of a value from a list of values.
    Parameters:
    - val (int): Value to compare with.
    - data (list): List of values to compare with.
    """
    return np.mean([np.square(val - i) for i in data]) 

def std_dev_func(val, data):
    """
    Get the standard deviation of a value from a list of values.
    Parameters:
    - val (int): Value to compare with.
    - data (list): List of values to compare with.
    """
    return np.sqrt(sqr_dev_func(val, data))

def abs_dev_func(val, data):
    """
    Get the mean absolute deviation of a value from a list of values.
    Parameters:
    - val (int): Value to compare with.
    - data (list): List of values to compare with.
    """
    return np.mean([np.abs(val - i) for i in data])

def cent_tend_func(data):
    tend_arr=[]
    sum_arr=[sum([abs(i-j) for j in data]) for i in data]
    for i in range(len(data)):
        if sum_arr[i] == min(sum_arr):
            tend_arr.append(data[i])
    return tend_arr[0] if len(tend_arr) < 2 else tend_arr

def abv_bel_func(val, data, type, is_equal):
    """
    Get values above or below a value from a list of values.
    Parameters:
    - val (int): Value to compare with.
    - data (list): List of values to compare with.
    - type (int): Type of comparison (1 for above, -1 for below, 0 for all).
    - is_equal (bool): Whether to include the value or not.
    """
    if type == 1:
        return [i for i in data if i >= val] if is_equal else [i for i in data if i > val]    
    elif type == -1:
        return [i for i in data if i <= val] if is_equal else [i for i in data if i < val]
    elif type == 0:
        return [i for i in data if (i == val)] if is_equal else [i for i in data if i != val]

def distr_func(val,func_,data):
    return [val-func_(val,data),val,val+func_(val,data)]

# data=[[1,2],[3,4]]
# data=np.concatenate(data)

# print(cent_tend_func(abs_dev_func,data))

data=[2,3,4,5,6,7,8,9,20]

v=np.std(data)
v2=abs_dev_func(np.mean(data),data)
v3=cent_tend_func(data)

print(v)
print(v2)
print(v3)