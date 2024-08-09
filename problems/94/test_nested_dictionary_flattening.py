from nested_dictionary_flattening import flatten_dict

def test_nested_dictionary_flattening():
    d = {
        "a": 1,
        "b": {
            "c": 2,
            "d": {
                "e": 3,
                "f": 4
            }
        }
    }
    separator = '.'
    assert flatten_dict(d, separator) == {
        "a": 1,
        "b.c": 2,
        "b.d.e": 3,
        "b.d.f": 4
    }

    d = {
        "user": {
            "name": "Alice",
            "address": {
                "city": "Wonderland",
                "zip": 12345
            },
            "email": "alice@example.com"
        }
    }
    separator = '_'
    assert flatten_dict(d, separator) == {
        "user_name": "Alice",
        "user_address_city": "Wonderland",
        "user_address_zip": 12345,
        "user_email": "alice@example.com"
    }