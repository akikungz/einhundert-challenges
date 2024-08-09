from graph_centroid import find_graph_centroid

def test_graph_centroid():
    graph = {
        0: [(1, 1), (2, 1)],
        1: [(0, 1), (3, 1)],
        2: [(0, 1), (3, 3)],
        3: [(0, 1), (2, 3)],
    }

    assert find_graph_centroid(graph) == (1, 2.0)

    graph = {
        0: [(1, 2), (2, 4)],
        1: [(0, 2), (2, 1)],
        2: [(0, 4), (1, 1), (3, 1)],
        3: [(2, 1)]
    }

    assert find_graph_centroid(graph) == (2, 2.0)
