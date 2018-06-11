"""
    breadth_first_search.py

    Iterative implementation of BFS algorithm on a graph.

    Breadth First Search Overview:
    ------------------------
    Used to traverse trees, tree structures or graphs.
    Starts at a selected node (root) and explores the nearest
    neighbor branches before proceeding further.

    Time Complexity: O(E + V)
        E = Number of edges
        V = Number of vertices (nodes)

    Pseudocode: https://en.wikipedia.org/wiki/Breadth-first_search
"""
from algorithms.data_structures.digraph import Digraph


def bfs(graph, start):
    if start not in graph or graph[start] is None or graph[start] == []:
        return None
    # visited, queue = set(), [start]
    visited, queue = [], [start]       #使用set的话是不知道顺序的
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            # visited.add(vertex)
            visited.append(vertex)
            # queue.extend(graph[vertex] - visited)
            for item in visited:
                if item in graph[vertex]:
                    graph[vertex].remove(item)
                queue.extend(graph[vertex])
    return visited


if __name__ == '__main__':
    g = Digraph()
    g.add_edge(2, 3)
    g.add_edge(0, 6)
    g.add_edge(0, 1)
    g.add_edge(2, 0)
    g.add_edge(11, 12)
    g.add_edge(9, 12)
    g.add_edge(9, 10)
    g.add_edge(9, 11)
    g.add_edge(3, 5)
    g.add_edge(8, 7)
    g.add_edge(5, 4)
    g.add_edge(0, 5)
    g.add_edge(6, 4)
    g.add_edge(6, 9)
    g.add_edge(7, 6)
    print g
    print bfs(g.get_adj(), 2)
