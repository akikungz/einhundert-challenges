from group_numbers_by_unit_digit import group_by_unit_digit

def test_group_by_unit_digit():
    numbers = [21, 34, 51, 23, 37, 44, 60, 11, 91, 99]
    assert group_by_unit_digit(numbers) == [[60], [21, 51, 11, 91], [], [23], [34, 44], [], [], [37], [], [99]]