'''
Module name: data
Date created: 27.12.20

This module contains the dictionary data for the program

'''

#######################################dictionary

def makedictionary():
    ''' reads in input file, gives a dictionary object'''
    file = open('shruti.dic', "r")
    contents = file.read()
    lines = contents.split('\n')
    # create dictionary object
    dictionary = {}
    for line in lines:
        words = line.split('\t')
        # add each transcription as a key, and its corresponding word as the value
        dictionary[words[1]] = words[0]
    file.close()
    
    return dictionary     

dictionary = makedictionary()



