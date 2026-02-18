class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for char in s:
            if not char.isalnum():
                continue
            cleaned += char.lower()
        
        L = 0
        R = len(cleaned) - 1
        while L < R:
            if cleaned[L] != cleaned[R]:
                return False
            L += 1
            R -= 1
        return True
