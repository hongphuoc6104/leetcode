"""
LeetCode 410. Split Array Largest Sum
https://leetcode.com/problems/split-array-largest-sum/

Difficulty: Hard

Problem:
Given an integer array nums and an integer k, split nums into k non-empty 
subarrays such that the largest sum of any subarray is minimized.

Return the minimized largest sum of the split.

A subarray is a contiguous part of the array.

Example 1:
    Input: nums = [7,2,5,10,8], k = 2
    Output: 18
    Explanation: There are four ways to split nums into two subarrays.
    The best way is to split it into [7,2,5] and [10,8], 
    where the largest sum among the two subarrays is only 18.

Example 2:
    Input: nums = [1,2,3,4,5], k = 2
    Output: 9
    Explanation: There are four ways to split nums into two subarrays.
    The best way is to split it into [1,2,3] and [4,5], 
    where the largest sum among the two subarrays is only 9.
"""
from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # TODO: Implement your solution here
        pass


def main():
    solution = Solution()
    
    # Test case 1
    print(f"Test 1: {solution.splitArray([7,2,5,10,8], 2)}")  # Expected: 18
    
    # Test case 2
    print(f"Test 2: {solution.splitArray([1,2,3,4,5], 2)}")  # Expected: 9


if __name__ == "__main__":
    main()
