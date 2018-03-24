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
