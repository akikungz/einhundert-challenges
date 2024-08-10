def group_by_unit_digit(numbers: list[int]) -> list[list[int]]:
    pass

def main():
    numbers = [21, 34, 51, 23, 37, 44, 60, 11, 91, 99]
    print(group_by_unit_digit(numbers)) # [[60], [21, 51, 11, 91], [], [23], [34, 44], [], [], [37], [], [99]]

if __name__ == "__main__":
    main()