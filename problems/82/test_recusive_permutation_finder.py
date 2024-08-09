from recusive_permutation_finder import find_permutations

def test_recusive_permutation_finder():
    test = find_permutations("abc")
    result = ["abc", "acb", "bac", "bca", "cab", "cba"]
    
    get_test(test, result)
    
    test = find_permutations("dog")
    result = ["dgo", "dog", "gdo", "god", "odg", "ogd"]
                
def get_test(test: list, result: list):
    if len(result) != len(test):
        assert False
    else:
        for item in test:
            if item not in result:
                assert False