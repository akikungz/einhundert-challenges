from currency_conversion_between_5_currencies import convert_currency

def test_convert_currency():
    # 1 USD = 32 THB
    # 1 USD = 0.85 EUR
    # 1 USD = 110 JPY
    # 1 USD = 0.75 GBP
    
    assert convert_currency(100.0, "USD", "THB") == 3200.0
    assert convert_currency(100.0, "USD", "EUR") == 85.0
    assert convert_currency(100.0, "USD", "JPY") == 11000.0
    assert convert_currency(100.0, "USD", "GBP") == 75.0
    assert convert_currency(100.0, "THB", "USD") == 3.125
    assert convert_currency(100.0, "EUR", "USD") == 117.6470588235294
    assert convert_currency(100.0, "JPY", "USD") == 0.9090909090909091
    assert convert_currency(100.0, "GBP", "USD") == 133.33333333333334
    assert convert_currency(100.0, "THB", "EUR") == 2.3529411764705883