"""
LeetCode 74. Search a 2D Matrix
https://leetcode.com/problems/search-a-2d-matrix/

Difficulty: Medium

Problem:
You are given an m x n integer matrix matrix with the following two properties:
- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:
    Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
    Output: true

Example 2:
    Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
    Output: false
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # TODO: Implement your solution here
        pass


def main():
    solution = Solution()
    
    # Test case 1
    matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    print(f"Test 1: {solution.searchMatrix(matrix1, 3)}")  # Expected: True
    
    # Test case 2
    print(f"Test 2: {solution.searchMatrix(matrix1, 13)}")  # Expected: False


if __name__ == "__main__":
    main()
