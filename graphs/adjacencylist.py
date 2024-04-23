
from collections import defaultdict
from typing import List, Tuple, Optional, Set
from collections import deque
#I get the reason to use self, but how does this object reference really work under the hood? Im confused
#what does typing do 
#can I use decorators here? whats the point
#weighted would be a tuple stored? Yes
class Graph:
    def __init__(self, directed: bool) -> None:
        """Initialize adjacency set"""
        self.adj_list = defaultdict(set)
        self.directed = directed
        

    def add_edge(self, u: int ,v: int, weight: int =1) -> None:
        """Initialize edge based on whether graph is directed"""
        self.adj_list[u].add((v, weight))
        if not self.directed:
            self.adj_list[v].add((u, weight))
            
    
    def remove_edge(self, u:int, v:int) -> None:

        """Remove edge based on whether graph is directed"""
        if u in self.adj_list:
            for i in self.adj_list[u]:
                if i[0] == v:
                    self.adj_list[u].remove(v)
            if not self.directed:
                for i in self.adj_list[v]:
                    if i[0] == u:
                        self.adj_list[v].remove(u)
        
        else:
            return f"the vertex {u} is not in the graph"
        
        return f"the vertex from {u} to {v} has been removed"

    def get_adjacent_vertices(self, u: int) -> Set:
        """get all adjacent vertices to given vertex"""
        return self.adj_list[u]
    
    def degree(self, u: int) -> int:
        """return number of edges connected to a vertex"""
        if not self.directed:
            return len(self.get_adjacent_vertices(u))
        else:
            #come back to this
            out = len(self.get_adjacent_vertices(u))
            #in = 
    #account for cycles and 
    def bfs(self, u: int, v: int) -> str:
        """"""
        if u not in self.adj_list:
            return f"{u} does not exist"
        queue = deque([(u, 0)])
        counter = 0
        visited = set()
        while queue:
            for j in range(len(queue)):
                counter += 1
                cur = queue.pop()
                visited.add(cur)
                for i in self.adj_list[cur[0]]:
                    if i[0] == v:
                        return f"Distance from {u} to {v} is {counter}"
                    if i not in visited:
                        queue.append(i)
        return f"{u} to {v} is unreachable"

    #check if path exists
    def dfs(self, u: int, v: int, visited: List=None) -> None:
        if visited is None:
            visited = set()
        visited.add(u)
        if u == v:
            return True
        for i in self.adj_list[u]:
            if i[0] not in visited:
                if self.dfs(i[0], v, visited):
                    return True
        return False


        

    def print_graph(self) -> None:
        for i in self.adj_list:
            print(f"{i} is connected to {self.adj_list[i]}")
    


test_graph = Graph(False)

test_graph.add_edge(2,3)
test_graph.add_edge(2,4)
test_graph.add_edge(4,5)
test_graph.add_edge(1,0)
print(test_graph.bfs(5, 3))
print(test_graph.bfs(6, 3))
print(test_graph.bfs(1,3))
print(test_graph.dfs(5, 3))
print(test_graph.dfs(1, 3))
test_graph.print_graph()
#what happens if you do print_graph instead of print_graph()