from collections import deque
from typing import List, Tuple, Optional
#this would be for undirected, for directed would just edit the add_edge method to create an edge one way
class Graph:
    def __init__(self, vertices: int, directed: bool) -> None:
        self.vertices = vertices
        self.graph = [[0 for _ in range(vertices)] for i in range(vertices)]
        self.directed = directed

    def add_edge(self, u: int, v: int, weight: int=1) -> None:
        
        if u >= len(self.graph) or v >= len(self.graph) or u < 0 or v < 0:
            raise ValueError("Invalid vertex")
        self.graph[u][v] = weight
        
        if not self.directed: 
            self.graph[v][u] = weight

    def remove_edge(self, u: int, v:int) -> None:
        if u >= len(self.graph) or v >= len(self.graph) or u < 0 or v < 0:
            raise ValueError("Invalid vertex") 
        self.graph[u][v] = 0
        
        if not self.directed:
            self.graph[v][u] = 0

    def get_adjacent_vertices(self, v:int) -> List[int]:
        #debated iterating vertically and then adding vertex based on row number, but remember something about indexing vertically
        #takes longer than indexing horizontally related to the way stored in memory
        ret = []
        counter = 0
        for i in self.graph[v]:
            if i != 0:
                ret.append(counter)
            
            counter += 1
        return ret
        


        
    def degree(self, v:int) -> Tuple[int, int]:
        '''can increase the time complexity from O(N) to O(1) by keeping two lists with len(graph) vertices and adding/subtracting when the
        add and remove methods are called'''
        if not self.directed:
            return len(self.graph[v]) - self.graph[v].count(0)
        else:
            out_degree = len(self.graph[v]) - self.graph[v].count(0)
            in_degree = 0
            for i in self.graph:
                if i[v] != 0:
                    in_degree += 1
            
            return in_degree, out_degree
        
    def is_directly_connected(self, u:int, v:int) -> bool:
        return self.graph[u][v] != 0

    #level order traversal, assume there are cycles
    def bfs(self, v:int) -> None:
        visited = [False] * self.vertices
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


    def dfs(self, u, v, visited=None):
        if visited == None:
        
            visited = [False] * self.vertices
        visited[u] = True
        if u == v:
            return True
        for i in self.get_adjacent_vertices(u):
            if visited[i] != True:
               
                if self.dfs(i, v, visited): #if we've found the path, return True everywhere
                    return True
                
        return False

        
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
print(test_graph.dfs(3, 0))
print()

#shouldn't write like this, go more toward test based

