"""Test graph."""

import pytest
from graph import Graph, Node
import pdb


@pytest.fixture
def new_graph():
    """Make graph to play with."""
    return Graph()


@pytest.fixture
def new_node():
    """A node."""
    return Node(1)


def test_new_emty_graph__nodes(new_graph):
    """Test_new_emty_graph__nodes."""
    assert new_graph._nodes == []


def test_new_emty_graph_nodes(new_graph):
    """Test_new_emty_graph_nodes."""
    assert new_graph.nodes() == []


def test_new_emty_graph__edges(new_graph):
    """Test_new_emty_graph__edges."""
    assert new_graph._edges == []


def test_new_emty_graph_edges(new_graph):
    """Test_new_emty_graph_edges."""
    assert new_graph.edges() == []


def test_node_neighbors(new_node):
    """Test_node_neighbors."""
    assert new_node.neighbors == []


def test_del_node_doesnt_exist(new_graph):
    """Test_del_node_doesnt_exist."""
    assert new_graph.del_node(2) == 'node not found'


def test_insert_1node(new_graph):
    """Test_insert_1node."""
    new_graph.add_node(1)
    assert new_graph._nodes[0].val == 1


def test_newgraph_scope(new_graph):
    """Test fixture."""
    assert new_graph._nodes == []


def test_insert_duplicate_node_raises_error(new_graph):
    """Test_insert_duplicate_node_raises_error."""
    new_graph.add_node(1)
    assert new_graph.add_node(1) == "Nodes must have unique values"


def test_add_edge_empty_graph_makes_nodes(new_graph):
    """Should make two new nodes and add to nodes list."""
    new_graph.add_edge(1, 2)
    assert len(new_graph._nodes) == 2


def test_add_edge_empty_graph_makes_edge(new_graph):
    """Should add an edge."""
    new_graph.add_edge(1, 2)
    assert new_graph._edges[0][0].val == 1
    assert new_graph._edges[0][1].val == 2


def test_add_edge_existing_nodes(new_graph):
    """Test_add_edge_existing_nodes."""
    new_graph.add_node(1)
    new_graph.add_node(2)
    new_graph.add_edge(1, 2)
    assert new_graph._edges[0][0].val == 1
    assert new_graph._edges[0][1].val == 2


def test_add_edge_same_node_error(new_graph):
    """Won't make circular edge to same node."""
    new_graph.add_node(1)
    new_graph.add_node(2)
    assert new_graph.add_edge(1, 1) == "You cannot connect a node to itself"


def test_add_existing_edge(new_graph):
    """Test_add_existing_edge."""
    new_graph.add_node(1)
    new_graph.add_node(2)
    new_graph.add_edge(1, 2)
    assert new_graph.add_edge(1, 2) == 'Edge already exists'


def test_add_existing_edge_reversed(new_graph):
    """Test_add_existing_edge_reversed."""
    new_graph.add_node(1)
    new_graph.add_node(2)
    new_graph.add_edge(1, 2)
    new_graph.add_edge(2, 1)
    assert new_graph._edges[1][0].val == 2
    assert new_graph._edges[1][1].val == 1


def test_add_edge_existing_node(new_graph):
    """Test_add_edge_existing_nod."""
    new_graph.add_node(1)
    new_graph.add_edge(1, 2)
    assert new_graph._edges[0][0].val == 1
    assert new_graph._edges[0][1].val == 2


def test_del_node_deletes_nodes(new_graph):
    """Test_del_node_deletes_nodes."""
    new_graph.add_node(1)
    new_graph.del_node(1)
    assert new_graph._nodes == []


def test_del_node_deletes_node_1(new_graph):
    """Test_del_node_deletes_node_1."""
    new_graph.add_node(1)
    new_graph.add_node(2)
    new_graph.del_node(1)
    assert new_graph._nodes[0].val == 2


def test_del_node_deltes_edge(new_graph):
    """Test_del_node_deltes_edge."""
    ng = Graph()
    ng.add_edge(1, 2)
    ng.del_node(1)
    assert ng._edges == []


