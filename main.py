from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    # count, weight = 0
    frontier = []
    heappush(frontier, (0, source))
    res = {source:(0, 0)}
    visited = set([source])
    vertex = source
    while len(visited) != len(graph.keys()):
        last_vertex = vertex
        weight, vertex = heappop(frontier)
        for pair in graph[vertex]:
          if pair[0] != visited:
            heappush(frontier,(graph[pair[0]][1], graph[pair[0]][0]))
        res[vertex] = min(1 ,(res[last_vertex][0] + weight, res[last_vertex][1] + 1))
        visited.add(vertex)
    return res

def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    ###TODO
    pass
    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    ###TODO
    pass
