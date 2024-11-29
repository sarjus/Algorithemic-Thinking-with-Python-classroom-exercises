'''
Objective: The Subset Sum Problem involves determining if there exists a subset of a
given set of numbers that sums up to a specified target value. The brute-force
approach to solve this problem involves generating all possible subsets of the
set and checking if the sum of any subset equals the target value.


Author: Sarju S
Date: 30-11-2024
'''

import itertools

def subset_sum_brute_force(nums, target):
    # Iterate over all possible subset sizes (from 0 to len(nums))
    for size in range(len(nums) + 1):
        # Generate all subsets of the current size
        for subset in itertools.combinations(nums, size):
            # Check if the sum of the current subset equals the target
            if sum(subset) == target:
                return True
    return False

# Example usage
nums = [3, 34, 4, 12, 5, 2]
target = 9
if subset_sum_brute_force(nums, target):
    print(f"A subset with sum {target} exists.")
else:
    print(f"No subset with sum {target} exists.")
