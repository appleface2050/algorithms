# coding=utf-8

"""
    Depth First Search
    ------------------
    Recursive implementation of the depth first search algorithm used to
    traverse trees or graphs. Starts at a selected node (root) and explores the
    branch as far as possible before backtracking.

    Time Complexity: O(E + V)

        E = Number of edges

        V = Number of vertices (nodes)

    Pseudocode: https://en.wikipedia.org/wiki/Depth-first_search
"""
from algorithms.data_structures.digraph import Digraph

def dfs(graph, start, path=[]):
    """
    Depth first search that recursively searches the path. Backtracking occurs
    only when the last node in the path is visited.

    :param graph: A dictionary of nodes and edges.
    :param start: The node to start the recursive search with.
    :param path: A list of edges to search.
    :rtype: A boolean indicating whether the node is included in the path.

    """
    if start not in graph or graph[start] is None or graph[start] == []:
        return None
    path = path + [start]
    # print path
    for edge in graph[start]:
        # print path
        if path and (edge not in path):
            path = dfs(graph, edge, path)
    return path

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
    print dfs(g.get_adj(), 0)

    # graph = {
    #     'A': ['B', 'C', 'E'],
    #     'B': ['A', 'D', 'F'],
    #     'C': ['A', 'G'],
    #     'D': ['B'],
    #     'F': ['B'],
    #     'E': ['A'],
    #     'G': ['C']
    # }
    # print dfs(graph, "A")