import numpy as np
import itertools

def mod_array(arr, combination_recursive, start_index=None, end_index=None, partition_type=None, partition_value=None):
    """
    Generate combinations or sub-arrays from a given array based on specified parameters.

    Parameters:
    - arr (list): The input array.
    - combination_recursive (str): Type of generation ('com' for combinations, 'rec' for recursive).
    - start_index (int, optional): Index to start the sub-array or combination. Default is None.
    - end_index (int, optional): Index to end the sub-array or combination. Default is None.
    - partition_type (str): Specify the partition type ('percentage', 'group_num', 'partition_num').
    - partition_value (int): Value depending on the value of partition_type.

    Returns:
    - result (list): List of generated combinations or sub-arrays, or None with an accompanying message.
    """
    try:
        if not isinstance(arr, list) or not arr:
            return None, "arr: Enter appropriate input (non-empty list)."
        if not isinstance(combination_recursive, str) or not combination_recursive:
            return None, "combination_recursive: Enter appropriate input (non-empty string)."
        if not isinstance(partition_type, str) or partition_type not in {'percentage', 'group_num', 'partition_num'}:
            return None, "partition_type: Enter appropriate input ('percentage', 'group_num', 'partition_num')."
        if partition_value is None or not isinstance(partition_value, (int, float)):
            return None, "partition_value: Enter appropriate input (numeric value)."

        arr = arr[start_index:end_index] if (start_index is not None and end_index is not None) else arr

        # Default values
        group_num, partition_percentage = 0, 0

        # Set values based on partition_type
        if partition_type == 'percentage':
            partition_percentage = partition_value if partition_value is not None else 30
        elif partition_type == 'group_num':
            group_num = partition_value if partition_value is not None else 2

        # Determine the size of each group
        if partition_type == 'percentage':
            n = int(np.floor(round((partition_percentage / 100) * len(arr), 0)))
        else:  # 'group_num', 'partition_num'
            n = group_num if partition_type == 'group_num' else int(np.floor(round(len(arr) / partition_value, 0))) if partition_value != 0 else 0

        #Generate combinations or sub-arrays based on the specified parameters
        result = [list(group) for group in itertools.combinations(arr, n)] if combination_recursive == 'com' else [arr[i:i + n] for i in range(0, len(arr) - n + 2, n - 1) if len(arr[i:i + n]) == n]
        return result
    except Exception as e:
        return str(e)

# # Example usage with partitioning
# real = [1,2,3,4,5,6,7,8,9,10]

# combination_recursive, start_index_value, end_index_value = 'rec', 0, len(real)
# partition_type, partition_value = 'group_num', 2

# brr= mod_array(real, combination_recursive, start_index_value, end_index_value, partition_type,partition_value)

# print(brr)