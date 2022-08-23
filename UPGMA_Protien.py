from ete3 import Tree

import csv

distanceMatrix = []

ch = "A"
names = []
with open('.\\Output\\Pdistance.csv', 'r') as input:
    reader = csv.reader(input)
    i = 0
    for line in reader:
        if i and line != []:
            distanceMatrix.append([float(i) for i in line[1:i]])
        elif i == 0:
            names = [x.split()[0] for x in line[1:]]
        i+=1

# print(distanceMatrix)
# print(names)
for o in range(len(names) - 1):
    max = 0
    for i in range(len(distanceMatrix)):
        for j in range(len(distanceMatrix[i])):
            if distanceMatrix[i][j] > max:
                max = distanceMatrix[i][j]
                maxpos = (j,i)
    names[maxpos[0]] = "(" + names[maxpos[0]] + "," + names[maxpos[1]] + ")"
    names.pop(maxpos[1])
    # print(names)
    for i in range(maxpos[0]):
        distanceMatrix[maxpos[0]][i] = (distanceMatrix[maxpos[0]][i] + distanceMatrix[maxpos[1]][i])/2

    for i in range(maxpos[0] + 1, maxpos[1]):
        distanceMatrix[i][maxpos[0]] = (distanceMatrix[i][maxpos[0]] + distanceMatrix[maxpos[1]][i])/2

    for i in range(maxpos[1] + 1, len(distanceMatrix)):
        distanceMatrix[i][maxpos[0]] = (distanceMatrix[i][maxpos[0]] + distanceMatrix[i][maxpos[1]])/2
        distanceMatrix[i].pop(maxpos[1])

    distanceMatrix.pop(maxpos[1])

final = names[0] + ";"
finalTree = Tree(final)
print(finalTree)