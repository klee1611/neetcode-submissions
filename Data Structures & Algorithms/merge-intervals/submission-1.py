class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        newIntervals = []
        for i in intervals:
            if not newIntervals or i[0] > newIntervals[-1][1]:
                newIntervals.append(i)
            else:
                newIntervals[-1][1] = max(newIntervals[-1][1], i[1])

        return newIntervals