def test_del_node_deltes_neighbor(new_graph):
    """Test_del_node_deltes_neighbor."""
    ng = Graph()
    ng.add_edge(1, 2)
    node1 = ng._nodes[0]
    node2 = ng._nodes[1]
    assert node1.neighbors[0][0].val == node1.val
    assert node1.neighbors[0][1].val == node2.val


def test_only_one_edge(new_graph):
    """Test_only_one_edge."""
    ng = Graph()
    ng.add_edge(1, 2)
    node1 = ng._nodes[0]
    with pytest.raises(IndexError):
        print(node1.neighbors[1][0].val)


def test_neighbors_function_returns_list_of_neighbors(new_graph):
    """Test_neighbors_function_returns_list_of_neighbors."""
    ng = Graph()
    ng.add_edge(1, 2)
    node1 = ng._nodes[0]
    nlist = ng.neighbors(1)
    assert nlist[0][0] == node1


def test_adjacent_returns_true(new_graph):
    """Test_adjacent_returns_true."""
    ng = Graph()
    ng.add_edge(1, 2)
    assert ng.adjacent(1, 2) is True


def test_remove_edge(new_graph):
    """Test_remove_edge."""
    ng = Graph()
    ng.add_edge(1, 2)
    ng.del_edge(1, 2)
    assert ng._edges == []


def test_nodes(new_graph):
    """Test_remove_edge."""
    ng = Graph()
    ng.add_edge(1, 2)
    assert ng.nodes() == [1, 2]


def test_remove_edge_not_exist():
    """Test_remove_edge_not_exist."""
    ng = Graph()
    ng.add_edge(1, 2)
    assert ng.del_edge(2, 3) == 'edge not found'


def test_adjacent_returns_false_edge_not_exist():
    """Test_adjacent_returns_false_edge_not_exist."""
    ng = Graph()
    ng.add_edge(1, 2)
    assert ng.adjacent(2, 3) is False


def test_remove_edge_also_removes_neighbors():
    """Test_remove_edge_also_removes_neighbors."""
    ng = Graph()
    ng.add_edge(1, 2)
    node1 = ng._nodes[0]
    ng.del_edge(1, 2)
    assert node1.neighbors == []


def test_graph_depth_first():
    """Test_graph_depth_first."""
    ng = Graph()
    ng.add_edge(1, 2)
    assert ng.depth_first_traversal(1) == [1, 2]


def test_graph_depth_first_node_not_found():
    """Test_graph_depth_first_node_not_found."""
    ng = Graph()
    ng.add_edge(1, 2)
    assert ng.depth_first_traversal(3) == 'node not found'


def test_graph_breadth_first_node_not_found():
    """Test_graph_breadth_first_node_not_found."""
    ng = Graph()
    ng.add_edge(1, 2)
    assert ng.breadth_first_traversal(3) == 'node not found'


def test_graph_depth_first_large():
    """Test_graph_depth_first_large."""
    ng = Graph()
    ng.add_edge(1, 2)
    ng.add_edge(1, 7)
    ng.add_edge(1, 8)
    ng.add_edge(8, 9)
    ng.add_edge(8, 12)
    ng.add_edge(9, 10)
    ng.add_edge(9, 11)
    ng.add_edge(2, 6)
    ng.add_edge(2, 3)
    ng.add_edge(3, 4)
    ng.add_edge(3, 5)
    assert ng.depth_first_traversal(1) == [1, 8, 12, 9, 11, 10, 7, 2, 3, 5, 4, 6]


@pytest.fixture
def ng():
    """Non weighted graph."""
    ng = Graph()
    ng.add_edge(1, 2)
    ng.add_edge(1, 3)
    ng.add_edge(2, 4)
    ng.add_edge(2, 5)
    ng.add_edge(3, 6)
    ng.add_edge(3, 7)
    ng.add_edge(4, 8)
    ng.add_edge(4, 9)
    ng.add_edge(5, 10)
    ng.add_edge(5, 11)
    ng.add_edge(6, 12)
    ng.add_edge(6, 13)
    ng.add_edge(7, 14)
    ng.add_edge(7, 15)
    return ng


