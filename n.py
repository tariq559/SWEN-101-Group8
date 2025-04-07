#w


def deduplicate_tuple(a_tuple):
    seen = {}
    result = []
    for element in a_tuple:
        if element not in seen:
            seen[element] = True
            result.append(element)
    return tuple(result)



def get_min_value_index(a_list):
    if not a_list:
        return None
    min_value = min(a_list)
    return a_list.index(min_value)

def fish_sort(a_list):
    sorted_list = []
    while a_list:
        min_index = get_min_value_index(a_list)
        smallest_value = a_list[min_index]
        a_list.pop(min_index)
        sorted_list.append(smallest_value)
    return sorted_list


import random
from collections import Counter

SOCKS = ["argyle", "blue", "polka dot", "red", "black", "white", "pink",
         "gingham", "orange", "striped"]

def get_pair_count(list_o_socks):
    # Count the occurrences of each sock style using Counter
    sock_counts = Counter(list_o_socks)
    
    # Initialize a list to store the result
    result = []
    
    # Iterate over the counted sock styles
    for style, count in sock_counts.items():
        # Calculate the number of pairs (each pair consists of exactly 2 socks)
        pair_count = count // 2
        # Append the style and the number of pairs to the result
        result.append((style, pair_count))
    
    return result

# Example usage:
print(get_pair_count(["blue", "striped", "striped", "blue", "blue"]))
print(get_pair_count(["blue", "red", "pink", "blue", "pink", "pink", "pink", "pink"]))
