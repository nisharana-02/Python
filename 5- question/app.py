# -*- coding: utf-8 -*-

"""
    Questoin no. 5: 
"""
import random

def game():
    wordsFile = open("words.txt","r")
    orignalWordsList = wordsFile.read().split(",")
    wordsList = [word.strip() for word in orignalWordsList]
    guessWord = random.choice(wordsList)
    print(guessWord)
    totalChances = len(guessWord)
    guessLetterList = []
    print("You have total {} chances".format(totalChances))
    while totalChances > 0:        
        guessLetter = str(input("PLease Enter character: "))
        guessLetterList.append(guessLetter)
        
        word = ""
        
        for letter in guessWord:
            if letter in guessLetterList:
                word += " "+letter+" "
            else:
                word +=" _ "
        print(word)
        if totalChances - 1 == 0:
            print("\n\n Game Finished!!!!")
        else:
            print("\n\nYou have left with {} chances".format(totalChances - 1))
       
        totalChances = totalChances - 1
 
game()
