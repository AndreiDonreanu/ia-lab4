class Node():

    def __init__(self, vertex_number):
        self.vertex_number = vertex_number
        self.neighbours = []

    def edge(self, node):
        self.neighbours.append(node)

    def __str__(self):
        return f'({self.vertex_number})'

    def __repr__(self):
        return f'({self.vertex_number})'



nodes = []
for i in range(7):
    nodes.append(Node(i))
nodes[1].edge(nodes[3])
nodes[1].edge(nodes[6])
nodes[2].edge(nodes[6])
nodes[3].edge(nodes[3])
nodes[3].edge(nodes[4])
nodes[5].edge(nodes[2])
nodes[6].edge(nodes[3])
nodes[6].edge(nodes[4])
nodes[6].edge(nodes[5])



adjmat=[
]
adjmat.append([0,0,0,0,0,0,0])
adjmat.append([0,0,0,0,0,0,0])
adjmat.append([0,0,0,0,0,0,0])
adjmat.append([0,0,0,0,0,0,0])
adjmat.append([0,0,0,0,0,0,0])
adjmat.append([0,0,0,0,0,0,0])
adjmat.append([0,0,0,0,0,0,0])



for i in range(7):
    vecini=nodes[i].neighbours
    for j in vecini:
        adjmat[i][j.vertex_number]=1
        adjmat[j.vertex_number][i]=1





for i in range(7):
    print(adjmat[i])






