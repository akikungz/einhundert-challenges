from json_diff_tool import json_diff

def test_json_diff_tool():
    dict1 = {
        "name": "Alice",
        "age": 30,
        "address": {
            "city": "Wonderland",
            "zipcode": 12345
        }
    }
    
    dict2 = {
        "name": "Alice",
        "age": 31,
        "address": {
            "city": "Wonderland",
            "zipcode": 54321
        },
        "email": "alice@example.com"
    }
    
    test = json_diff(dict1, dict2)
    result = {
        "added": {
            "email": "alice@example.com"
        },
        "removed": {},
        "modified": {
            "age": {
                "from": 30,
                "to": 31
            },
            "address": {
                "zipcode": {
                    "from": 12345,
                    "to": 54321
                }
            }
        }
    }
    
    if test != result:
        for key in result:
            if key == "modified":
                for sub_l1_key in result[key]:
                    for sub_l2_key in result[key][sub_l1_key]:
                        assert test[key][sub_l1_key][sub_l2_key] == result[key][sub_l1_key][sub_l2_key]
            else:
                for sub_key in result[key]:
                    assert test[key][sub_key] == result[key][sub_key]
    else:
        assert test == result