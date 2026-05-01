class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        negative = True if x < 0 else False

        x = abs(x)
        while x:
            res = res * 10 + x % 10
            x //= 10

        res = res if not negative else -res

        if res > (1 << 31) - 1 or res < -(1 << 31):
            return 0
            
        return res