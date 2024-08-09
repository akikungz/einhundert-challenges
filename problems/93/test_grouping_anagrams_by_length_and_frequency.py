from grouping_anagrams_by_length_and_frequency import group_anagrams

def test_grouping_anagrams_by_length_and_frequency():
    words = ["bat", "tab", "cat", "act", "tac", "rat", "tar", "art", "star", "rats"]
    
    result = {
        3: [
            ['bat', 'tab'],
            ['cat', 'act', 'tac'],
            ['rat', 'tar', 'art'],
        ],
        4: [
            ['star', 'rats'],
        ],
    }
    
    get_case(words, result)
    
    words = ["listen", "silent", "enlist", "inlets", "google", "gogole", "elgoog", "cat", "tac", "act"]
    
    result = {
        3: [
            ['cat', 'tac', 'act'],
        ],
        6: [
            ['listen', 'silent', 'enlist', 'inlets'],
            ['google', 'gogole', 'elgoog'],
        ]
    }
    
    get_case(words, result)
    
def get_case(test: list[str], result: dict[int, list[str]]):
    test_case = group_anagrams(test)
    if test_case != result:
        for key in result:
            if key not in test_case:
                assert False
            assert sorted(test_case[key]) == sorted(result[key])
    else:
        assert group_anagrams(test) == result