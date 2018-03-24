#calculates abundance of all crAssphage k-mer in a metagenome
#this was done before feature reduction 

import sys
import operator
from operator import itemgetter
import time

cr = str(sys.argv[1])
mf = str(sys.argv[2])
crassMers = {}


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


#calls the readFasta function
#creates a global dictionary called crassMers
#that maps every position in crassphage to every possible kmer
def getCrassMers(filename):
    cseq = readFasta(filename)
    print("Pulling out crAssphage kmers..")
    cGenome = cseq['>JQ995537']
    clen = len(cGenome)-50
    i = 0

    while i < clen:
        mer = cGenome[i:i+50]
        crassMers[i] = mer.upper()
        i+=1


#reads in a FASTA file containing the metagenome
#creates a dictionary called abundance
#that maps the kmer to the frequency
#returns abundance dictionary
def getMetaMers(metafile):
    mseq = readFasta(metafile)
    print("Pulling out metagenome mers..")
    abundance = {}
    for x, sequence in mseq.items():
        mlen = len(sequence)-50
        y = 0
        while y<mlen:
            mer = sequence[y:y+50].upper()
            if mer in abundance:
                abundance[mer] += 1
            else:
                abundance[mer] = 1
            y+=1

    return abundance


#calls getCrassMers and getFastqMers functions
#creates a dictionary called bins
#mapping every crass kmer to its frequency
#returns the bins dictionary
def binMetagenomes(crassfile, metafile):
    getCrassMers(crassfile)
    mdict = getMetaMers(metafile) 
    print("Binning kmers..")
    bins = {}
    
    for pos, mer in crassMers.items():
        if mer in mdict:
            bins[pos] = mdict[mer]
        else:
            bins[pos] = 0
    return bins


#calls the binMetagenomes function
#sorts the kmers from most abundant to least
#creates two sorted lists occurrence/frequency and kmer
#returns the two sorted lists
def sortBins(crass,meta):
    binDict = binMetagenomes(crass, meta)
    print("Sorting bins based on abundance..")
    sortedbins = sorted(binDict.items(), key=itemgetter(1), reverse=True)
    occurrence = [x[1] for x in sortedbins]
    position = [y[0] for y in sortedbins]
    o = 0
    p = 0
    return occurrence, position


#calls the sortBins function
#creates as output TSV file with columns position, occurence, and kmer
#prints the amount of time it took to run the whole program
def binplot(cfile, mfile):
    tStart = time.time()
    occurrences, positions = sortBins(cfile, mfile)
    print("Creating TSV file..")
    i = 0
    s = open('S57_50mers.tsv', 'w')
    s.write('position\toccurence\tkmer\n')
    while i < len(crassMers): 
        o = str(occurrences[i])
        p = str(positions[i])
        kmer = crassMers[positions[i]]
        s.write(p + '\t' + o + '\t' + kmer + '\n')
        i += 1
    s.close()
    tEnd = time.time()
    print("Finished in " + str(tEnd-tStart) + " seconds!!")   


binplot(cr, mf)
