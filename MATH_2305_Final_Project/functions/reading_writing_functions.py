

import numpy as np 

def get_graph(textfile):
    
edgelist = np.loadtxt('data/{textfile}', dtype = int)

G = ([],[])

for x in edgelist:
    if x[0] not in G[0]:
        G[0].append((x[0], x[0]))

    if x[1] not in G[0]:
        G[1].append((x[0], x[1]))

    G[1]
    G[1].append((x[0], x[1]))

    return G
