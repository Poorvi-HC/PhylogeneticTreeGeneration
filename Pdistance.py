import csv

import blosum as bl

blosum = bl.BLOSUM(62)

elements = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V', 'B', 'Z', 'X', '*']

# Opening the input file and storing all the data in l
file = open(".\\Input\\Protein.txt", "r")
lines = []
flag = 0
for line in file:
    if line[0] == '>':
        lines.append(line.strip())
        p = 1
    else:
        if p:
            lines.append(line.strip())
            p = 0
        else:
            lines[-1] += line.strip()
file.close()

# Seperating the names from the sequences
sequences = []
names = []
for i in range(len(lines)):
    if i%2:
        sequences.append(lines[i])
    else:
        names.append(lines[i])

# The function to calculate the distance
def distance(seq1, seq2):
    matrix = []
    seq1len = len(seq1)
    seq2len = len(seq2)
    tracker = [[0 for i in range(seq2len + 1)] for j in range(seq1len + 1)]
    matrix.append([-4*i for i in range(seq2len + 1)])
    for i in range(seq1len):
        toad = [-4*(i+1)]
        for j in range(seq2len):
            toad.append(blosum[elements[elements.index(seq1[i])] + elements[elements.index(seq2[j])]])
        matrix.append(toad)
    for i in range(1, seq1len + 1):
        for j in range(1, seq2len + 1):
            diag = matrix[i-1][j-1] + matrix[i][j]
            right = matrix[i][j-1] - 4
            down = matrix[i-1][j] - 4
            matrix[i][j] = max(diag, right, down)
            if matrix[i][j] == diag:
                tracker[i][j] = tracker[i-1][j-1] + 1
            elif right == down:
                tracker[i][j] = min(tracker[i-1][j], tracker[i][j-1]) + 1
            elif right > down:
                tracker[i][j] = tracker[i][j-1] + 1
            else:
                tracker[i][j] = tracker[i-1][j] + 1

    return matrix[seq1len][seq2len]/tracker[seq1len][seq2len]


# The main loop - goes through all the pair combinations to find distance and stores them in distanceMatrix

distanceMatrix = [[0 for i in range(len(sequences))] for j in range(len(sequences))]
for i in range(len(sequences)):
    for j in range(i+1, len(sequences)):
        distanceMatrix[i][j] = distanceMatrix[j][i] = distance(sequences[i], sequences[j])


# Finally storing all the data in ther csv file
# print(names)
ch = "A"
names_out = []
for idx in range(len(names)):
    names_out.append(ch)
    ch = chr(66 + idx)
# print(names_out)

with open('.\\Output\\Pdistance.csv', 'w') as output:
    writer = csv.writer(output)
    writer.writerow([""] + names_out)
    for i in range(len(names)):
        towrite = [names_out[i]]
        towrite.extend(distanceMatrix[i])
        writer.writerow(towrite)