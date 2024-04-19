from collections import deque
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

    def get_adjacent_vertices(self, v):
        #debated iterating vertically and then adding vertex based on row number, but remember something about indexing vertically
        #takes longer than indexing horizontally related to the way stored in memory
        ret = []
        counter = 0
        for i in self.graph[v]:
            if i != 0:
                ret.append(counter)
            
            counter += 1
        return ret
        


        
    def degree(self, v):
        if not self.directed:
            return len(self.graph[v]) - self.graph[v].count(0)
        else:
            out_degree = len(self.graph[v]) - self.graph[v].count(0)
            in_degree = 0
            for i in self.graph:
                if i[v] != 0:
                    in_degree += 1
            
            return in_degree, out_degree
        
    def is_directly_connected(self, u, v):
        return self.graph[u][v] != 0

    #level order traversal, assume there are cycles
    def bfs(self, v):
        visited = [False] * len(self.graph[v])
        def helper(v):
            queue = deque([v])
            
            counter = 0
            while queue:
                for j in range(len(queue)):
                    cur = queue.popleft()
                    visited[cur] = True
                    ret = []
                    for i in self.get_adjacent_vertices(cur):
                        if visited[i] == False:
                            queue.append(i)
                            ret.append(i)
                counter += 1
                print(v, str(counter), ret)

        helper(v)


    def dfs(self, u, v):

        
        
    def print_graph(self):
        for i in self.graph:
            for j in i:
                print(str(j), end = " ")
            print()
        print()

test_graph = Graph(5, True)
test_graph.add_edge(1,2)
test_graph.add_edge(3,4)
test_graph.add_edge(4,1)
test_graph.add_edge(4,0)
test_graph.add_edge(3,2)
test_graph.add_edge(2,3)
test_graph.add_edge(0,3)
test_graph.print_graph()
test_graph.remove_edge(0,3)
test_graph.print_graph()
print(test_graph.get_adjacent_vertices(3))
print(test_graph.degree(3))
print(test_graph.degree(1))
test_graph.bfs(3)
print()

#shouldn't write like this, go more toward test based

