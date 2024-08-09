def flatten_dict(d: dict, separator: str = '.') -> dict:
    pass

def main():
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
    print(flatten_dict(d, separator))
    
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
    print(flatten_dict(d, separator))