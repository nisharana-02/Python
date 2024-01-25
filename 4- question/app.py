# -*- coding: utf-8 -*-
"""
Question#4
"""

def getUserInput(msg):
    isEmpty=True
    inputString = ""
    while isEmpty == True:
       
        inputString = input(msg)
    
        if inputString !="":
            isEmpty=False
    
    return inputString
    
def checkStrings():
    
    firstString = set([*getUserInput("Enter First String: ")])
    secondString = set([*getUserInput("Enter Second String: ")])
    alphabets = []
    start = ord('a')
    for i in range(26):
       alphabets.append(chr(start + i))
    alphabetSet = set(alphabets)
    print("\n\n Common Characters are: {}".format(firstString.intersection(secondString)))
    print("\n\n Unique Characters are: {}".format(firstString.symmetric_difference(secondString)))
    print("\n\n Non-occuring Characters are: {}".format(alphabetSet.symmetric_difference(firstString.union(secondString))))
    
checkStrings()
