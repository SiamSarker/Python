import math as m

with open("weighted.txt", 'r') as f:
    firstline = f.readline()
    nodes, edge = [int(eachval) for eachval in firstline.split()]
    print(nodes, edge)

    adj_matrix = [[m.inf]*(nodes+1) for eachrow in range(0, nodes+1)]

    for eachline in range(edge):
        curline = f.readline()
        leftnode, rightnode, weight = [int(eachval) for eachval in curline.split()]

        adj_matrix[leftnode][rightnode] = weight
        adj_matrix[rightnode][leftnode] = weight  # for directed graph, skip this line

    for row in range(1, nodes+1):
        for col in range(1, nodes+1):
            print(adj_matrix[row][col], end=" ")
        print()