from maximum_subarray_sum_with_one_deletion import max_sum_with_one_deleteion

def test_maximum_subarray_sum_with_one_deletion():
    arr = [1, -2, 0, 3]
    assert max_sum_with_one_deleteion(arr) == 4
    
    arr = [1, -2, -2, 3]
    assert max_sum_with_one_deleteion(arr) == 3
    
    arr = [-1, -1, -1, -1]
    assert max_sum_with_one_deleteion(arr) == -1