from convert_thb_to_multiple_currencies import convert_thb_to_currency

def test_convert_thb_to_multiple_currencies():
    assert convert_thb_to_currency(1000.0, "USD") == 30.0
    assert convert_thb_to_currency(1000.0, "JPY") == 3400.0