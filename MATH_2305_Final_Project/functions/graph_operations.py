
def incident_edges(G, T):
    edges = []
    for e in G[1]:
        for v in T[0]:
            if v in e and e not in T[1]:
                edges.append(e)

    # Remove edges that make cycles

     return edges

def cost(G, e):
    return G[1][e]

# add a min_cost_incident_edge(G, T)

# GRAPH_COST RETURN THE TOTAL WEIGHT OF A GRAPH
