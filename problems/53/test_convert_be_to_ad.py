from convert_be_to_ad import convert_be_to_ad

def test_convert_be_to_ad():
    assert convert_be_to_ad(2567) == 2024
    assert convert_be_to_ad(2566) == 2023
    assert convert_be_to_ad(2565) == 2022
    assert convert_be_to_ad(2564) == 2021
    assert convert_be_to_ad(2563) == 2020