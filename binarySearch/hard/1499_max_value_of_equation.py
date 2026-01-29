"""
LeetCode 1499. Max Value of Equation
https://leetcode.com/problems/max-value-of-equation/

Difficulty: Hard

Problem:
You are given an array points containing the coordinates of points on a 2D plane, 
sorted by the x-values, where points[i] = [xi, yi] such that xi < xj for all 
1 <= i < j <= points.length. You are also given an integer k.

Return the maximum value of the equation yi + yj + |xi - xj| where 
|xi - xj| <= k and 1 <= i < j <= points.length.

It is guaranteed that there exists at least one pair of points that satisfy 
the constraint |xi - xj| <= k.

Example 1:
    Input: points = [[1,3],[2,0],[5,10],[6,-10]], k = 1
    Output: 4
    Explanation: The first two points satisfy the condition |xi - xj| <= 1 
    and if we calculate the equation we get 3 + 0 + |1 - 2| = 4. 
    Third and fourth points also satisfy the condition and give 10 + -10 + |5 - 6| = 1.

Example 2:
    Input: points = [[0,0],[3,0],[9,2]], k = 3
    Output: 3
    Explanation: Only the first two points have an absolute difference of 3 or less.
"""
from typing import List


class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        # TODO: Implement your solution here
        pass


def main():
    solution = Solution()
    
    # Test case 1
    print(f"Test 1: {solution.findMaxValueOfEquation([[1,3],[2,0],[5,10],[6,-10]], 1)}")  # Expected: 4
    
    # Test case 2
    print(f"Test 2: {solution.findMaxValueOfEquation([[0,0],[3,0],[9,2]], 3)}")  # Expected: 3


if __name__ == "__main__":
    main()
