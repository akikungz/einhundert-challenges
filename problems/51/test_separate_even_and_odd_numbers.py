from separate_even_and_odd_numbers import separate_even_and_odd

def test_separate_even_and_odd():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert separate_even_and_odd(numbers) == ([2, 4, 6, 8, 10], [1, 3, 5, 7, 9])
    
    numbers = [1, 3, 5, 7, 9]
    assert separate_even_and_odd(numbers) == ([], [1, 3, 5, 7, 9])
    
    numbers = [2, 4, 6, 8, 10]
    assert separate_even_and_odd(numbers) == ([2, 4, 6, 8, 10], [])
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert separate_even_and_odd(numbers) == ([2, 4, 6, 8], [1, 3, 5, 7, 9])
    
    numbers = [1, 3, 5, 7, 9, 11]
    assert separate_even_and_odd(numbers) == ([], [1, 3, 5, 7, 9, 11])
    
    numbers = [2, 4, 6, 8, 10, 12]
    assert separate_even_and_odd(numbers) == ([2, 4, 6, 8, 10, 12], [])
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    assert separate_even_and_odd(numbers) == ([2, 4, 6, 8, 10], [1, 3, 5, 7, 9, 11])
    
    numbers = [1, 3, 5, 7, 9, 11, 13]
    assert separate_even_and_odd(numbers) == ([], [1, 3, 5, 7, 9, 11, 13])
    
    numbers = [2, 4, 6, 8, 10, 12, 14]
    assert separate_even_and_odd(numbers) == ([2, 4, 6, 8, 10, 12, 14], [])