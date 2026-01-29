"""
LeetCode 34. Find First and Last Position of Element in Sorted Array
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Difficulty: Medium

Problem:
Given an array of integers nums sorted in non-decreasing order, 
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]

Example 2:
    Input: nums = [5,7,7,8,8,10], target = 6
    Output: [-1,-1]

Example 3:
    Input: nums = [], target = 0
    Output: [-1,-1]
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # TODO: Implement your solution here
        pass


def main():
    solution = Solution()
    
    # Test case 1
    print(f"Test 1: {solution.searchRange([5,7,7,8,8,10], 8)}")  # Expected: [3, 4]
    
    # Test case 2
    print(f"Test 2: {solution.searchRange([5,7,7,8,8,10], 6)}")  # Expected: [-1, -1]
    
    # Test case 3
    print(f"Test 3: {solution.searchRange([], 0)}")  # Expected: [-1, -1]


if __name__ == "__main__":
    main()
