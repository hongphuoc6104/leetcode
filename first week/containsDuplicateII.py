# 219. Contains Duplicate II
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

class Solution:
    # @param nums, a list of integers
    # @param k, an integer
    # @return a boolean
    def containsNearbyDuplicate(self, nums, k):
        pass

if __name__ == '__main__':
    s = Solution()
    # Test Case 1
    # Input: nums = [1,2,3,1], k = 3
    # Output: True
    nums1 = [1, 2, 3, 1]
    k1 = 3
    print(f"Input: nums = {nums1}, k = {k1}")
    print(f"Output: {s.containsNearbyDuplicate(nums1, k1)}")

    # Test Case 2
    # Input: nums = [1,0,1,1], k = 1
    # Output: True
    nums2 = [1, 0, 1, 1]
    k2 = 1
    print(f"\nInput: nums = {nums2}, k = {k2}")
    print(f"Output: {s.containsNearbyDuplicate(nums2, k2)}")

    # Test Case 3
    # Input: nums = [1,2,3,1,2,3], k = 2
    # Output: False
    nums3 = [1, 2, 3, 1, 2, 3]
    k3 = 2
    print(f"\nInput: nums = {nums3}, k = {k3}")
    print(f"Output: {s.containsNearbyDuplicate(nums3, k3)}")
