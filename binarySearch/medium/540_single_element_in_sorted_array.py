"""
LeetCode 540. Single Element in a Sorted Array
https://leetcode.com/problems/single-element-in-a-sorted-array/

Difficulty: Medium

Problem:
You are given a sorted array consisting of only integers where every element 
appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

Example 1:
    Input: nums = [1,1,2,3,3,4,4,8,8]
    Output: 2

Example 2:
    Input: nums = [3,3,7,7,10,11,11]
    Output: 10
"""
from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # TODO: Implement your solution here
        pass


def main():
    solution = Solution()
    
    # Test case 1
    print(f"Test 1: {solution.singleNonDuplicate([1,1,2,3,3,4,4,8,8])}")  # Expected: 2
    
    # Test case 2
    print(f"Test 2: {solution.singleNonDuplicate([3,3,7,7,10,11,11])}")  # Expected: 10


if __name__ == "__main__":
    main()
