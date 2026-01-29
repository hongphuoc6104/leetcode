"""
LeetCode 1675. Minimize Deviation in Array
https://leetcode.com/problems/minimize-deviation-in-array/

Difficulty: Hard

Problem:
You are given an array nums of n positive integers.

You can perform two types of operations on any element of the array any number of times:
- If the element is even, divide it by 2.
- If the element is odd, multiply it by 2.

The deviation of the array is the maximum difference between any two elements in the array.

Return the minimum deviation the array can have after performing some number of operations.

Example 1:
    Input: nums = [1,2,3,4]
    Output: 1
    Explanation: You can transform the array to [1,2,3,2], then to [2,2,3,2], 
    then the deviation will be 3 - 2 = 1.

Example 2:
    Input: nums = [4,1,5,20,3]
    Output: 3
    Explanation: You can transform the array after two operations to [4,2,5,5,3], 
    then the deviation will be 5 - 2 = 3.

Example 3:
    Input: nums = [2,10,8]
    Output: 3
"""
from typing import List


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        # TODO: Implement your solution here
        pass


def main():
    solution = Solution()
    
    # Test case 1
    print(f"Test 1: {solution.minimumDeviation([1,2,3,4])}")  # Expected: 1
    
    # Test case 2
    print(f"Test 2: {solution.minimumDeviation([4,1,5,20,3])}")  # Expected: 3
    
    # Test case 3
    print(f"Test 3: {solution.minimumDeviation([2,10,8])}")  # Expected: 3


if __name__ == "__main__":
    main()
