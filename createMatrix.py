#creates a matrix/training set of the rows of data
#produced in the previous program
filenames = ['/path/to/infile/ofVariableNames.tsv', '/path/to/Desktop/infile.tsv', '/path/to/Desktop/infile.tsv', '/path/to/Desktop/infile.tsv', '/path/to/Desktop/infile.tsv', '/path/to/Desktop/infile.tsv', '/path/to/Desktop/infile.tsv', '/path/to/Desktop/infile.tsv', '/path/to/Desktop/infile.tsv', '/path/to/Desktop/infile.tsv', '/path/to/Desktop/infile.tsv']

with open('/path/to/outfile.tsv', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line + '\n')

outfile.close()

print('Matrix is finished'
