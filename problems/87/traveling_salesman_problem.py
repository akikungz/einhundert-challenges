def tsp(graph: list) -> int:
    pass

def main():
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0] 
    ]
    print(tsp(graph))  # 80
    
    graph = [
        [0, 29, 20, 21],
        [29, 0, 15, 17],
        [20, 15, 0, 28],
        [21, 17, 28, 0] 
    ]
    print(tsp(graph))  # 76