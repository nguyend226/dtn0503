
from functions. import get_graph
from functions. import incident_edges, cost

G = get_graph('G1.text')

print(f'V(G) = {G[0]}')
print('')
print(f'E(G) = {G[1]}')
print('')

# Initialize tree 

T = ([3,1]), [(1, 3), (1, 4)])

print(f' T = {T}'
print()

for e i G[1]:
    print(e)

#print(incident_edges(G, T))

for e in  incident_edges(G, T):
    print(f'Edge {e} with cost {cost{G,e}}')

printf'The cost pf edge (1,3) is {cost(G, (1,3))}')

----------------
import numpy as np 

def get_graph(textfile):

edgelist = np.loadtxt('data/G1.txt', dtype = int)

G = ([],[])

for x in edgelist:
    if x[0] not in G[0]:
        G[0].append((x[0], x[0]))

    if x[1] not in G[0]:
        G[1].append((x[0], x[1]))

    G[1].append((x[0], x[1]))

    return G 

G = get_graph('G1.txt')

print(f'V(G) = {G[0]}')
print('')
print(f'E(G) = {G[1]}')
