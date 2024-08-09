def word_break(s: str, word_set: set) -> bool:
    pass

def main():
    s = "leetcode"
    word_set = {"leet", "code"}
    
    print(word_break(s, word_set))  # True
    
    s = "applepenapple"
    word_set = {"apple", "pen"}
    
    print(word_break(s, word_set))  # True
    
    s = "catsandog"
    word_set = {"cats", "dog", "sand", "and", "cat"}
    
    print(word_break(s, word_set))  # False
    
if __name__ == "__main__":
    main()