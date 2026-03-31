class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = max(piles)

        while l < r:
            mid = l + (r - l) // 2
            t = sum([math.ceil(p/mid) for p in piles])
            if t <= h:
                res = min(res, mid)
                r = mid
            else:
                l = mid + 1

        return res