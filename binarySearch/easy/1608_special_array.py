"""
LeetCode 1608. Special Array With X Elements Greater Than or Equal X
https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

Difficulty: Easy

Problem:
You are given an array nums of non-negative integers. 
nums is considered special if there exists a number x such that 
there are exactly x numbers in nums that are greater than or equal to x.

Notice that x does not have to be an element in nums.

Return x if the array is special, otherwise, return -1. 
It can be proven that if nums is special, the value for x is unique.

Example 1:
    Input: nums = [3,5]
    Output: 2
    Explanation: There are 2 values (3 and 5) that are greater than or equal to 2.

Example 2:
    Input: nums = [0,0]
    Output: -1
    Explanation: No numbers fit the criteria for x.

Example 3:
    Input: nums = [0,4,3,0,4]
    Output: 3
    Explanation: There are 3 values that are greater than or equal to 3.
"""
from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        # TODO: Implement your solution here
        pass


def main():
    solution = Solution()
    
    # Test case 1
    print(f"Test 1: {solution.specialArray([3,5])}")  # Expected: 2
    
    # Test case 2
    print(f"Test 2: {solution.specialArray([0,0])}")  # Expected: -1
    
    # Test case 3
    print(f"Test 3: {solution.specialArray([0,4,3,0,4])}")  # Expected: 3


if __name__ == "__main__":
    main()
