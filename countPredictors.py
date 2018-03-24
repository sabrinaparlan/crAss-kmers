#calcuates the abundance of predictor k-mers
#of crAssphage in a fecal metagenome
#predictors chosen with random forest model 

import sys
import operator
from operator import itemgetter
import time

mf = str(sys.argv[1])

predictors = ['GTTTATATTGTTCAAGTTTCTCACG', 'TTAAAATTTCTCAAGATGATTATGT', 'ATACTGGCTATTGGAAAGATAAACT', 'AACTGCCCTGTTTTACCTGTATCGA', 'GTGCTTGTTCTAATAATTATAATAC', 'ATTATTAGCTTCAACATCTATATAA','CTGATATTCTTTTTGAGAAATTTTA', 'CAAAATCATTAATAAAACTAGTAAT', 'TACCATCAGCATCTAACTGCCCTGT']

#reads in FASTA file
#creates a dicitonary called seqs mapping the sequence id to the genome
#returns the dictionary
def readFasta(fastafile):
    print("Reading new genome..")
    seqs = {}
    f = open(fastafile, 'r+')
    seq = ''
    seqid = None
    sequence = None

    for line in f:
        line = line.rstrip('\n')
        if line.startswith('>'):
            if seqid != None:
                seqs[seqid] = sequence

            seqid = line
            sequence = ''
        else:
            sequence += line
    seqs[seqid] = sequence
    f.close()
    return seqs


#reads in a FASTA file containing the metagenome
#creates a dictionary called abundance
#that maps the kmer to the frequency
#returns abundance dictionary
def getMetaMers(metafile):
    mseq = readFasta(metafile)
    print("Pulling out metagenome mers..")
    abundance = {}
    totalMers = 0
    for x, sequence in mseq.items():
        mlen = len(sequence)-25
        totalMers = totalMers + mlen
        y = 0
        while y<mlen:
            mer = sequence[y:y+25].upper()
            if mer in predictors:
                if mer in abundance:
                    abundance[mer] += 1
                    y+=1
                else:
                    abundance[mer] = 1
                    print('Found a predictor!')
            else:
                y+=1
    print(totalMers)

    return abundance, totalMers #predictor:abundance


#calls the binMetagenomes function
#sorts the kmers from most abundant to least
#creates two sorted lists occurrence/frequency and kmer
#returns the two sorted lists
def sortBins(meta):
    binDict, totalMers = getMetaMers(meta)
    print("Sorting bins based on abundance..")
    sortedbins = sorted(binDict.items(), key=itemgetter(0))
    occurrence = [x[1] for x in sortedbins]
    kmer = [y[0] for y in sortedbins]
    occurrence[:] = [z/totalMers for z in occurrence] #normalizing it
    return occurrence, kmer


#calls the sortBins function
#creates as output TSV file with columns position, occurence, and kmer
#prints the amount of time it took to run the whole program
def binplot(mfile):
    tStart = time.time()
    occurrences, kmer = sortBins(mfile)
    print("Creating TSV file..")
    i = 0
    s = open('ignore.tsv', 'w')
    s.write('kmer\toccurence\n')
    while i < len(kmer): 
        o = str(occurrences[i])
        k = str(kmer[i])
        s.write(k + '\t' + o + '\n')
        i += 1
    s.close()
    tEnd = time.time()
    print("Finished in " + str(tEnd-tStart) + " seconds!!")   


binplot(mf)
