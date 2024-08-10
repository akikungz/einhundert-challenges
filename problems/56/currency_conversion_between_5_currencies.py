def convert_currency(amount: float, from_currency: str, to_currency: str) -> float:
    pass

def main():
    print(convert_currency(100.0, "USD", "EUR")) # 85
    print(convert_currency(1000.0, "JPY", "THB")) # 290.91
    
if __name__ == "__main__":
    main()