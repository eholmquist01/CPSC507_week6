# Author: Emmalyn Holmquist
# Date: 10/13/2024
# Homework 6, Problem 5

# Write a Python function that counts the number of lines in a text file.

def count_line(file):
    counter = 0
    for line in file:
        counter+= 1
    print(counter)

#test
# fin = open("note1.txt")
# count_line(fin)
