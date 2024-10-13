# Author: Emmalyn Holmquist
# Date: 10/13/2024
# Homework 6, Problem 3

# Write a function that merges two dictionaries.
# If the dictionaries have overlapping keys, sum the values corresponding to these keys in the resulting dictionary.

def merge(d1, d2):
    for key in d2: #go through each key in second dict; will add to first dict
        if key not in d1: #if the key is not in the second dict, add it
            d1[key] = d2[key]
        else: #if it is, this changes the key's value to be the sum of the two
            d1[key] = d2[key] + d1[key]

    print(d1)

# test
# d1 = {'hello': 2, 'bye': 3}
# d2 = {'hello': 3, 'my': 1, 'name' : 3, 'is': 4, 'jerry': 7, 'bye': -2}
#
# merge(d1, d2)
