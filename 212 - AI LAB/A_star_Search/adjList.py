with open("weighted.txt", 'r') as f:
    firstline = f.readline()
    nodes, edge = [int(eachval) for eachval in firstline.split()]
    print(nodes, edge)

    adj_list = [[] for node in range(0, nodes+1)]

    for eachline in range(edge):
        curline = f.readline()
        leftnode, rightnode, weight = [int(eachval) for eachval in curline.split()]

        adj_list[leftnode].append([rightnode, weight])
        adj_list[rightnode].append([leftnode, weight])  # for directed graph, skip this line

    for node in range(1, nodes+1):
        print(node, adj_list[node])