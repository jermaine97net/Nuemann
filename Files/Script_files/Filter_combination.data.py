import numpy as np

iterations = 7
repeat = 2
index_increment = 1
greater_than = 3
less_than = iterations + 1

data = np.tile(np.arange(iterations), repeat)

indx = list(np.where((data > greater_than) & (data < less_than))[0])
print(data)


def direct_method (): # This method acts directly on the range without creating a list of indices
    results, counter = [], 0
    data_size = len(data)
    for val in data:
        if(counter + index_increment < data_size) and (val > greater_than and val < less_than):
            results.append((val, data[counter + index_increment]))
        counter += 1
    return results


def conditional_method (): # This method directly checks each value in the list of indices without recreating the list of indices
    results = [] 
    for index in indx:
        if index + index_increment < len(data):
            results.append((data[index], data[index + index_increment]))  
    return results  # Return the results list


def remove_method (): # This method recreates the list of indices based on the condition
    results = []  
    if len(data) - index_increment in indx:
        indx.remove(len(data) -index_increment)

    for i in indx:
        results.append((data[i],data[i+index_increment]))  
    return results  
        

    results = [] 
    for index in indx:
        if index + index_increment < len(data):
            results.append((data[index], data[index + index_increment]))  
    return results  # Return the results list



