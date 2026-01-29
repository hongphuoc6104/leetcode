"""
LeetCode 658. Find K Closest Elements
https://leetcode.com/problems/find-k-closest-elements/

Difficulty: Medium

Problem:
Given a sorted integer array arr, two integers k and x, return the k closest 
integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:
- |a - x| < |b - x|, or
- |a - x| == |b - x| and a < b

Example 1:
    Input: arr = [1,2,3,4,5], k = 4, x = 3
    Output: [1,2,3,4]

Example 2:
    Input: arr = [1,2,3,4,5], k = 4, x = -1
    Output: [1,2,3,4]
"""
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # TODO: Implement your solution here
        pass


def main():
    solution = Solution()
    
    # Test case 1
    print(f"Test 1: {solution.findClosestElements([1,2,3,4,5], 4, 3)}")  # Expected: [1,2,3,4]
    
    # Test case 2
    print(f"Test 2: {solution.findClosestElements([1,2,3,4,5], 4, -1)}")  # Expected: [1,2,3,4]


if __name__ == "__main__":
    main()
