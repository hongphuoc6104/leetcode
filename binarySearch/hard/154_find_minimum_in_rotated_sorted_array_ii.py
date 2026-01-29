"""
LeetCode 154. Find Minimum in Rotated Sorted Array II
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

Difficulty: Hard

Problem:
Suppose an array of length n sorted in ascending order is rotated between 
1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:
- [4,5,6,7,0,1,4] if it was rotated 4 times.
- [0,1,4,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time 
results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums that may contain duplicates, 
return the minimum element of this array.

You must decrease the overall operation steps as much as possible.

Example 1:
    Input: nums = [1,3,5]
    Output: 1

Example 2:
    Input: nums = [2,2,2,0,1]
    Output: 0
"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # TODO: Implement your solution here
        pass


def main():
    solution = Solution()
    
    # Test case 1
    print(f"Test 1: {solution.findMin([1,3,5])}")  # Expected: 1
    
    # Test case 2
    print(f"Test 2: {solution.findMin([2,2,2,0,1])}")  # Expected: 0


if __name__ == "__main__":
    main()
