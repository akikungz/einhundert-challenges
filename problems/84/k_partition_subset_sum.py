def can_partition_k_subsets(nums: list[int], k: int) -> bool:
    pass

def main():
    nums = [4, 3, 2, 3, 5, 2, 1]
    k = 4
    print(can_partition_k_subsets(nums, k))  # True
    
    nums = [1, 2, 3, 4]
    k = 3
    print(can_partition_k_subsets(nums, k))  # False

if __name__ == "__main__":
    main()