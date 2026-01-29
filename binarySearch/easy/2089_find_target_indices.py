"""
LeetCode 2089. Find Target Indices After Sorting Array
https://leetcode.com/problems/find-target-indices-after-sorting-array/

Difficulty: Easy

Problem:
You are given a 0-indexed integer array nums and a target element target.

A target index is an index i such that nums[i] == target.

Return a list of the target indices of nums after sorting nums in non-decreasing order. 
If there are no target indices, return an empty list. 
The returned list must be sorted in increasing order.

Example 1:
    Input: nums = [1,2,5,2,3], target = 2
    Output: [1,2]
    Explanation: After sorting, nums is [1,2,2,3,5].
    The indices where nums[i] == 2 are 1 and 2.

Example 2:
    Input: nums = [1,2,5,2,3], target = 3
    Output: [3]
    Explanation: After sorting, nums is [1,2,2,3,5].
    The index where nums[i] == 3 is 3.

Example 3:
    Input: nums = [1,2,5,2,3], target = 5
    Output: [4]
"""
from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # TODO: Implement your solution here
        pass


def main():
    solution = Solution()
    
    # Test case 1
    print(f"Test 1: {solution.targetIndices([1,2,5,2,3], 2)}")  # Expected: [1, 2]
    
    # Test case 2
    print(f"Test 2: {solution.targetIndices([1,2,5,2,3], 3)}")  # Expected: [3]
    
    # Test case 3
    print(f"Test 3: {solution.targetIndices([1,2,5,2,3], 5)}")  # Expected: [4]


if __name__ == "__main__":
    main()
