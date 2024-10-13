# Author: Emmalyn Holmquist
# Date: 10/13/2024
# Homework 6, Problem 1

# Given a string, write a Python function that returns a dictionary with the frequency count of
# each character in the string. Ignore case and ignore all non-alphabetic characters.

def char_freq(string):
    freq_string = {}
    for char in string: #look at every character in the string
        if char.isalpha(): #if the character is in alphabet, we will add it
            char = char.lower() #make it lowercase to ignore case
            if char in freq_string: #if it is already in dict, add one to value of dict pertaining to char key
                freq_string[char] += 1
            else: # otherwise add it to dict
                freq_string[char] = 1
    return freq_string

string = input("Enter a string for analysis: ")
print(char_freq(string))