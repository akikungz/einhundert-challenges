from find_all_divisors_of_a_given_number import find_divisors

def test_find_divisors():
    test = find_divisors(12)
    case = [1, 2, 3, 4, 6, 12]
    
    if test == case:
        assert True
    else:
        for i in test:
            assert i in case