from word_break_problem_with_memoization_using_set import word_break

def test_word_break_problem_with_memoization_using_set():
    s = "leetcode"
    word_set = {"leet", "code"}
    
    assert word_break(s, word_set) == True
    
    s = "applepenapple"
    word_set = {"apple", "pen"}
    
    assert word_break(s, word_set) == True
    
    s = "catsandog"
    word_set = {"cats", "dog", "sand", "and", "cat"}
    
    assert word_break(s, word_set) == False