from algorithms import *


text = input('Please provide a graph  to run the TSP on ')
text = input('Please provide a starting vertex ')


T = prims(G, v)
print('Optimal Tree is ')

print('')

print(f'Optimal cost: {graph_cost(T)}')