"""
LeetCode 162. Find Peak Element
https://leetcode.com/problems/find-peak-element/

Difficulty: Medium

Problem:
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. 
If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is 
always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

Example 1:
    Input: nums = [1,2,3,1]
    Output: 2
    Explanation: 3 is a peak element and your function should return the index 2.

Example 2:
    Input: nums = [1,2,1,3,5,6,4]
    Output: 5
    Explanation: Your function can return either index 1 where the peak is 2, 
    or index 5 where the peak is 6.
"""
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # TODO: Implement your solution here
        pass


def main():
    solution = Solution()
    
    # Test case 1
    print(f"Test 1: {solution.findPeakElement([1,2,3,1])}")  # Expected: 2
    
    # Test case 2
    result = solution.findPeakElement([1,2,1,3,5,6,4])
    print(f"Test 2: {result}")  # Expected: 1 or 5


if __name__ == "__main__":
    main()
