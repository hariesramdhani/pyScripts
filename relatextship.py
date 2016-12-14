#!/usr/bin/python3

"""
Relatextship is a program that will help you find the relation
between texts in the scientific journals, books, articles or 
anything that contain texts.
------------------------------------------------------------
PROGRESS : ███ 22.3%
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
    filters = 'in at was is are of on than but from can'
    libs = {}
    for i in range(len(tokens)-1):
        token = tokens[i]
        nextToken = tokens[i+1]

        if token not in libs:
            libs[token] = [1, {}]
            sublib = libs[token][1]
            if filters.find(nextToken) == -1:         
                sublib[nextToken] = 1
        else:
            libs[token][0] += 1
            sublib = libs[token][1]
            if nextToken not in sublib and filters.find(nextToken) == -1:
                sublib[nextToken] = 1
            elif filters.find(nextToken) == -1:
                sublib[nextToken] += 1
    return libs

# def mostAppearingWords(filename):
#     libs = libraryMaking(filename)
#     h = max(libs, libs.get[0])
#     return h

def main():
    filename = 'test.txt'
    libs = libraryMaking(filename)
    keyword = input('Enter your keyword: ')
    while keyword not in libs:
        print('The keyword you entered is not on the text.')
        keyword = input('Please enter a different keyword: ')
    print('%s appeared %d times in the text' % (keyword, libs[keyword][0]))
        
if __name__ == '__main__':
    main()
