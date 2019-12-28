from Graph import Graph
def dijkstra(graph, source):
    distance = {}
    unvisited = []
    for i in range(graph.get_number_of_vertices()):
        distance[i] = 1000
        unvisited.append(i)
    distance[source] = 0
    print(distance)
    print(unvisited)
    
    while len(unvisited) > 0:
        current_node = min(distance, key=distance.get) # Should get ID number of source node on first loop
        print(current_node)
        unvisited.remove(current_node)
        neighbours = graph.neighbours(current_node)
        for neighbour in neighbours:
            if neighbour in unvisited:
                a = distance[current_node] + graph.get_edge_value(current_node,neighbour)
                if a < distance[neighbour]:
                    distance[neighbour] = a
    #current error being caused by current_node always switching to node with lowest distance value after first loop.
    #this causes code to choose source node again, need to change code so it doesn't change current_node to node that has
    #been visited

    
edges = [[0,0,0,0,1,4,0],
        [0,0,0,0,1,1,15],
        [0,0,0,6,0,0,3],
        [0,0,6,0,4,0,0],
        [1,1,0,4,0,0,0],
        [4,1,0,0,0,0,0],
        [0,15,3,0,0,0,0]]

graph1 = Graph(edges)

dijkstra(graph1,2)
