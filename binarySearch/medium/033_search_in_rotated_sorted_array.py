"""
LeetCode 33. Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/

Difficulty: Medium

Problem:
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown 
pivot index k (1 <= k < nums.length) such that the resulting array is 
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).

Given the array nums after the possible rotation and an integer target, 
return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4

Example 2:
    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1

Example 3:
    Input: nums = [1], target = 0
    Output: -1
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # TODO: Implement your solution here
        pass


def main():
    solution = Solution()
    
    # Test case 1
    print(f"Test 1: {solution.search([4,5,6,7,0,1,2], 0)}")  # Expected: 4
    
    # Test case 2
    print(f"Test 2: {solution.search([4,5,6,7,0,1,2], 3)}")  # Expected: -1
    
    # Test case 3
    print(f"Test 3: {solution.search([1], 0)}")  # Expected: -1


if __name__ == "__main__":
    main()
