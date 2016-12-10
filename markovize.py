#!/usr/bin/python3

"""
Markovize is a program that will let you randomize sentences
from a txt file based on the probability of appearance of 
letter that came after the order using Markov's chain rule.

---------------------------FUNCTIONS------------------------
getSentences: gets sentences from a file
ngramize: ngramizes the sentences
markovize: return the possible sentence that can be generated
by markov chain rule
------------------------------------------------------------
---------------------------ARGUMENTS------------------------
filename: your file name
sentenceLength: Length of sentence to be generated 
order: Length of word to be n-grammized, for example order of
3 will return 3-grams of the sentences
------------------------------------------------------------
"""

import random

def getSentences(filename):
    sentences = ''
    with open(filename, 'r') as f:
        for line in f:
            sentences += line.strip()
    return sentences.lower() 

#Generating the ngrams from the given sentences or texts
def ngramize(filename, order):
    sentences = getSentences(filename)
    ngrams = {}
    for i in range(len(sentences)-order+1):
        gram = sentences[i:i+order]
        
        if gram not in ngrams:
            ngrams[gram] = []
        if i + order < len(sentences):
            ngrams[gram].append(sentences[i+order])
    return ngrams, sentences

#Generating random sentences based on the probability of the
#letter appearance
def markovize(keyword, filename, order, sentenceLength):
    ngrams, sentences = ngramize(filename, order)
    while len(keyword) < order:
        keyword = input('Please enter a longer keyword: ')
    while sentences.find(keyword) == -1:
        keyword = input('Your keyword wasnot in the text, please enter another: ')
    currentGram = keyword[-order:]
    result = keyword

    for i in range(sentenceLength):
        possibilities = ngrams[currentGram]
        if len(possibilities) == 0:
            break
        else:
            next = random.choice(possibilities)
            result += next
            currentGram = result[len(result)-order:]
    return result

def main():
    filename = input('Please enter the filename: ')
    keyword = input('Please enter the keyword: ')
    order = int(input('Please enter the order lenght: '))
    sentenceLength = int(input('Please enter the sentece length: '))
    generate = int(input('Please enter the number of generation: '))
    for i in range(generate):
        print(markovize(keyword, filename, order, sentenceLength))
    #print(getSentences(filename))

if __name__ == '__main__':
    main()
    