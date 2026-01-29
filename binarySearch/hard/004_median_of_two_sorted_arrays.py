"""
LeetCode 4. Median of Two Sorted Arrays
https://leetcode.com/problems/median-of-two-sorted-arrays/

Difficulty: Hard

Problem:
Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:
    Input: nums1 = [1,3], nums2 = [2]
    Output: 2.00000
    Explanation: merged array = [1,2,3] and median is 2.

Example 2:
    Input: nums1 = [1,2], nums2 = [3,4]
    Output: 2.50000
    Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # TODO: Implement your solution here
        pass


def main():
    solution = Solution()
    
    # Test case 1
    print(f"Test 1: {solution.findMedianSortedArrays([1,3], [2])}")  # Expected: 2.0
    
    # Test case 2
    print(f"Test 2: {solution.findMedianSortedArrays([1,2], [3,4])}")  # Expected: 2.5


if __name__ == "__main__":
    main()
