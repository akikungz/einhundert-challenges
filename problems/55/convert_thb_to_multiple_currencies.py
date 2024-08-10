def convert_thb_to_currency(amount: float, to_currency: str) -> float:
    pass

def main():
    print(convert_thb_to_currency(1000.0, "USD")) # 30.0
    print(convert_thb_to_currency(1000.0, "JPY")) # 3400.0

if __name__ == "__main__":
    main()