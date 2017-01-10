#!/usr/bin/python3

codon = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"s", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}

def reverseComplement(seq):
    dna = 'AGCT'
    rev = 'TCGA'
    trans = str.maketrans(dna, rev)
    return seq.translate(trans)

def toRNA(seq):
    rev = reverseComplement(seq)
    rna = 'UCGA'
    dna = 'AGCT'
    trans = str.maketrans(dna, rna)
    return [seq.translate(trans), rev.translate(trans)]  

def orfReader(seq):
    rna = toRNA(seq)[0]
    rev = toRNA(seq)[1]
    rnaProts = []
    revProts = []
    start = 0
    for i in range(0, 3):
        rnaProt = ''
        revProt = ''
        for j in range(i, len(rna), 3):
            codonRNA = rna[j:j+3]
            codonRev = rev[j:j+3]
            if len(codonRNA) == 3:
                rnaProt += codon[codonRNA]
                revProt += codon[codonRev]
        rnaProts.append(rnaProt)
        revProts.append(revProt)
    return [rnaProts, revProts]

if __name__ == '__main__':
    seq = 'AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG'
    #print(toRNA(seq))
    print(orfReader(seq))