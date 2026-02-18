class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        while n > 0:
            a = n % 2
            n = n // 2
            b = n % 2 
            if(a == b):
                return False
        return True