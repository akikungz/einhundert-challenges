from traveling_salesman_problem import tsp

def test_traveling_salesman_problem():
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0] 
    ]
    assert tsp(graph) == 80
    
    graph = [
        [0, 29, 20, 21],
        [29, 0, 15, 17],
        [20, 15, 0, 28],
        [21, 17, 28, 0] 
    ]
    assert tsp(graph) == 76