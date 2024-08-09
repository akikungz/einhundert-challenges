def max_sum_with_one_deleteion(arr: list) -> int:
    pass

def main():
    arr = [1, -2, 0, 3]
    print(max_sum_with_one_deleteion(arr))  # 4
    
    arr = [1, -2, -2, 3]
    print(max_sum_with_one_deleteion(arr))  # 3
    
    arr = [-1, -1, -1, -1]
    print(max_sum_with_one_deleteion(arr))  # -1

if __name__ == "__main__":
    main()