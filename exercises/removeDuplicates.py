# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# 26. Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        L = 0
        R = 1
        while R < len(nums):
            if nums[L] == nums[R]:
                R += 1
            else:
                L += 1
                nums[L] = nums[R]
                R += 1
        return L + 1
        
