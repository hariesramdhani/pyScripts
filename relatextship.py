#!/usr/bin/python3

"""
Relatextship is a program that will help you find the relation
between texts in the scientific journals, books, articles or 
anything that contain texts.
------------------------------------------------------------
PROGRESS : ███ 21%
---------------------------FUNCTIONS------------------------
<TBA>
------------------------------------------------------------
--------------------------PARAMETERS------------------------
<TBA>
------------------------------------------------------------
"""

import re

def getSentences(filename):
    sentences = ''
    with open(filename, 'r') as f:
        for line in f:
            sentences += line.strip()
    return sentences.lower() 

def tokenize(filename):
    sentences = getSentences(filename).lower()
    wordPattern = r'\w*[A-Za-z]\w*'
    sentences = re.findall(wordPattern, sentences)
    return sentences

# def filterTokens(filename):
#     tokens = tokenize(filename)
    
def libraryMaking(filename):
    tokens = tokenize(filename)
    print(len(tokens))
    libs = {}
    for i in range(len(tokens)-1):
        token = tokens[i]
        nextToken = tokens[i+1]

        if token not in libs:
            libs[token] = [1, {}]
            sublib = libs[token][1]            
            sublib[nextToken] = 1
        else:
            libs[token][0] += 1
            sublib = libs[token][1]
            if nextToken not in sublib:
                sublib[nextToken] = 1
            else:
                sublib[nextToken] += 1
    return libs

# def mostAppearingWords(filename):
#     libs = libraryMaking(filename)
#     h = max(libs, libs.get[0])
#     return h


        
if __name__ == '__main__':
    filename = 'test.txt'
    print(mostAppearingWords(filename))
