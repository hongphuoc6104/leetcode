"""
LeetCode 1011. Capacity To Ship Packages Within D Days
https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

Difficulty: Medium

Problem:
A conveyor belt has packages that must be shipped from one port to another 
within days days.

The ith package on the conveyor belt has a weight of weights[i]. 
Each day, we load the ship with packages on the conveyor belt (in the order 
given by weights). We may not load more weight than the maximum weight capacity 
of the ship.

Return the least weight capacity of the ship that will result in all the 
packages on the conveyor belt being shipped within days days.

Example 1:
    Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
    Output: 15
    Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days:
    Day 1: 1, 2, 3, 4, 5
    Day 2: 6, 7
    Day 3: 8
    Day 4: 9
    Day 5: 10

Example 2:
    Input: weights = [3,2,2,4,1,4], days = 3
    Output: 6

Example 3:
    Input: weights = [1,2,3,1,1], days = 4
    Output: 3
"""
from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # TODO: Implement your solution here
        pass


def main():
    solution = Solution()
    
    # Test case 1
    print(f"Test 1: {solution.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5)}")  # Expected: 15
    
    # Test case 2
    print(f"Test 2: {solution.shipWithinDays([3,2,2,4,1,4], 3)}")  # Expected: 6
    
    # Test case 3
    print(f"Test 3: {solution.shipWithinDays([1,2,3,1,1], 4)}")  # Expected: 3


if __name__ == "__main__":
    main()
