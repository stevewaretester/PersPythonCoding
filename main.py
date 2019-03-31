# -*- coding: latin-1 -*-
import os, sys

"""
Write a Python function which accepts a single list as a parameter. This list consists of any number of lists (1..n),
and you can assume each list only contains character strings (e..g. [‘a’, ‘b’, ‘bc’...]). The function should print out the
following:
- Strings that appear in more than one list
- The total number of unique strings across all lists
- The total number of strings that were processed
"""
inputList= [['test','test1','test2'],['test','test3','test4'],['test','test1','test5','test6']]

def StringThing(topList):
    
    processedStrings = 0
    uniqueStrings = []
    StringsInMoreThanOne = []

    #logic

    for subList in topList: #each sublist in the toplist
        for item in subList: #each item in the sublist
            processedStrings += 1 #increment for processing
            
            if uniqueStrings.count(item)==0:
                uniqueStrings.append(item) #getting a list of unique strings for counting later
            for tempSublist in topList:
                if tempSublist==subList:
                    continue
                if tempSublist.count(item)>0:
                    if StringsInMoreThanOne.count(item)==0:
                        StringsInMoreThanOne.append(item)
                
    print("Strings that appear in more than one list: ", end =" ")
    #print(*StringsInMoreThanOne, sep=', ') #didn't print in quotes
    loopCount = 0
    for aString in StringsInMoreThanOne:
        loopCount+=1
        if(loopCount==len(StringsInMoreThanOne)): #the last
            print('"'+aString+'"')
        else: #the first/inbetween
            print('"'+aString+'",', end =" ")
        
    print("Total number of unique strings across all lists: "+str(len(uniqueStrings)))
    print("Total number of strings that were processed: "+str(processedStrings))
    return

StringThing(inputList)
