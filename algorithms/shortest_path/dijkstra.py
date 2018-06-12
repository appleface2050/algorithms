from collections import defaultdict


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance


def dijsktra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            if not graph.distances.get((min_node, edge)):
                continue
            weight = current_weight + graph.distances[(min_node, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path


if __name__ == '__main__':
    g = Graph()
    g.add_node(0)
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_node(4)
    g.add_node(5)
    g.add_node(6)
    g.add_node(7)
    g.add_node(8)
    g.add_node(9)
    g.add_node(10)
    g.add_node(11)
    g.add_node(12)


    g.add_edge(2, 3, 4)
    g.add_edge(0, 6, 3)
    g.add_edge(0, 1, 3)
    g.add_edge(2, 0, 2)
    g.add_edge(11, 12, 1)
    g.add_edge(9, 12, 9)
    g.add_edge(9, 10, 7)
    g.add_edge(9, 11, 7)
    g.add_edge(3, 5, 1)
    g.add_edge(8, 7, 9)
    g.add_edge(5, 4, 8)
    g.add_edge(0, 5, 3)
    g.add_edge(6, 4, 4)
    g.add_edge(6, 9, 1)
    g.add_edge(7, 6, 10)

    dijsktra(g,0)