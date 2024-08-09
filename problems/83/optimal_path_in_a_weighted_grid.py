def min_cost_path(grid: list) -> int:
    pass

def main():
    grid = [
        [1, 3, 1], 
        [1, 5, 1], 
        [4, 2, 1]
    ]
    print(min_cost_path(grid)) # 7
    
    grid = [
        [1, 2, 3],
        [4, 8, 2],
        [1, 5, 3]
    ]
    print(min_cost_path(grid)) # 8

if __name__ == "__main__":
    main()