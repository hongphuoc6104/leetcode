"""
LeetCode 668. Kth Smallest Number in Multiplication Table
https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/

Difficulty: Hard

Problem:
Nearly everyone has used the Multiplication Table. The multiplication table 
of size m x n is an integer matrix mat where mat[i][j] == i * j (1-indexed).

Given three integers m, n, and k, return the kth smallest element in the 
m x n multiplication table.

Example 1:
    Input: m = 3, n = 3, k = 5
    Output: 3
    Explanation: The 5th smallest number is 3.
    Multiplication Table:
    1 2 3
    2 4 6
    3 6 9

Example 2:
    Input: m = 2, n = 3, k = 6
    Output: 6
    Explanation: The 6th smallest number is 6.
    Multiplication Table:
    1 2 3
    2 4 6
"""


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        # TODO: Implement your solution here
        pass


def main():
    solution = Solution()
    
    # Test case 1
    print(f"Test 1: {solution.findKthNumber(3, 3, 5)}")  # Expected: 3
    
    # Test case 2
    print(f"Test 2: {solution.findKthNumber(2, 3, 6)}")  # Expected: 6


if __name__ == "__main__":
    main()
