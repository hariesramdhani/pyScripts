#!/usr/bin/python3

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

# def libraryMaking(filename):
#     tokens = tokenize(filename)
#     libs = {}
#     for i in range(len(token)):

if __name__ == '__main__':
    filename = 'test.txt'
    print(tokenize(filename))