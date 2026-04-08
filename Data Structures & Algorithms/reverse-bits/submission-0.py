class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res <<= 1
            if n & (1 << i):
                res += 1
        return res