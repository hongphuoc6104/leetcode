"""
LeetCode 875. Koko Eating Bananas
https://leetcode.com/problems/koko-eating-bananas/

Difficulty: Medium

Problem:
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas.
The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses 
some pile of bananas and eats k bananas from that pile. If the pile has less 
than k bananas, she eats all of them instead and will not eat any more bananas 
during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas 
before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:
    Input: piles = [3,6,7,11], h = 8
    Output: 4

Example 2:
    Input: piles = [30,11,23,4,20], h = 5
    Output: 30

Example 3:
    Input: piles = [30,11,23,4,20], h = 6
    Output: 23
"""
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # TODO: Implement your solution here
        pass


def main():
    solution = Solution()
    
    # Test case 1
    print(f"Test 1: {solution.minEatingSpeed([3,6,7,11], 8)}")  # Expected: 4
    
    # Test case 2
    print(f"Test 2: {solution.minEatingSpeed([30,11,23,4,20], 5)}")  # Expected: 30
    
    # Test case 3
    print(f"Test 3: {solution.minEatingSpeed([30,11,23,4,20], 6)}")  # Expected: 23


if __name__ == "__main__":
    main()
