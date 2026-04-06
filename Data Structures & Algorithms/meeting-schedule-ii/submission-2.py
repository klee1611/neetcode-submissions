"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        if not n:
            return 0
        if n < 2:
            return 1

        times = []
        for intv in intervals:
            times.append((intv.start, 1))
            times.append((intv.end, -1))
        times.sort()

        rooms, res = 0, 0
        for t in times:
            rooms += t[1]
            res = max(res, rooms)

        return res