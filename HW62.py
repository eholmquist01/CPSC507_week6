# Author: Emmalyn Holmquist
# Date: 10/13/2024
# Homework 6, Problem 2

# Write a function that takes a dictionary as an argument and returns a new dictionary that has the keys and values swapped.
# If multiple keys in the original dictionary have the same value, convert these values to lists in the inverted dictionary.

def swap(d):
    inverse = {} #initialize a dict to return swaps
    for key in d:
        value = d[key] #temporary storage for swap value
        if value not in inverse: #if value is not yet in inverse, then make it a key
            inverse[value] = [key]
        else:
            inverse[value].append(key) #if the value is already in dict, append it (make it a list)
    return inverse


#test
#input_dict = {'hello':'world', 'true': 'world', 'false': 'world', 'goodbye': 'hi'}
#print(swap(input_dict))