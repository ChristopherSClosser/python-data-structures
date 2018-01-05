"""Implement a graph."""


class Graph(object):
    """Graph data structure."""

    def __init__(self):
        """."""
        self._nodes = []
        self.list_nodes = []
        self._edges = []
        self.list_edges = []

    def nodes(self):
        """Return list of nodes."""
        nodes = []
        for node in self._nodes:
            nodes.append(node.val)
        return nodes

    def edges(self):
        """Return list of edges."""
        return self._edges

    def add_node(self, val):
        """."""
        for node in self.list_nodes:
            if node.val == val:
                return "Nodes must have unique values"
        self.list_nodes.append(Node(val))
        self._nodes.append(val)

    def add_edge(self, val1, val2, weight=0):
        """Add a connection between two nodes, val1 points to val2."""
        if not isinstance(weight, (int, float)):
            return 'weight must be int or float'
        node1 = 0
        node2 = 0
        for node in self.list_nodes:
            if node.val == val1:
                node1 = node
            if node.val == val2:
                node2 = node
        if node1 == 0:
            node1 = Node(val1)
            self.list_nodes.append(node1)
        if node2 == 0:
            node2 = Node(val2)
            self.list_nodes.append(node2)
        if node1 == node2:
            return "You cannot connect a node to itself"
        for edge in self.list_edges:
            if edge == (node1, node2, weight):
                return 'Edge already exists'
        node1.neighbors.append((node1, node2, weight))
        node2.neighbors.append((node1, node2, weight))
        self.list_edges.append((node1, node2, weight))

    def del_node(self, val):
        """Delete and remove edges."""
        del_node = self.has_node(val)
        if not del_node:
            return 'node not found'
        self.list_nodes.remove(del_node)

        for edge in self.list_edges:
            if del_node.val == edge[0].val or del_node.val == edge[1].val:
                self.list_edges.remove(edge)
        for node in self.list_nodes:
            for neighbor in node.neighbors:
                if del_node.val == neighbor[0].val or del_node.val == neighbor[1].val:
                    node.neighbors.remove(neighbor)

    def del_edge(self, val1, val2):
        """Remove an edge."""
        for edge in self.list_edges:
            if edge[0].val == val1 and edge[1].val == val2:
                self.list_edges.remove(edge)
                del_node1 = edge[0]
            else:
                return 'edge not found'
        for node in self.list_nodes:
            for neighbor in node.neighbors:
                if del_node1.val == neighbor[0].val or del_node1.val == neighbor[1].val:
                    node.neighbors.remove(neighbor)

    def has_node(self, val):
        """Return the node if found."""
        for node in self.list_nodes:
            if node.val == val:
                return node

    def neighbors(self, val):
        """Return list of neighbors for the given node."""
        node = self.has_node(val)
        return node.neighbors

    def adjacent(self, val1, val2):
        """Return True if edge exists."""
        for edge in self.list_edges:
            if edge[0].val == val1 and edge[1].val == val2:
                return True
            else:
                return False

    def depth_first_traversal(self, start_val):
        """."""
        if not self.has_node(start_val):
            return 'node not found'
        current = self.has_node(start_val)
        res = [current.val]
        unvisited = []
        for neighbor in current.neighbors:
            if neighbor[0] == current:
                unvisited.append(neighbor[1])

        while unvisited:
            current = unvisited[-1]
            unvisited.remove(current)
            if current.val not in res:
                res.append(current.val)
            for neighbor in current.neighbors:
                if neighbor[0] == current:
                    if not neighbor[1].val in res:
                        unvisited.append(neighbor[1])
        return res

    def breadth_first_traversal(self, start_val):
        """."""
        if not self.has_node(start_val):
            return 'node not found'
        current = self.has_node(start_val)
        res = [current.val]
        unvisited = []
        for neighbor in current.neighbors:
            if neighbor[0] == current:
                unvisited.append(neighbor[1])

        while unvisited:
            current = unvisited[0]
            unvisited.remove(current)
            if current.val not in res:
                res.append(current.val)
            for neighbor in current.neighbors:
                if neighbor[0] == current:
                    if not neighbor[1].val in res:
                        unvisited.append(neighbor[1])
        return res

    def dijkstra(self, start, end):
        """Find all shortest distances between start and end nodes using Dijkstra."""
        start = self.has_node(start)
        if not start:
            raise KeyError('Graph does not contain start node.')
        end = self.has_node(end)
        if not end:
            raise KeyError('Graph does not contain end node.')
        if not len(self._edges):
            raise KeyError('No edges in this graph.')

        current = start
        visited = {}
        unvisited = {node: float("inf") for node in self._nodes}
        paths = {node: '' for node in self._nodes}
        unvisited[current] = 0
        edges = {(edge[0], edge[1]): edge[2] for edge in self._edges}

        while end not in visited or min(unvisited.values()) == float("inf"):
            origin = current
            for node in unvisited:
                if (current, node) in edges:
                    weight = (unvisited[current] +
                              edges[(current, node)])
                    if unvisited[node] > weight:
                        unvisited[node] = weight
                        paths[node] = origin
            visited[current] = min(unvisited.values())
            del unvisited[current]

            if len(unvisited):
                current = min(unvisited.keys(), key=unvisited.get)
            else:
                break

        if visited[end] == float("inf"):
            raise IndexError('There is no path between those nodes.')

        curr = end
        path = []
        while start not in path:
            path.insert(0, curr)
            curr = paths[curr]

        return path

    def bellman(self, start, end):
        """"Find the shortest path using bellman ford algorithm."""
        start = self.has_node(start)
        if not start:
            raise KeyError('Graph does not contain start node.')
        end = self.has_node(end)
        if not end:
            raise KeyError('Graph does not containend node.')
        if not len(self._edges):
            raise KeyError('No edges in this graph.')

        iterations = len(self.edges()) - 1
        unvisited = self._nodes[:]
        unvisited.remove(start)
        unvisited.insert(0, start)
        paths = {node: [float("inf"), ''] for node in self._nodes}
        prev_paths = {node: [paths[node][0], paths[node][1]] for node in paths}
        changing = True
        overlap = []
        paths[start][0] = 0
        edges = self.edges()
        while iterations >= 0 and changing:
            for node in unvisited:
                if paths[node][0] != float("inf"):
                    for edge in edges:
                        if edge[0] == node and edge[1] != start:
                            if paths[node][0] + edge[2] < paths[edge[1]][0]:
                                paths[edge[1]][0] = paths[node][0] + edge[2]
                                paths[edge[1]][1] = node
            for node in self._nodes:
                if paths[node][0] == prev_paths[node][0]:
                    overlap.append(node)
            if len(overlap) == len(self._nodes):
                changing = False
            overlap = []
            prev_paths = paths
            iterations -= 1
        if paths[end][0] == float("inf"):
            raise IndexError('There is no path between nodes.')
        curr = end
        path = []
        while paths[curr][1]:
            path.insert(0, curr)
            curr = paths[curr][1]
        path.insert(0, start)
        return path


