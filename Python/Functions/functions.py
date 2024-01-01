import numpy as np

# List of all functions:
# - diff(a, b, _abs_)
# - sqr_dev(val, data)
# - std_dev(val, data)
# - abs_dev(val, data)
# - central_ten(function, data)
# - abv_bel(val, data, type, is_equal)


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

def diff(a, b):
    """
    Get the difference between two values.
    Parameters:
    - a (int): First value.
    - b (int): Second value.
    """   
    return a - b

def sqr_dev(val, data):
    """
    Get the mean square deviation of a value from a list of values.
    Parameters:
    - val (int): Value to compare with.
    - data (list): List of values to compare with.
    """
    return np.mean([np.square(val - i) for i in data]) 

def std_dev(val, data):
    """
    Get the standard deviation of a value from a list of values.
    Parameters:
    - val (int): Value to compare with.
    - data (list): List of values to compare with.
    """
    return np.sqrt(sqr_dev(val, data))

def abs_dev(val, data):
    """
    Get the mean absolute deviation of a value from a list of values.
    Parameters:
    - val (int): Value to compare with.
    - data (list): List of values to compare with.
    """
    return np.mean([np.abs(val - i) for i in data])

def central_ten(function, data):
    """
    Get the central tendency of a list of values, 
    function can be absolute deviation, sqaure deviation, standard deviation.
    Parameters:
    - function (function): Function to use for the central tendency.
    - data (list): List of values to compare with.
    """
    array = [function(i, data) for i in data]
    return data[array.index(min(array))]

def abv_bel(val, data, type, is_equal):
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


