import os, sys
import unittest

###Preamble
#This solution is more experimental and more reflecting of actually testing the components of the function.
#instead of simply testing one output string, it tests the individual answers, with a test case for each.

"""
Write a Python function which accepts a single list as a parameter. This list consists of any number of lists (1..n),
and you can assume each list only contains character strings (e..g. [‘a’, ‘b’, ‘bc’...]). The function should print out the
following:
- Strings that appear in more than one list
- The total number of unique strings across all lists
- The total number of strings that were processed
"""
inputList= [['test','test1','test2'],['test','test3','test4'],['test','test1','test5','test6']]


def StringAnalyzer(topList):
    
    processedStrings = 0 #all of the strings
    uniqueStrings = [] #all unique instances of strings (not strings that appear only once)
    stringsInMoreThanOne = [] #Strings that appear in more than one list

    ###LOGIC

    for subList in topList: #each sublist in the toplist
        for item in subList: #each item in the sublist
            processedStrings += 1 #increment for processedStrings
            
            if uniqueStrings.count(item)==0: #add it to the uniqueStrings if it's not already on (count!=0)
                uniqueStrings.append(item) #getting a list of unique strings for counting later
            for tempSublist in topList: 
                if tempSublist==subList:#skip if the subList and tempSubList are the same
                    continue
                if tempSublist.count(item)>0:#if this item is found in this (temp)SubList
                    if stringsInMoreThanOne.count(item)==0:#and we haven't already got it on the stringsInMoreThanOne list
                        stringsInMoreThanOne.append(item)#add it to the list
    
    ###PRINT AS WE GO METHOD/RETURN THE DATA

    #Print as we build
    print("Strings that appear in more than one list: ", end =" ")
    #print(*stringsInMoreThanOne, sep=', ') #didn't print in quotes
    loopCount = 0
    for aString in stringsInMoreThanOne:
        loopCount+=1
        if(loopCount==len(stringsInMoreThanOne)): #the last
            print('"'+aString+'"')
        else: #the first/inbetween
            print('"'+aString+'",', end =" ")
        
    print("Total number of unique strings across all lists: "+str(len(uniqueStrings)))
    print("Total number of strings that were processed: "+str(processedStrings))
    
    return stringsInMoreThanOne, len(uniqueStrings), processedStrings
    #return outString

print(StringAnalyzer(inputList))#will print once within the function, then print a list of variables.

