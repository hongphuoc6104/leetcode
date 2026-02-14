# https://leetcode.com/problems/maximum-average-subarray-i/
# 643. Maximum Average Subarray I

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        L = 0
        R = k
        sum_current = 0
        sum_max = 0
        for i in range(R):
            sum_max += nums[i]
        sum_current = sum_max
        
        while R < len(nums):
            sum_current += nums[R]
            sum_current -= nums[L]
            L += 1
            R += 1
            sum_max = max(sum_max, sum_current)
        return sum_max/k

