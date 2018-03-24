#to transpose the column of data created
#in the last program into a row
#to be made into a matrix in the next program
x = []
with open('/Users/sparlan/Desktop/EdwardsLab/matrices/matwVars.txt', 'r') as infile:
    for line in infile:
        x.append(line.replace('\n', ''))

with open('/Users/sparlan/Desktop/EdwardsLab/matrices/TRANSPOSED.tsv', 'w') as outfile:
    outfile.write('\t'.join(x))

print('Your array is transposed!')


#####


#creates a matrix/training set of the rows of data
#produced in the previous program
filenames = ['/path/to/infile/ofVariableNames.tsv', '/path/to/Desktop/infile.tsv', '/path/to/Desktop/infile.tsv', '/path/to/Desktop/infile.tsv', '/path/to/Desktop/infile.tsv', '/path/to/Desktop/infile.tsv', '/path/to/Desktop/infile.tsv', '/path/to/Desktop/infile.tsv', '/path/to/Desktop/infile.tsv', '/path/to/Desktop/infile.tsv', '/path/to/Desktop/infile.tsv']

with open('/path/to/outfile.tsv', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line + '\n')

outfile.close()

print('Matrix is finished')
