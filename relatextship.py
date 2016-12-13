#!/usr/bin/python3

"""
Relatextship is a program that will help you find the relation
between texts in the scientific journals, books, articles or 
anything that contain texts.
------------------------------------------------------------
PROGRESS : ██ 18%
---------------------------FUNCTIONS------------------------
<TBA>
------------------------------------------------------------
---------------------------ARGUMENTS------------------------
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

def libraryMaking(filename):
    tokens = tokenize(filename)
    print(len(tokens))
    libs = {}
    for i in range(len(tokens)):
        token = tokens[i]

        if token not in libs:
            libs[token] = 1
        else:
            libs[token] += 1
    return libs
        


if __name__ == '__main__':
    filename = 'test.txt'
    print(libraryMaking(filename))
