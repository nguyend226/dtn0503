from functions.reading_writing_functions import get_graph
from functions.graph_operations import incident_edges, cost

G = get_graph('G1.txt')

print(f'V(G) = {G[0]}')
print('')
print(f'E(G) = {G[1]}')
print('')

# Initialize tree 

T = ([3,1, 4]), [(1, 3), (1, 4)])

print(f' T = {T}'
print('')

for e i G[1]:
    print(e)

#print(incident_edges(G, T))

for e in  incident_edges(G, T):
    print(f'Edge {e} with cost {cost{G,e}}')

printf'The cost of edge (1,3) is {cost(G, (1,3))}')
