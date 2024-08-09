from minimum_edit_distance_with_three_operations import min_edit_distance

def test_minimum_edit_distance_with_three_operations():
    str1 = "kitten"
    str2 = "sitting"
    assert min_edit_distance(str1, str2) == 3
    
    str1 = "flaw"
    str2 = "lawn"
    assert min_edit_distance(str1, str2) == 2