class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        n = len(intervals)
        pre, l, r = -1, 0, n
        while l < r:
            mid = (l + r) // 2
            tmp = intervals[mid][0]
            if tmp == newInterval[0]:
                pre = mid
                break

            if intervals[mid][0] < newInterval[0]:
                pre = mid
                l = mid + 1
            else:
                r = mid

        intervals.insert(pre + 1, newInterval)
        res = []
        for i in intervals:
            print(res, i)
            if not res or i[0] > res[-1][1]:
                res.append(i)
            else:
                res[-1][1] = max(i[1], res[-1][1])

        return res