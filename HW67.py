# Author: Emmalyn Holmquist
# Date: 10/13/2024
# Homework 6, Problem 7

# Write a Python function that reads a text file containing integers, each on a new line.
# The function should create a new file containing the square of each integer, also each on a new line.

def square_int(infile):
    import math #import math module for sqrt function
    fout_name = input("What is the name of the output file?") #ask user for new file name
    fin = open(infile) #define input and output file
    fout = open(fout_name, 'w') #paramter 'w' because we will be writing!
    for line in fin:
        newline = float(line.strip()) #convert each line to a float
        newline = math.sqrt(newline) #take sqrt
        newline = str(newline) #convert back to string for printing
        fout.write(newline + '\n') #write with a new line
    fout.close() #close file

# test
#square_int("prob7.txt")
