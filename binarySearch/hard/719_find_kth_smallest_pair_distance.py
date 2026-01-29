"""
LeetCode 719. Find K-th Smallest Pair Distance
https://leetcode.com/problems/find-k-th-smallest-pair-distance/

Difficulty: Hard

Problem:
The distance of a pair of integers a and b is defined as the absolute 
difference between a and b.

Given an integer array nums and an integer k, return the kth smallest 
distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.

Example 1:
    Input: nums = [1,3,1], k = 1
    Output: 0
    Explanation: Here are all the pairs:
    (1,3) -> 2
    (1,1) -> 0
    (3,1) -> 2
    Then the 1st smallest distance pair is (1,1), and its distance is 0.

Example 2:
    Input: nums = [1,1,1], k = 2
    Output: 0

Example 3:
    Input: nums = [1,6,1], k = 3
    Output: 5
"""
from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # TODO: Implement your solution here
        pass


def main():
    solution = Solution()
    
    # Test case 1
    print(f"Test 1: {solution.smallestDistancePair([1,3,1], 1)}")  # Expected: 0
    
    # Test case 2
    print(f"Test 2: {solution.smallestDistancePair([1,1,1], 2)}")  # Expected: 0
    
    # Test case 3
    print(f"Test 3: {solution.smallestDistancePair([1,6,1], 3)}")  # Expected: 5


if __name__ == "__main__":
    main()
