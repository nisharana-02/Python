# -*- coding: utf-8 -*-
"""
Question#3
"""
def palindromicChecker():
    isEmpty=True
    word = ""
    while isEmpty == True:
        word = input("Please Enter a word: ")
        if word !="":
            isEmpty=False
    
    reverseWord = word[::-1]    
    
        
    if word == reverseWord:
        print("Word is a palidromic word")
    else:
        print("Word is not a palidromic word")

palindromicChecker()