# """
# LeetCode 367. Valid Perfect Square
# https://leetcode.com/problems/valid-perfect-square/

# Difficulty: Easy

# Problem:
# Given a positive integer num, return true if num is a perfect square 
# or false otherwise.

# A perfect square is an integer that is the square of an integer; 
# in other words, it is the product of some integer with itself.

# You must not use any built-in library function, such as sqrt.

# Example 1:
#     Input: num = 16
#     Output: true
#     Explanation: We return true because 4 * 4 = 16 and 4 is an integer.

# Example 2:
#     Input: num = 14
#     Output: false
#     Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.
# """


# class Solution:
#     def isPerfectSquare(self, num: int) -> bool:
#         if num < 2:
#             return True
#         left = 2
#         right = num // 2
#         while left <= right:
#             mid = left + (right - left) // 2
#             square = mid * mid
#             if square == num:
#                 return True
#             elif square < num:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         return False


# def main():
#     solution = Solution()
    
#     # Test case 1
#     print(f"Test 1: {solution.isPerfectSquare(225)}")  # Expected: True
    
#     # Test case 2
#     print(f"Test 2: {solution.isPerfectSquare(9)}")  # Expected: False
    
#     # Test case 3
#     print(f"Test 3: {solution.isPerfectSquare(19)}")  # Expected: True


# if __name__ == "__main__":
#     main()
