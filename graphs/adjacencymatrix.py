
#this would be for undirected, for directed would just edit the add_edge method to create an edge one way
class Graph:
    def __init__(self, vertices, directed):
        self.vertices = vertices
        self.graph = [[0 for _ in range(vertices)] for i in range(vertices)]
        self.directed = directed

    def add_edge(self, u, v, weight=1):
        
        if u >= len(self.graph) or v >= len(self.graph) or u < 0 or v < 0:
            return "can't call that" 
        self.graph[u][v] = weight
        
        if not self.directed: 
            self.graph[v][u] = weight

    def remove_edge(self, u, v):
        if u >= len(self.graph) or v >= len(self.graph) or u < 0 or v < 0:
            return "can't call that" 
        self.graph[u][v] = 0
        
        if not self.directed:
            self.graph[v][u] = 0

    def get_adjacent_vertices(v):
        
        
    def degree(self, v):
        return len(self.graph[v]) - self.graph[v].count(0)
        
    def is_connected(self, u, v):
        return self.graph[u][v] != 0

    def bfs(self, v):
        pass
    
    def dfs(self, v):
        pass
    
    def print_graph(self):
        for i in self.graph:
            for j in i:
                print(str(j), end = " ")
            print()

test_graph = Graph(5)
test_graph.add_edge(1,2)
test_graph.add_edge(3,4)
test_graph.print_graph()


