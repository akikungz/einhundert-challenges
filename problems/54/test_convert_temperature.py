from convert_temperature import *

def test_convert_temperature():
    assert fahrenhiet_to_celsius(32) == 0.0
    
    assert celsius_to_fahrenhiet(100) == 212.0