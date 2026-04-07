class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)

        for i in range(n+1):
            n, count = i, 0
            while n:
                count += 1
                n &= n-1
            res[i] = count
        return res