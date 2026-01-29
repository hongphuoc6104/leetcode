"""
LeetCode 35. Search Insert Position
https://leetcode.com/problems/search-insert-position/

Difficulty: Easy

Problem:
Given a sorted array of distinct integers and a target value, 
return the index if the target is found. If not, return the index 
where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [1,3,5,6], target = 5
    Output: 2

Example 2:
    Input: nums = [1,3,5,6], target = 2
    Output: 1

Example 3:
    Input: nums = [1,3,5,6], target = 7
    Output: 4
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1
        while L <= R:
            mid = (L + R) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                R = mid - 1
            else:
                L = mid + 1
        return L


def main():
    solution = Solution()
    
    # Test case 1
    print(f"Test 1: {solution.searchInsert([1,3,5,6], 5)}")  # Expected: 2
    
    # Test case 2
    print(f"Test 2: {solution.searchInsert([1,3,5,6], 2)}")  # Expected: 1
    
    # Test case 3
    print(f"Test 3: {solution.searchInsert([1,3,5,6], 7)}")  # Expected: 4


if __name__ == "__main__":
    main()
