"""Prims' Algorithm :
                The steps for implementing Prim's algorithm are as follow:
                
                1) Initialize the minimum spanning tree with a vertex chosen at random.
                2) Find all the edges that connect the tree to new vertices, find the minimum and add it to the tree
                3) Keep repeating step 2 until we get a minimum spanning tree. """



def Prims(G):
#Initialiazation 
    T = {0}
    E = []
    Tree = (T, E)  # a tuple
    total = 0
    while Tree[0] != VT:
    #Finding min cost edge incident to vertex.
        min_edge = min_valid_incident_edge(G, Tree)
        if min_edge[0] not in VT:
            VT.add(min_edge[0])     # Finding new vertex

        if min_edge[1] not in VT:   
            VT.add(min_edge[1])
        ET.append(min_edge)

    print('Result: ',VT, ET) 
