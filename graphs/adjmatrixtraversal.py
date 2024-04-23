import adjacencymatrix
from collections import deque


  


    




new_graph = adjacencymatrix.Graph(5, False)
new_graph.add_edge(3,4)
new_graph.add_edge(1,2)
new_graph.add_edge(3,2)
new_graph.bfs(4,1)
new_graph.print_graph()