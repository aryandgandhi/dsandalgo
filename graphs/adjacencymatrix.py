
#this would be for undirected, for directed would just edit the add_edge method to create an edge one way
#what about weighted? can store the weights in the graph, so for each edge take in a weight and set it accordingly
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for _ in range(vertices)] for i in range(vertices)]

    def add_edge(self, u, v):
        self.graph[u][v] = 1
        #can remove below for directed
        self.graph[v][u] = 1

    #weighted and directed add_edge: 
    # def add_edge(self, u, v, weight):
    #     self.graph[u][v] = weight

    def 

    def print_graph(self):
        for i in self.graph:
            for j in i:
                print(str(j), end = " ")
            print()

test_graph = Graph(5)
test_graph.add_edge(1,2)
test_graph.add_edge(3,4)
test_graph.print_graph()


