# 190. Reverse Bits
# Reverse bits of a given 32 bits unsigned integer.

# Note:
# Note that in some languages, such as Java, there is no unsigned integer type. 
# In this case, both input and output will be given as a signed integer type. 
# They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
# In Java, the compiler represents the signed integers using 2's complement notation. 
# Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1 
        return res 
        

if __name__ == '__main__':
    s = Solution()
    # Test Case 1
    # Input: 00000010100101000001111010011100 (43261596)
    # Output: 00111001011110000010100101010000 (964176192)
    n = 0b00000010100101000001111010011100
    print(f"Input: {n} ({bin(n)})")
    res = s.reverseBits(n)
    print(f"Output: {res} ({bin(res)})")