def test_graph_depth_first_large_2(ng):
    """Test_graph_depth_first_large_2."""
    assert ng.depth_first_traversal(1) == [1, 3, 7, 15, 14, 6, 13, 12, 2, 5, 11, 10, 4, 9, 8]


def test_circular():
    """Test_circular."""
    ng = Graph()
    ng.add_edge(1, 2)
    ng.add_edge(1, 3)
    ng.add_edge(3, 1)
    assert ng.depth_first_traversal(1) == [1, 3, 2]


def test_circular_more_complex():
    """Test_circular_more_complex."""
    ng = Graph()
    ng.add_edge(1, 2)
    ng.add_edge(1, 3)
    ng.add_edge(3, 5)
    ng.add_edge(5, 2)
    ng.add_edge(3, 4)
    ng.add_edge(4, 3)
    ng.add_edge(2, 4)
    assert ng.depth_first_traversal(1) == [1, 3, 4, 5, 2]


def test_graph_breadth_first_large(ng):
    """Test_graph_breadth_first_large."""
    assert ng.breadth_first_traversal(1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


def test_graph_breadth_first_unbalanced():
    """Test_graph_breadth_first_unbalanced."""
    ng = Graph()
    ng.add_edge(1, 2)
    ng.add_edge(1, 3)
    ng.add_edge(1, 4)
    ng.add_edge(2, 5)
    ng.add_edge(2, 6)
    ng.add_edge(5, 8)
    ng.add_edge(8, 10)
    ng.add_edge(4, 7)
    ng.add_edge(7, 9)
    assert ng.breadth_first_traversal(1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_graph_breadth_first_unbalanced_different_order():
    """Test_graph_breadth_first_unbalanced_different_order."""
    ng = Graph()
    ng.add_edge(8, 10)
    ng.add_edge(1, 2)
    ng.add_edge(7, 9)
    ng.add_edge(1, 4)
    ng.add_edge(2, 5)
    ng.add_edge(2, 6)
    ng.add_edge(5, 8)
    ng.add_edge(1, 3)
    ng.add_edge(4, 7)
    assert ng.breadth_first_traversal(1) == [1, 2, 4, 3, 5, 6, 7, 8, 9, 10]


def test_graph_breadth_first_large_start_at_2(ng):
    """Test_graph_breadth_first_large_start_at_2."""
    assert ng.breadth_first_traversal(2) == [2, 4, 5, 8, 9, 10, 11]


def test_graph_depth_first_large_2_start_at_2(ng):
    """Test_graph_depth_first_large_2_start_at_2."""
    assert ng.depth_first_traversal(2) == [2, 5, 11, 10, 4, 9, 8]


def test_zero_edge_weight():
    """Test default weight."""
    ng = Graph()
    ng.add_edge(1, 2)
    assert ng._edges[0][2] == 0


def test_edge_weight():
    """Test correct weight."""
    ng = Graph()
    ng.add_edge(1, 2, 1)
    assert ng._edges[0][2] == 1


def test_edge_weight_not_num():
    """Test incorrect weight."""
    ng = Graph()
    assert ng.add_edge(1, 2, 'qwoei') == 'weight must be int or float'


def test_add_duplicate_node():
    """Test_add_duplicate_node."""
    ng = Graph()
    ng.add_node(1)
    assert ng.add_node(1) == "Nodes must have unique values"


def test_graph_dijkstra_lenght(ng):
    """Test_graph_dijkstra_lenght."""
    path = ng.dijkstra(1, 15)
    assert len(path) == 4


def test_graph_dijkstra_first_val(ng):
    """test_graph_dijkstra_first_val."""
    path = ng.dijkstra(1, 15)
    assert path[0].val == 1


def test_graph_dijkstra_end_val(ng):
    """test_graph_dijkstra_end_val."""
    path = ng.dijkstra(1, 15)
    assert path[3].val == 15


@pytest.fixture
def wng():
    """Weighted graph."""
    ng = Graph()
    ng.add_edge(1, 2, 5)
    ng.add_edge(1, 3, 9)
    ng.add_edge(2, 4)
    ng.add_edge(2, 5, 5)
    ng.add_edge(3, 6)
    ng.add_edge(3, 7)
    ng.add_edge(4, 8)
    ng.add_edge(4, 9)
    ng.add_edge(5, 10)
    ng.add_edge(5, 11)
    ng.add_edge(6, 12)
    ng.add_edge(6, 13)
    ng.add_edge(7, 14)
    ng.add_edge(14, 15)
    ng.add_edge(7, 15, 9)
    return ng


def test_graph_dijkstra_lenght_with_weight(wng):
    """test_graph_dijkstra_lenght_with_weight."""
    path = wng.dijkstra(1, 15)
    assert len(path) == 5


def test_graph_dijkstra_start_with_weight(wng):
    """test_graph_dijkstra_start_with_weight."""
    path = wng.dijkstra(1, 15)
    assert path[0].val == 1


def test_graph_dijkstra_end_with_weight(wng):
    """test_graph_dijkstra_end_with_weight."""
    path = wng.dijkstra(1, 15)
    assert path[4].val == 15


def test_graph_bellman_lenght_with_weight(wng):
    """test_graph_bellman_lenght_with_weight."""
    path = wng.bellman(1, 15)
    assert len(path) == 5


def test_graph_bellman_start_with_weight(wng):
    """test_graph_bellman_start_with_weight."""
    path = wng.bellman(1, 15)
    assert path[0].val == 1


def test_graph_bellman_end_with_weight(wng):
    """test_graph_bellman_end_with_weight."""
    path = wng.bellman(1, 15)
    assert path[4].val == 15


def test_graph_dijkstra_not_start(ng):
    """test_graph_dijkstra_not_start."""
    with pytest.raises(KeyError):
        ng.dijkstra(16, 20)


def test_graph_dijkstra_not_end(ng):
    """test_graph_dijkstra_not_end."""
    with pytest.raises(KeyError):
        ng.dijkstra(1, 20)


def test_graph_dijkstra_no_edges():
    """test_graph_dijkstra_no_edges."""
    ng = Graph()
    ng.add_node(1)
    ng.add_node(2)
    with pytest.raises(KeyError):
        ng.dijkstra(1, 2)


def test_graph_dijkstra_no_path_to_end():
    """test_graph_dijkstra_no_path_to_end."""
    ng = Graph()
    ng.add_edge(1, 2, 5)
    ng.add_edge(1, 3, 9)
    ng.add_edge(2, 4)
    ng.add_edge(2, 5, 5)
    ng.add_edge(3, 6)
    ng.add_edge(7, 14)
    ng.add_edge(14, 15)
    with pytest.raises(IndexError):
        ng.dijkstra(1, 15)


def test_graph_bellman_not_start(ng):
    """test_graph_bellman_not_start."""
    with pytest.raises(KeyError):
        ng.bellman(16, 20)


def test_graph_bellman_not_end(ng):
    """test_graph_bellman_not_end."""
    with pytest.raises(KeyError):
        ng.bellman(1, 20)


def test_graph_bellman_no_edges():
    """test_graph_bellman_no_edges."""
    ng = Graph()
    ng.add_node(1)
    ng.add_node(2)
    with pytest.raises(KeyError):
        ng.bellman(1, 2)


def test_graph_bellman_no_path_to_end():
    """test_graph_bellman_no_path_to_end."""
    ng = Graph()
    ng.add_edge(1, 2, 5)
    ng.add_edge(1, 3, 9)
    ng.add_edge(2, 4)
    ng.add_edge(2, 5, 5)
    ng.add_edge(3, 6)
    ng.add_edge(7, 14)
    ng.add_edge(14, 15)
    with pytest.raises(IndexError):
        ng.bellman(1, 15)
