#!/usr/bin/python3

import re

def enzymeSelection(filename):
    pattern = "(\w.*) \("
    enzymes = []
    with open(filename, 'r') as file:
        for enzyme in file:
            enzymes += re.findall(pattern, enzyme)
    return enzymes

def compareEnzymes(dnaFile, plasmidFile):
    usableEnzymes = []
    dnaEnzymes = ' '.join(enzymeSelection(dnaFile))
    plasmidEnzymes = enzymeSelection(plasmidFile)
    for enzyme in plasmidEnzymes:
        if dnaEnzymes.find(enzyme) == -1:
            usableEnzymes.append(enzyme)
    return usableEnzymes

if __name__ == '__main__':
    dnaFile = 'aprX.txt'
    plasmidFile = 'pUC19.txt'
    print(compareEnzymes(dnaFile, plasmidFile))