class Node(object):
    """Graph node."""

    def __init__(self, val):
        """."""
        self.val = val
        self.neighbors = []


if __name__ == '__main__':  # pragma no cover
    g1 = Graph()
    g1.add_edge(1, 2)
    g1.add_edge(1, 3)
    g1.add_edge(2, 4)
    g1.add_edge(2, 5)
    g1.add_edge(3, 6)
    g1.add_edge(3, 7)

    print("traversal of a normal graph")
    print("depth first traversal, ", g1.depth_first_traversal(1))
    print("breadth first traversal, ", g1.breadth_first_traversal(1))

    g2 = Graph()
    g2.add_edge(1, 2)
    g2.add_edge(1, 3)
    g2.add_edge(1, 4)
    g2.add_edge(2, 5)
    g2.add_edge(2, 6)
    g2.add_edge(5, 8)
    g2.add_edge(8, 10)
    g2.add_edge(4, 7)
    g2.add_edge(7, 9)

    print("traversal of an unbalanced graph")
    print("depth first traversal, ", g2.depth_first_traversal(1))
    print("breadth first traversal, ", g2.breadth_first_traversal(1))

    g3 = Graph()
    g3.add_edge(1, 2)
    g3.add_edge(1, 3)
    g3.add_edge(2, 4)
    g3.add_edge(2, 5)
    g3.add_edge(4, 6)
    g3.add_edge(6, 2)
    g3.add_edge(3, 7)
    g3.add_edge(4, 7)

    print("traversal of an circular graph")
    print("depth first traversal, ", g3.depth_first_traversal(1))
    print("breadth first traversal, ", g3.breadth_first_traversal(1))
