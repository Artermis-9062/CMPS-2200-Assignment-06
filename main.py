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
    frontier = []
    heappush(frontier, (0, 0, source))  # (weight, num_edges, vertex)
    res = {}
    while frontier:
        curr_length, num_step, vertex = heappop(frontier)
        if vertex in res:
            continue  # already finalized, skip
        res[vertex] = (curr_length, num_step)
        for neighbor, weight in graph[vertex]:
            if neighbor not in res:
                heappush(frontier, (curr_length + weight, num_step + 1, neighbor))
    return res


def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of
      that vertex in the shortest path tree.
    """
    frontier = deque(
        (neighbor, source) for neighbor in graph[source]
    )  # Make frontier is a deque of tuple (neighbor, parent)
    visited = set([source])
    res = dict()
    while frontier:
        vertex, parent = frontier.popleft()
        if vertex not in visited:
            res[vertex] = parent
            visited.add(vertex)
            for curr_vertex_neighbor in graph[vertex]:
                if curr_vertex_neighbor not in visited:
                    frontier.append((curr_vertex_neighbor, vertex))
    return res


def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node
      (excluding the destination node itself). See test_get_path for an example.
    """
    path = ""
    key = destination
    while parents.get(key) is not None:
        path = parents[key] + path
        key = parents[key]
    return path
