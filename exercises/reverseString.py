from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Write a function that reverses a string. The input string is given as an array of characters s.
        You must do this by modifying the input array in-place with O(1) extra memory.

        Example 1:
        Input: s = ["h","e","l","l","o"]
        Output: ["o","l","l","e","h"]

        Example 2:
        Input: s = ["H","a","n","n","a","h"]
        Output: ["h","a","n","n","a","H"]
        """
        # Your code here (Code của bạn ở đây)
        if s is None or len(s) ==0:
            return
        L=0
        R=len(s) - 1 
        while L < R:
            s[L], s[R] = s[R], s[L]
            L += 1
            R -= 1