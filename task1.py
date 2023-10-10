def find_min_value(dictionary):
    min_value = float('inf')

    for value in dictionary.values():
        if isinstance(value, int):
            min_value = min(min_value, value)
    
    if min_value == float('inf'):
        return None  
    else:
        return min_value

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': -10000}
result = find_min_value(my_dict)
print(result)
