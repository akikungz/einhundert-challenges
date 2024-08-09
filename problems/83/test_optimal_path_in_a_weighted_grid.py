from optimal_path_in_a_weighted_grid import min_cost_path

def test_optimal_path_in_a_weighted_grid():
    grid = [
        [1, 3, 1], 
        [1, 5, 1], 
        [4, 2, 1]
    ]
    assert min_cost_path(grid) == 7
    
    grid = [
        [1, 2, 3],
        [4, 8, 2],
        [1, 5, 3]
    ]
    assert min_cost_path(grid) == 8