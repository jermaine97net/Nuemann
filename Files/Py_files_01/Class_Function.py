activate_file = 1

if activate_file:

    import itertools
    import numpy as np
    import random
   
    
    # region List of all functions:
    # - find_file(filename)
    # - sqr_dev_func(val, data)
    # - std_dev_func(val, data)
    # - abs_dev_func(val, data)
    # - distribution_func(data, deviation_type, return_type)
    # - diff_filter_func(val, data, type, is_equal)
    # - difference_generator(data,1)
    # - change_prob(data, diff_type)
    # - change_distribution(data, deviation_type, diff_type,return_type)
    # endregion
    
    class Functions:
        def __init__(self):
            pass
        
    # region created distribution_func
    # def distribution_func_1(data, deviation_type, return_type):   
    #     min_deviation = float('inf')
    #     tendency = []
    #     if deviation_type == 1 or deviation_type == 2 :
    #         for current_value in data:
    #             deviation_array = np.mean(tuple(abs(current_value - other_value)**deviation_type for other_value in data))**(1/deviation_type)
    #             if deviation_array < min_deviation:
    #                 min_deviation = deviation_array
    #                 tendency = [current_value]
    #             elif min_deviation == deviation_array and current_value != tendency[-1]:
    #                 tendency.append(current_value)

    #         if return_type == 'distr':
    #             return tuple(([val - min_deviation, val, val + min_deviation]) for val in tendency)
    #         elif return_type == 'conc distr':
    #             return [np.min(tendency) - min_deviation,np.mean(tendency),np.max(tendency) + min_deviation]
    #         else:
    #             return min_deviation if return_type == 'dev' else tendency if return_type == 'tend' else [min_deviation, tendency]
    #     else: 
    #         return 'Type 1 for absolute deviation or 2 for standard deviation'
    #endregion

    def find_file(filename):
        """
        Find a file with the given filename in the system.

        Args:
            filename (str): The name of the file to search for.

        Returns:
            str: The path of the found file.

        """
        import subprocess
        command = f"find / -name {filename}"
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()

        if process.returncode != 0:
            print(f"Error occurred: {error.decode().strip()}")
        else:
            print(f"Output: {output.decode().strip()}")

        return output.decode().strip()


    def sqr_dev_func(val, data):
        """
        Calculate the mean square deviation of a value from a list of values.

        Args:
            val (int): The value to compare with.
            data (list): The list of values to compare with.

        Returns:
            float: The mean square deviation.

        """
        return np.mean([np.square(val - i) for i in data])


    def std_dev_func(val, data):
        """
        Calculate the standard deviation of a value from a list of values.

        Args:
            val (int): The value to compare with.
            data (list): The list of values to compare with.

        Returns:
            float: The standard deviation.

        """
        return np.sqrt(sqr_dev_func(val, data))


    def abs_dev_func(val, data):
        """
        Calculate the mean absolute deviation of a value from a list of values.

        Args:
            val (int): The value to compare with.
            data (list): The list of values to compare with.

        Returns:
            float: The mean absolute deviation.

        """
        return np.mean([np.abs(val - i) for i in data])


    def distribution_func(data, deviation_type, return_type):
        """
        Calculate the tendency of a given data set.

        Args:
            data (iterable): The input data set.
            deviation_type (int): The type of deviation to be used in the calculation. Must be either 1 or 2.
            return_type (str): The type of result to return.

        Returns:
            The calculated tendency based on the given parameters.

        Raises:
            ValueError: If the deviation_type is not 1 or 2.

        """
        if deviation_type == 1 or deviation_type == 2:
            deviation_array = tuple(np.mean(tuple(abs(i-j)**deviation_type for j in data))**(1/deviation_type) for i in data)
            min_indices = np.where(deviation_array == np.min(deviation_array))
            tendency = np.unique(list(data[index] for index in min_indices[0]))

            if return_type == 'distr':
                return [[val - min(deviation_array), val, val + min(deviation_array)] for val in tendency]
            elif return_type == 'conc distr':
                return [np.min(tendency) - min(deviation_array),np.mean(tendency),np.max(tendency) + min(deviation_array)]
            else:
                return min(deviation_array) if return_type == 'dev' else tendency if return_type == 'tend' else [min(deviation_array), tendency]
        else: 
            raise ValueError('deviation_type must be 1 or 2')


    def diff_filter_func(val, data, type, is_equal):
        """
        Filter values above or below a given value from a list of values.

        Args:
            val (int): The value to compare with.
            data (list): The list of values to compare with.
            type (int): The type of comparison. 1 for above, -1 for below, 0 for all.
            is_equal (bool): Whether to include the value or not.

        Returns:
            list: The filtered values.

        """
        if type == 1:
            return [i for i in data if i >= val] if is_equal else [i for i in data if i > val]    
        elif type == -1:
            return [i for i in data if i <= val] if is_equal else [i for i in data if i < val]
        elif type == 0:
            return [i for i in data if (i == val)] if is_equal else [i for i in data if i != val]


    def difference_generator(data, order):
        """
        Generate the differences between consecutive elements in a list.

        Args:
            data (list): The input list.

        Returns:
            list: The differences between consecutive elements.

        """
        return np.diff(data, n=order)


    def change_prob(data, diff_type):
        """
        Calculate the probability of change in a given data set.

        Args:
            data (list): The input data set.
            diff_type (int): The type of difference to consider.

        Returns:
            float: The probability of change.

        """
        return len(diff_filter_func(0, difference_generator(data,1), diff_type, False)) / len(difference_generator(data,1))


    def change_distribution(data, deviation_type, diff_type, return_type):
        """
        Calculate the distribution of change in a given data set.

        Args:
            data (list): The input data set.
            deviation_type (int): The type of deviation to be used in the calculation.
            diff_type (int): The type of difference to consider.
            return_type (str): The type of result to return.

        Returns:
            The calculated distribution of change based on the given parameters.

        """
        change_data = diff_filter_func(0, difference_generator(data,1), diff_type, False)
        return distribution_func(change_data, deviation_type, return_type)


    def random_func(prob_range, pos_change_range, neg_change_range):
        """
        Generate a random value based on probability ranges.

        Args:
            prob_range (tuple): The range of probability.
            pos_change_range (tuple): The range of positive change.
            neg_change_range (tuple): The range of negative change.

        Returns:
            float: A random value based on the probability ranges.

        """
        return random.uniform(*pos_change_range) if random.random() <= random.uniform(*prob_range) else random.uniform(*neg_change_range)


    def gen_forecasts(function, first_val, events, number_sub_arrays, is_concatenated):
        """
        Generate forecasts based on a given function.

        Args:
            function (function): The function used to generate values.
            first_val (float): The initial value.
            events (int): The number of events.
            number_sub_arrays (int): The number of sub-arrays.
            is_concatenated (bool): Whether to return concatenated sub-arrays.

        Returns:
            list: The generated forecasts.

        """
        main_arr, sub_arr = [], []

        for i in range(number_sub_arrays*events):
            if np.mod(i, events) == 0  or i == 0:
                main_arr.append(first_val)
                if is_concatenated and i != 0 :
                    sub_arr.append(main_arr[i-events:i])  
            else:
                main_arr.append(main_arr[-1] + function())
            if is_concatenated and i == number_sub_arrays*events-1:
                sub_arr.append(main_arr[i+1-events:i+1])
        return sub_arr if is_concatenated else main_arr


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

            # Generate combinations or sub-arrays based on the specified parameters
            result = [list(group) for group in itertools.combinations(arr, n)] if combination_recursive == 'com' else [arr[i:i + n] for i in range(0, len(arr) - n + 2, n - 1) if len(arr[i:i + n]) == n]
            return result
        except Exception as e:
            return str(e)

