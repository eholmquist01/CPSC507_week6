# Author: Emmalyn Holmquist
# Date: 10/13/2024
# Homework 6, Problem 6

# Write a function that reads a text file and writes a new file where all the duplicate lines are removed.

def new_file(infile):
    outfile = input("Enter a new file name: ") #ask user for file name
    fin = open(infile) #define input and output fiel names
    fout = open(outfile, "w")
    non_duplicates = [] #initialize a list for non duplicate lines

    for line in fin: #for each line in the file...
        stripped = line.strip() #take out all unnecessary spaces
        if stripped not in non_duplicates: # if it is a unique line, then add it to the unique line list
            non_duplicates.append(stripped)

    for line in non_duplicates: #print each item in list to the outfile
        fout.write(line + '\n')

    fout.close() #close file

#test
#new_file("tester.txt")