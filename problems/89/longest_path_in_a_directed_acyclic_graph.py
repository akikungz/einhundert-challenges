def longest_path_dag(graph: dict, start_node: int) -> int:
    pass

def main():
    graph = {
        1: [(2, 3), (3, 6)], 
        2: [(3, 4), (4, 11)], 
        3: [(4, 8)], 
        4: []
    }
    start_node = 1
    
    print(longest_path_dag(graph, start_node))  # 15
    
    graph = {
        0: [(1, 5), (2, 3)], 
        1: [(3, 6)], 
        2: [(3, 7)], 
        3: [(4, 4)], 
        4: []
    } 
    start_node = 0
    
    print(longest_path_dag(graph, start_node))  # 15

if __name__ == "__main__":
    main()