from Graph import Graph
def dijkstra(graph, start):
    distance = []
    previous = []
    for i in range(graph.get_number_of_vertices()):
        distance.append(1000) # Distance to each node is set to "infinite"
        previous.append(-1) # Previous node for each vertex is set to "undefined"
    distance[start - 1] = 0 # Distance to start node is 0
    nodes = []
    for i in range(graph.get_number_of_vertices()): # Create list of nodes
        nodes.append(i)
        
    return











































edges = [[0,0,0,0,1,4,0],
        [0,0,0,0,1,1,15],
        [0,0,0,6,0,0,3],
        [0,0,6,0,4,0,0],
        [1,1,0,4,0,0,0],
        [4,1,0,0,0,0,0],
        [0,15,3,0,0,0,0]]

graph1 = Graph(edges)

print(graph1.neighbours(2))

print(graph1.get_edge_value(1,6))

dijkstra(graph1, 1)
