from ete3 import Tree

import csv

Distance = []

with open('.\\Output\\Ndistance.csv', 'r') as input:
    reader = csv.reader(input)
    i = 0
    for line in reader:
        if i and line != []:
            Distance.append([float(i) for i in line[1:int(i/2)]])
        elif i == 0:
            names = [x.split()[0] for x in line[1:]]
        i+=1

# print(Distance)

for o in range(len(names) - 1):
    min = 1
    for i in range(len(Distance)):
        for j in range(len(Distance[i])):
            if Distance[i][j] < min:
                min = Distance[i][j]
                pos = (j,i)
    names[pos[0]] = "(" + names[pos[0]] + "," + names[pos[1]] + ")"
    # print(names)
    names.pop(pos[1])
    # print(names)
    for i in range(pos[0]):
        Distance[pos[0]][i] = (Distance[pos[0]][i] + Distance[pos[1]][i])/2

    for i in range(pos[0] + 1, pos[1]):
        Distance[i][pos[0]] = (Distance[i][pos[0]] + Distance[pos[1]][i])/2

    for i in range(pos[1] + 1, len(Distance)):
        Distance[i][pos[0]] = (Distance[i][pos[0]] + Distance[i][pos[1]])/2
        Distance[i].pop(pos[1])

    Distance.pop(pos[1])

final = names[0] + ";"
finalTree = Tree(final)
print(finalTree)