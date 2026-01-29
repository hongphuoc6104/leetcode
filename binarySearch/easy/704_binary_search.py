"""
LeetCode 704. Binary Search
https://leetcode.com/problems/binary-search/

Difficulty: Easy

Problem:
Given an array of integers nums which is sorted in ascending order, 
and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4

Example 2:
    Input: nums = [-1,0,3,5,9,12], target = 2
    Output: -1
    Explanation: 2 does not exist in nums so return -1
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # TODO: Implement your solution here
        pass


def main():
    solution = Solution()
    
    # Test case 1
    nums1 = [-1, 0, 3, 5, 9, 12]
    target1 = 9
    print(f"Test 1: {solution.search(nums1, target1)}")  # Expected: 4
    
    # Test case 2
    nums2 = [-1, 0, 3, 5, 9, 12]
    target2 = 2
    print(f"Test 2: {solution.search(nums2, target2)}")  # Expected: -1


if __name__ == "__main__":
    main()
