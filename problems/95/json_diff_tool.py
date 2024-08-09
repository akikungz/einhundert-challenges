def json_diff(dict1: dict, dict2: dict) -> dict:
    # Write your code here
    pass

def main():
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
    
    print(json_diff(dict1, dict2))