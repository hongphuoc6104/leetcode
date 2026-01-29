"""
LeetCode 878. Nth Magical Number
https://leetcode.com/problems/nth-magical-number/

Difficulty: Hard

Problem:
A positive integer is magical if it is divisible by either a or b.

Given the three integers n, a, and b, return the nth magical number. 
Since the answer may be very large, return it modulo 10^9 + 7.

Example 1:
    Input: n = 1, a = 2, b = 3
    Output: 2

Example 2:
    Input: n = 4, a = 2, b = 3
    Output: 6

Example 3:
    Input: n = 5, a = 2, b = 4
    Output: 10

Constraints:
    1 <= n <= 10^9
    2 <= a, b <= 4 * 10^4
"""


class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        # TODO: Implement your solution here
        pass


def main():
    solution = Solution()
    
    # Test case 1
    print(f"Test 1: {solution.nthMagicalNumber(1, 2, 3)}")  # Expected: 2
    
    # Test case 2
    print(f"Test 2: {solution.nthMagicalNumber(4, 2, 3)}")  # Expected: 6
    
    # Test case 3
    print(f"Test 3: {solution.nthMagicalNumber(5, 2, 4)}")  # Expected: 10


if __name__ == "__main__":
    main()
