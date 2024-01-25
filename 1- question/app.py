# -*- coding: utf-8 -*-
"""
Question#1 
"""


def stripParagraphContent(file):
    paragraphs=file.readlines()
    paragraphsList=[]
        
    for paragraph in paragraphs:
        paragraphsList.append(paragraph.strip())  
             
    return paragraphsList



def readOrWriteFile(message,permission): 
    isOK=False
    file = {}
    fileName = ""
    while isOK != True:
        try :
            name = ""
            isEmpty=True
            while isEmpty == True:
               
                name = input(message)
            
                if name !="":
                    fileName = name                    
                    isEmpty=False
            
            

            file = open(fileName,permission)
                    
        except IOError:
            print("FILE NOT FOUND")
            
        except:
            print("something went wrong")
        else:
             isOK = True
    return file


       
def sensitiveWordsChecker():
    textDoc = readOrWriteFile ("Enter name and extension of file for checking: ","r")
    paragraphs = stripParagraphContent(textDoc)
    
    sesitiveDoc = readOrWriteFile ("Enter name and extension of senstive words file: ","r")
    sensitiveWordsList = stripParagraphContent(sesitiveDoc)
    
    finalDoc = readOrWriteFile("Please enter file name you wish to save detaring data: ", "w")
    finalDoc.write(' ')  
    
    
    for paragraph in paragraphs:
        wordsList = paragraph.split()
      
        for word in wordsList :
            word = word.strip(",.!? ")
            word = word.strip() 
            if word in sensitiveWordsList:
                word = word.replace(word,"*" * len(word))
            finalDoc.write(" "+ word )         
        finalDoc.write('. \n')     
        
sensitiveWordsChecker()