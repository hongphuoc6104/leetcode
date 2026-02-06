# """
# LeetCode 374. Guess Number Higher or Lower
# https://leetcode.com/problems/guess-number-higher-or-lower/

# Difficulty: Easy

# Problem:
# We are playing the Guess Game. The game is as follows:
# I pick a number from 1 to n. You have to guess which number I picked.
# Every time you guess wrong, I will tell you whether the number I picked 
# is higher or lower than your guess.

# You call a pre-defined API int guess(int num), which returns three possible results:
#     -1: Your guess is higher than the number I picked (i.e. num > pick).
#      1: Your guess is lower than the number I picked (i.e. num < pick).
#      0: your guess is equal to the number I picked (i.e. num == pick).

# Return the number that I picked.

# Example 1:
#     Input: n = 10, pick = 6
#     Output: 6

# Example 2:
#     Input: n = 1, pick = 1
#     Output: 1
# """

# pick = 6  # For testing


# def guess(num: int) -> int:
#     if num > pick:
#         return -1
#     elif num < pick:
#         return 1
#     else:
#         return 0


# class Solution:
#     def guessNumber(self, n: int) -> int:
#         left = 1
#         right = n
#         while left <= right:
#             mid = left + (right - left) // 2
#             out = guess(mid)
#             if out == 0:
#                 return mid
#             elif out == -1:
#                 right = mid - 1
#             else:
#                 left = mid + 1
#         return -1


# def main():
#     global pick
#     solution = Solution()
    
#     # Test case 1
#     pick = 6
#     print(f"Test 1: {solution.guessNumber(10)}")  # Expected: 6
    
#     # Test case 2
#     pick = 12
#     print(f"Test 2: {solution.guessNumber(18)}")  # Expected: 1


# if __name__ == "__main__":
#     main()
