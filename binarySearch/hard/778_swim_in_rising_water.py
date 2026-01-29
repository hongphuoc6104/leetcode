"""
LeetCode 778. Swim in Rising Water
https://leetcode.com/problems/swim-in-rising-water/

Difficulty: Hard

Problem:
You are given an n x n integer matrix grid where each value grid[i][j] 
represents the elevation at that point (i, j).

The rain starts to fall. At time t, the depth of the water everywhere is t. 
You can swim from a square to another 4-directionally adjacent square if and 
only if the elevation of both squares individually are at most t.

You can swim infinite distances in zero time. Of course, you must stay within 
the boundaries of the grid during your swim.

Return the least time until you can reach the bottom right square (n - 1, n - 1) 
starting from the top left square (0, 0).

Example 1:
    Input: grid = [[0,2],[1,3]]
    Output: 3
    Explanation:
    At time 0, you are in grid location (0, 0).
    You cannot go anywhere else because 4-directionally adjacent neighbors 
    have a higher elevation than t = 0.
    You cannot reach point (1, 1) until time 3.

Example 2:
    Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
    Output: 16
"""
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # TODO: Implement your solution here
        pass


def main():
    solution = Solution()
    
    # Test case 1
    print(f"Test 1: {solution.swimInWater([[0,2],[1,3]])}")  # Expected: 3
    
    # Test case 2
    grid2 = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
    print(f"Test 2: {solution.swimInWater(grid2)}")  # Expected: 16


if __name__ == "__main__":
    main()
