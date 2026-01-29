"""
LeetCode 1351. Count Negative Numbers in a Sorted Matrix
https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

Difficulty: Easy

Problem:
Given a m x n matrix grid which is sorted in non-increasing order both row-wise 
and column-wise, return the number of negative numbers in grid.

Example 1:
    Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    Output: 8
    Explanation: There are 8 negatives number in the matrix.

Example 2:
    Input: grid = [[3,2],[1,0]]
    Output: 0
"""
from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # TODO: Implement your solution here
        pass


def main():
    solution = Solution()
    
    # Test case 1
    grid1 = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    print(f"Test 1: {solution.countNegatives(grid1)}")  # Expected: 8
    
    # Test case 2
    grid2 = [[3,2],[1,0]]
    print(f"Test 2: {solution.countNegatives(grid2)}")  # Expected: 0


if __name__ == "__main__":
    main()
