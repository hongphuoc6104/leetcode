# """
# LeetCode 744. Find Smallest Letter Greater Than Target
# https://leetcode.com/problems/find-smallest-letter-greater-than-target/

# Difficulty: Easy

# Problem:
# You are given an array of characters letters that is sorted in non-decreasing order,
# and a character target. There are at least two different characters in letters.

# Return the smallest character in letters that is lexicographically greater than target.
# If such a character does not exist, return the first character in letters.

# Example 1:
#     Input: letters = ["c","f","j"], target = "a"
#     Output: "c"
#     Explanation: The smallest character that is lexicographically greater than 'a' is 'c'.

# Example 2:
#     Input: letters = ["c","f","j"], target = "c"
#     Output: "f"

# Example 3:
#     Input: letters = ["x","x","y","y"], target = "z"
#     Output: "x"
# # """
# from typing import List


# class Solution:
#     def nextGreatestLetter(self, letters: List[str], target: str) -> str:
#         left = 0
#         right = len(letters) - 1
#         while left <= right:
#             mid = left + (right - left) // 2
#             if letters[mid] <= target:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         print(left) 
#         return letters[left % len(letters)]


# def main():
#     solution = Solution()
    
#     # Test case 1
#     print(f"Test 1: {solution.nextGreatestLetter(['c','f','j'], 'a')}")  # Expected: 'c'
    
#     # Test case 2
#     print(f"Test 2: {solution.nextGreatestLetter(['c','f','j'], 'c')}")  # Expected: 'f'
    
#     # Test case 3
#     print(f"Test 3: {solution.nextGreatestLetter(['x','x','y','y'], 'z')}")  # Expected: 'x'


# if __name__ == "__main__":
#     main()
