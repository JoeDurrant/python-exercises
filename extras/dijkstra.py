def dijkstra(graph, start):
    return
from Graph import Graph

edges = [[0,0,0,0,1,4,0],
        [0,0,0,0,1,1,15],
        [0,0,0,6,0,0,3],
        [0,0,6,0,4,0,0],
        [1,1,0,4,0,0,0],
        [4,1,0,0,0,0,0],
        [0,15,3,0,0,0,0]]

graph1 = Graph(edges)

print(graph1.neighbours(2))
