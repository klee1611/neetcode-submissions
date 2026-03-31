class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)+1
        res = r-1

        while l < r:
            mid = (l+r) // 2
            t = 0
            for p in piles:
                t += math.ceil(p / mid)
            if t <= h:
                res = mid
                r = mid
            else:
                l = mid + 1
        
        return r