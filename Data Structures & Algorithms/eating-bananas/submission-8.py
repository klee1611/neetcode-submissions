class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)+1
        res = 0

        while l < r:
            mid = (l + r) // 2
            hour = sum([math.ceil(p/mid) for p in piles])
            if hour > h:
                l = mid + 1
            else:
                res = mid
                r = mid

        return res