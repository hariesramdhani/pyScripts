#!/usr/bin/python3

import re
from relatextship import getSentences

def sentencesize(filename):
    sentences = getSentences(filename)
    splSentence = sentences.split('.')
    perSentences = [words.split(' ') for words in splSentence]    
    return perSentences

def libraryMaking(filename):
    perSentences = sentencesize(filename)
    libs = {}
    i = 1
    for sentence in perSentences:
        for word in sentence:
            if word not in libs:
                libs[word] = [i]
            else:
                libs[word].append(i)
        i += 1
    return libs


def main():
    filename = 'test2.txt'
    #print(sentencesize(filename))
    print(libraryMaking(filename))

if __name__ == '__main__':
    main()