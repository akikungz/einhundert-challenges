from compare_length_of_two_strings import compare_string_lengths

def test_compare_length_of_two_strings():
    str1 = "apple"
    str2 = "banana"
    assert compare_string_lengths(str1, str2) ==  "The second string is longer by 1 character(s)."  