from k_partition_subset_sum import can_partition_k_subsets

def test_k_partition_subset_sum():
    nums = [4, 3, 2, 3, 5, 2, 1]
    k = 4
    assert can_partition_k_subsets(nums, k) == True

    nums = [1, 2, 3, 4]
    k = 3
    assert can_partition_k_subsets(nums, k) == False