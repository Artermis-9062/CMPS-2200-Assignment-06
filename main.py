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
    count, weight = 0
    frontier = set((source, 0))
    res = dict(tuple)
    visited = set()

    while len(visited) != len(graph.keys()):
        vertex = frontier.pop()
        for node in graph[vertex][0]:
          if node != visited:
            frontier.update(graph[vertex])
        if vertex[0] != visited:
            res[vertex] = 

            visited.add(vertex[0])
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
