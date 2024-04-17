
#this would be for undirected, for directed would just edit the add_edge method to create an edge one way
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for _ in range(vertices)] for i in range(vertices)]

    def add_edge(self, u, v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1

    def print_graph(self):
        for i in self.graph:
            for j in i:
                print(str(j), end = " ")
            print()

test_graph = Graph(5)
test_graph.add_edge(1,2)
test_graph.add_edge(3,4)
test_graph.print_graph()


