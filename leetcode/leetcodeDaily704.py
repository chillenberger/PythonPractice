# Given an array of integers nums which is sorted in ascending order, 
# and an integer target, write a function to search target in nums. If 
# target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

import bisect

class Solution:
    # staticmethod
    def search(nums: list[int], target: int) -> int:
        index = bisect.bisect_left(nums, target)
        if index >= len(nums) or nums[index] != target:
            return -1
        return index

if __name__ == '__main__':
    print(Solution.search([-1, 0, 3, 5, 9, 12], 13))
