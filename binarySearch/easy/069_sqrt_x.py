"""
LeetCode 69. Sqrt(x)
https://leetcode.com/problems/sqrtx/

Difficulty: Easy

Problem:
Given a non-negative integer x, return the square root of x rounded down 
to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

Example 1:
    Input: x = 4
    Output: 2
    Explanation: The square root of 4 is 2, so we return 2.

Example 2:
    Input: x = 8
    Output: 2
    Explanation: The square root of 8 is 2.82842..., 
    and since we round it down to the nearest integer, 2 is returned.
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        # TODO: Implement your solution here
        pass


def main():
    solution = Solution()
    
    # Test case 1
    print(f"Test 1: {solution.mySqrt(4)}")  # Expected: 2
    
    # Test case 2
    print(f"Test 2: {solution.mySqrt(8)}")  # Expected: 2
    
    # Test case 3
    print(f"Test 3: {solution.mySqrt(16)}")  # Expected: 4


if __name__ == "__main__":
    main()
