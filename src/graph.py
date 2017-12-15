"""Implement a graph."""

import pdb


class Graph(object):
    """Graph data structure."""

    def __init__(self):
        """."""
        self._nodes = []
        self.list_nodes = []
        self._edges = []
        self.list_edges = []

    def nodes(self):
        """."""
        return self._nodes

    def edges(self):
        """."""
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
            # import pdb; pdb.set_trace()
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
            # import pdb; pdb.set_trace()
            if current.val not in res:
                res.append(current.val)
            for neighbor in current.neighbors:
                if neighbor[0] == current:
                    if not neighbor[1].val in res:
                        unvisited.append(neighbor[1])
        return res


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
