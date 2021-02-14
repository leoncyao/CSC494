


edges = [('0', '1'), ('1', '2'), ('2', '1')]
# edges = [('0', '1', '2')]
hyperedges = []
for e1 in edges:
    for e2 in edges:
        # print(e1)
        # print(e2)
        # print([e1[0]+e2[0],e1[0]+e2[1], e1[1]+e2[0], e1[1]+e2[1]])   
        # hyperedges.append([e1[0]+e2[0],e1[0]+e2[1], e1[1]+e2[0], e1[1]+e2[1]])
        hyperedge = []
        for i in range(len(e1)):
            for j in range(len(e2)):
                hyperedge.append(e1[i] + e2[j])
        hyperedges.append(hyperedge)
print(hyperedges)

def decode(word):
    word = 3 * int(word[0]) + int(word[1])
    # print(word)
    return word


def genbin(n, bs = ''):
    if n-1:
        genbin(n-1, bs + '0')
        genbin(n-1, bs + '1')
    else:
        word = '1' + bs
        coloring = []
        for i in range(len(word)):
            # print(word[i])
            if word[i] == "1":
                coloring.append(1)
            else:
                coloring.append(-1)
        # print(coloring)
        disc = 0
        for edge in hyperedges:
            for i in range(len(edge)):
                disc += coloring[decode(edge[i])]
            # disc += abs(coloring[decode(edge[0])] + coloring[decode(edge[1])] + coloring[decode(edge[2])] + coloring[decode(edge[3])])
        # print(disc)
        if disc == 0:
            print(coloring) Z
genbin(9)