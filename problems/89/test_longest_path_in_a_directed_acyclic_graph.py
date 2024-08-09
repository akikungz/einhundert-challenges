from longest_path_in_a_directed_acyclic_graph import longest_path_dag

def test_longest_path_in_a_directed_acyclic_graph():
    graph = {
        1: [(2, 3), (3, 6)], 
        2: [(3, 4), (4, 11)], 
        3: [(4, 8)], 
        4: []
    }
    start_node = 1
    
    assert longest_path_dag(graph, start_node) == 15
    
    graph = {
        0: [(1, 5), (2, 3)], 
        1: [(3, 6)], 
        2: [(3, 7)], 
        3: [(4, 4)], 
        4: []
    } 
    start_node = 0
    
    assert longest_path_dag(graph, start_node) == 15