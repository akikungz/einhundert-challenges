def find_graph_centroid(graph: dict[int, list[tuple[int, float]]]) -> tuple[int, float]:
    pass

def main():
    graph = {
        0: [(1, 1), (2, 1)],
        1: [(0, 1), (3, 1)],
        2: [(0, 1), (3, 3)],
        3: [(0, 1), (2, 3)],
    }
    
    print(find_graph_centroid(graph))  # (1, 2.0)
    
    graph = {
        0: [(1, 2), (2, 4)], 
        1: [(0, 2), (2, 1)], 
        2: [(0, 4), (1, 1), (3, 1)], 
        3: [(2, 1)] 
    } 
    
    print(find_graph_centroid(graph))  # (2, 2.0)