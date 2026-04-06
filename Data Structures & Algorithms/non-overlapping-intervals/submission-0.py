class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n == 1:
            return 0

        intervals.sort()
        res = [intervals[0]]
        for intv in intervals:
            if intv[1] < res[-1][1]:
                res[-1] = intv

            if intv[0] >= res[-1][1]:
                res.append(intv)
            
        return len(intervals) - len(res)