# Author: Emmalyn Holmquist
# Date: 10/13/2024
# Homework 6, Problem 4

# Write a function that takes a nested dictionary and a target value as parameters.
# The function should return a list of keys that form the path to the target value.
# If the target value doesn't exist, return None.

def path(d, target):
    def recurse(cd, cp): #call function while we get through the nest
        for key, value in cd.items(): #looks through both the keys and values of the current dictionary
            new_path= cp + [key] #new path is the list we are making. Add the current path (old list) plus the key to build the path
            if value == target: #if the value in the current path is the same as the target (value we are searching for!)...
                return new_path #return the path we built. process finished! otherwise, we need to continue to build path.
            elif isinstance(value, dict): #this line checks to see if there is another dictionary in the nest to look into. python doc: https://docs.python.org/3/library/functions.html#isinstance
                # (i.e., is value another dictionary, or just a value in a dict?).
                #If we cannot "disect" anymore, the process is finished, and we need to return that there is no target value.
                final_path = recurse(value, new_path) #if it is a dictionary, recurse the function again!
                if final_path: # if the value is the target, it will skip to this line and return the result/path
                    return final_path
        return None #if the value was not the target, and we reached the end of the dict, then we will return None.
    return recurse(d, []) #this will recurse again so that we check other possible nested dictionaries (the list stores the path so far)



# test
# nested_dict = {'a':
#                   {'b':
#                       {'c': 1,'d': 2},
#                        'e': 3},
#                    'f': 4,'g': {'h': {'i': 5}}}
#
# target_value = 8
# x = path(nested_dict, target_value)
# print(x)
#
# target_value = 5
# x = path(nested_dict, target_value)
# print(x)