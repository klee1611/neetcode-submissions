class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = -1
        l, r = 1, max(piles) + 1

        while l < r:
            mid = (l + r) // 2
            time = sum([math.ceil(p / mid) for p in piles])
            if time > h:
                l = mid + 1
            else:
                res = mid
                r = mid

        return res